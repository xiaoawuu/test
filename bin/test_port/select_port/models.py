import pymysql
import pymysql.cursors
import configparser


def config(environment):
    conf = configparser.ConfigParser()
    conf.read('sql_configuration_file.ini')
    host = conf.get(str(environment), 'host')
    account = conf.get(str(environment), 'account')
    pwd=conf.get(str(environment),'pwd')
    library_name=conf.get(str(environment),'library_name')
    return {"host":host,"account":account,"pwd":pwd,"library_name":library_name}

def query(types,sql):
    data = config(types)
    print(data)
    try:
        conn = pymysql.connect(host=data["host"],user=data["account"],
                               passwd=data["pwd"], db=data["library_name"], charset='utf8')
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql)

        data_list = []
        for i in cur.fetchall():
            data_list.append(i)
        return data_list
    finally:conn.close()

# sql = "SELECT order_id FROM tms_wl_freight WHERE freight_id = 'DO-202003000043' or freight_id='DO-202003000033'"
# a = query('tms_test',sql)
# print(a)

