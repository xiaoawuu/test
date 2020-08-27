
class mainThread():
	def __init__(self):
		pass
	def timing(self):
		pass
from test_server.tests import read

import schedule
import time


import schedule
import time
import datetime

def job1():
	data = '执行job1()，执行时间是:{}'.format(time.strftime('%Y-%m-%d %H:%M:%S'))
	read(data)

def job2():
	data = '执行job2()，执行时间是:{}'.format(time.strftime('%Y-%m-%d %H:%M:%S'))
	read(data)


def job3():
	data = '执行job3(),每小时执行一次,执行时间是:{}'.format(time.strftime('%Y-%m-%d %H:%M:%S'))
	print(read(data))

def job4():
	data = '执行job4(),每天01:00点执行,执行时间是:{}'.format(time.strftime('%Y-%m-%d %H:%M:%S'))
	read(data)
def job5():
	data = '执行job5()，执行时间是:{}'.format(time.strftime('%Y-%m-%d %H:%M:%S'))
	read(data)
# job3()
if __name__ == '__main__':
# 	# schedule.every(10).seconds.do(job1)
# 	# schedule.every(30).seconds.do(job2)
	schedule.every(60).minutes.do(job3)
	schedule.every().day.at('01:00').do(job4)
	# schedule.every(5).to(10).seconds.do(job5)
	while True:
		schedule.run_pending()