import pymysql
import pymysql.cursors
import configparser
class Data():
    def __init__(self):
        pass
    def config(self,environment):
        conf = configparser.ConfigParser()
        conf.read('C:\\test_server\\test_server\data\sql_configuration_file.ini')
        host = conf.get(str(environment), 'host')
        account = conf.get(str(environment), 'account')
        pwd=conf.get(str(environment),'pwd')
        library_name=conf.get(str(environment),'library_name')
        return {"host":host,"account":account,"pwd":pwd,"library_name":library_name}

    def query(self,types,sql):
        data = Data().config(types)
        try:
            self.conn = pymysql.connect(host=data["host"],user=data["account"],
                                   passwd=data["pwd"], db=data["library_name"], charset='utf8')
            cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
            cur.execute(sql)
            return cur.fetchall()
        finally:self.conn.close()

# aa= "SELECT id,bank,number FROM `zyb_pay_bankcard` WHERE bank_authid = '132521197806153017' AND del != 1 ORDER BY id DESC LIMIT 1;"
# sql = "SELECT id FROM `zyb_db`.`zyb_customer` WHERE `mobile` = '18866478743';"
# d = Data()
# a = d.query('zyb_live_r',sql)
# print(a)
