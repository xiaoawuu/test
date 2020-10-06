def is_number(s):
    try:
        float(s)
        return False
    except ValueError:
        return True

