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
    DELETE FROM zyb_customer WHERE id = '54'; DELETE FROM zyb_driver_person_cert WHERE user_id = '54'; 
    '''

    print(sql_('zyb_test', sql))




