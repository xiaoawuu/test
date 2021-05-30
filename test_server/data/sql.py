import pyodbc
from test_server.data.mysqls import Data


class ODBC:
	def __init__(self, type, DRIVER='{SQL Server}'):
		self.data = Data().config(type)
		self.server = self.data['host']
		self.uid = self.data['account']
		self.pwd = self.data['pwd']
		self.db = self.data['library_name']
		self.DRIVER = DRIVER

	def GetConnect(self):
		# table_s = Data().config(types)
		if not self.db:
			raise (NameError, '没有设置数据库信息!')
		self.conn = pyodbc.connect(SERVER=self.server, UID=self.uid, PWD=self.pwd, DATABASE=self.db, DRIVER=self.DRIVER)
		cur = self.conn.cursor()
		if not cur:
			raise (NameError, '连接数据库失败!')
		else:
			return cur

	def ExecQuery(self, sql):
		cur = self.GetConnect()
		cur.execute(sql)
		resList = cur.fetchall()

		self.conn.close()
		return resList

	def ExecNonQuery(self, sql):
		cur = self.GetConnect()
		cur.execute(sql)
		self.conn.commit()
		self.conn.close()


def sql_select(data, type='jy_live_r'):
	ms = ODBC(type)
	sql = ms.ExecQuery(data)
	return sql


def sql_exec(data, type='jy_live_r'):
	ms = ODBC(type)
	sql = ms.ExecNonQuery(data)
	return sql
