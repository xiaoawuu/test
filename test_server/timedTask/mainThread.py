
class mainThread():
	def __init__(self):
		pass
	def timing(self):
		pass
# from test_server.tests import read

import schedule
import time


import schedule
import time
import datetime

def is_num_by_except(num):
	try:
		int(num)
		return True
	except ValueError:
		return False

import base64
from test_server.data.sql import sql_select,sql_exec

def update_base64():
	# table_s = sql_select("SELECT id,recommend_mobile FROM biz_invite_code WHERE recommend_mobile LIKE 'MT%';")
	data = sql_select("SELECT id,recommend_mobile FROM biz_invite_code WHERE recommend_mobile != '' AND id > 11356;")
	for i in data:
		if not is_num_by_except(i[1]):
			try:
				temp = base64.b64decode(i[1].replace('\n', '').replace('\r', ''))
				sql_exec(
					"UPDATE biz_invite_code SET recommend_mobile = '{}' WHERE id = {};".format(temp.decode(), i[0]))
				print(i[1], '转换为：', temp.decode())
			except:
				break



def job1():
	data = '执行job1()，执行时间是:{}'.format(time.strftime('%Y-%m-%d %H:%M:%S'))
	print(data)
	# read(table_s)

# def job2():
	# table_s = '执行job2()，执行时间是:{}'.format(time.strftime('%Y-%m-%d %H:%M:%S'))
	# read(table_s)


def job3():
	data = '每分钟执行一次,执行时间是:{}'.format(time.strftime('%Y-%m-%d %H:%M:%S'))
	update_base64()
	print(data)

# def job4():
# 	table_s = '执行job4(),每天01:00点执行,执行时间是:{}'.format(time.strftime('%Y-%m-%d %H:%M:%S'))
# 	read(table_s)
# def job5():
# 	table_s = '执行job5()，执行时间是:{}'.format(time.strftime('%Y-%m-%d %H:%M:%S'))
# 	read(table_s)
# job3()
if __name__ == '__main__':
# 	# schedule.every(10).seconds.do(job1)
# 	# schedule.every(30).seconds.do(job2)
	schedule.every(1).minutes.do(job3)
	# schedule.every().day.at('01:00').do(job4)
	# schedule.every(5).to(10).seconds.do(job5)
	while True:
		schedule.run_pending()

