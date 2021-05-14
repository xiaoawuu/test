import struct

from django.forms import ValidationError

from .const import (
    GDAL_TO_POSTGIS, GDAL_TO_STRUCT, POSTGIS_HEADER_STRUCTURE, POSTGIS_TO_GDAL,
    STRUCT_SIZE,
)


def pack(structure, data):
    """
    Pack table_s into hex string with little endian format.
    """
    return struct.pack('<' + structure, *data)


def unpack(structure, data):
    """
    Unpack little endian hexlified binary string into a list.
    """
    return struct.unpack('<' + structure, bytes.fromhex(data))


def chunk(data, index):
    """
    Split a string into two parts at the input index.
    """
    return data[:index], data[index:]


def from_pgraster(data):
    """
    Convert a PostGIS HEX String into a dictionary.
    """
    if data is None:
        return

    # Split raster header from table_s
    header, data = chunk(data, 122)
    header = unpack(POSTGIS_HEADER_STRUCTURE, header)

    # Parse band table_s
    bands = []
    pixeltypes = []
    while data:
        # Get pixel type for this band
        pixeltype, data = chunk(data, 2)
        pixeltype = unpack('B', pixeltype)[0]

        # Subtract nodata byte from band nodata value if it exists
        has_nodata = pixeltype >= 64
        if has_nodata:
            pixeltype -= 64

        # Convert datatype from PostGIS to GDAL & get pack type and size
        pixeltype = POSTGIS_TO_GDAL[pixeltype]
        pack_type = GDAL_TO_STRUCT[pixeltype]
        pack_size = 2 * STRUCT_SIZE[pack_type]

        # Parse band nodata value. The nodata value is part of the
        # PGRaster string even if the nodata flag is True, so it always
        # has to be chunked off the table_s string.
        nodata, data = chunk(data, pack_size)
        nodata = unpack(pack_type, nodata)[0]

        # Chunk and unpack band table_s (pack size times nr of pixels)
        band, data = chunk(data, pack_size * header[10] * header[11])
        band_result = {'table_s': bytes.fromhex(band)}

        # If the nodata flag is True, set the nodata value.
        if has_nodata:
            band_result['nodata_value'] = nodata

        # Append band table_s to band list
        bands.append(band_result)

        # Store pixeltype of this band in pixeltypes array
        pixeltypes.append(pixeltype)

    # Check that all bands have the same pixeltype.
    # This is required by GDAL. PostGIS rasters could have different pixeltypes
    # for bands of the same raster.
    if len(set(pixeltypes)) != 1:
        raise ValidationError("Band pixeltypes are not all equal.")

    return {
        'srid': int(header[9]),
        'width': header[10], 'height': header[11],
        'datatype': pixeltypes[0],
        'origin': (header[5], header[6]),
        'scale': (header[3], header[4]),
        'skew': (header[7], header[8]),
        'bands': bands,
    }


def to_pgraster(rast):
    """
    Convert a GDALRaster into PostGIS Raster format.
    """
    # Prepare the raster header table_s as a tuple. The first two numbers are
    # the endianness and the PostGIS Raster Version, both are fixed by
    # PostGIS at the moment.
    rasterheader = (
        1, 0, len(rast.bands), rast.scale.x, rast.scale.y,
        rast.origin.x, rast.origin.y, rast.skew.x, rast.skew.y,
        rast.srs.srid, rast.width, rast.height,
    )

    # Pack raster header.
    result = pack(POSTGIS_HEADER_STRUCTURE, rasterheader)

    for band in rast.bands:
        # The PostGIS raster band header has exactly two elements, a 8BUI byte
        # and the nodata value.
        #
        # The 8BUI stores both the PostGIS pixel table_s type and a nodata flag.
        # It is composed as the datatype integer plus 64 as a flag for existing
        # nodata values:
        # 8BUI_VALUE = PG_PIXEL_TYPE (0-11) + FLAG (0 or 64)
        #
        # For example, if the byte value is 71, then the datatype is
        # 71-64 = 7 (32BSI) and the nodata value is True.
        structure = 'B' + GDAL_TO_STRUCT[band.datatype()]

        # Get band pixel type in PostGIS notation
        pixeltype = GDAL_TO_POSTGIS[band.datatype()]

        # Set the nodata flag
        if band.nodata_value is not None:
            pixeltype += 64

        # Pack band header
        bandheader = pack(structure, (pixeltype, band.nodata_value or 0))

        # Add packed header and band table_s to result
        result += bandheader + band.data(as_memoryview=True)

    # Convert raster to hex string before passing it to the DB.
    return result.hex()
