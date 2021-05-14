import pymysql
import pymysql.cursors
import configparser


class Data():
    def __init__(self):
        pass

    def config(self, environment):
        conf = configparser.ConfigParser()
        conf.read(r'C:\test_server\test\test_server\data\sql_configuration_file.ini')
        host = conf.get(str(environment), 'host')
        account = conf.get(str(environment), 'account')
        pwd = conf.get(str(environment), 'pwd')
        library_name = conf.get(str(environment), 'library_name')
        return {"host": host, "account": account, "pwd": pwd, "library_name": library_name}

    def query(self, types, sql):
        data = Data().config(types)
        try:
            self.conn = pymysql.connect(host=data["host"], user=data["account"],
                                        passwd=data["pwd"], db=data["library_name"], charset='utf8')
            cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
            cur.execute(sql)
            self.conn.commit()
            return cur.fetchall()
        except Exception as err:
            return 'SQL_ERR:',err

        finally:
            self.conn.close()

if __name__ == '__main__':
    sql_ = Data().query
    sql = '''
        SELECT
        driver_mobile,
        driver_number,
        loading_date,
        loading_x_y,
        unload_x_y,
        CONCAT(loading_province,loading_city,loading_district,loading_address) a,
        CONCAT(unload_province,unload_city,unload_district,unload_address) b
    FROM
        tms_wl_freight A
        JOIN tms_wl_order_particulars B ON A.first_order_id = B.first_order_id 
    WHERE
        freight_id = 'DO-202103003483';
    '''

    print(sql_('tms_test', sql))




