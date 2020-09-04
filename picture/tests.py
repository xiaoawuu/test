# print(sys.path)
from test_server.data import mysqls

'''
['C:\\test_server\\test_server',
 'C:\\test_server',
  'C:\\test_server\\bin\\test_port\\venv\\Scripts\\python37.zip',
   'C:\\install_file\\python3\\DLLs', 'C:\\install_file\\python3\\lib',
    'C:\\install_file\\python3', 'C:\\test_server\\bin\\test_port\\venv', 
    'C:\\test_server\\bin\\test_port\\venv\\lib\\site-packages', 
    'C:\\test_server\\bin\\test_port\\venv\\lib\\site-packages\\setuptools-40.8.0-py3.7.egg',
     'C:\\test_server\\bin\\test_port\\venv\\lib\\site-packages\\pip-19.0.3-py3.7.egg']
'''


def tests():
	print('------------')
	return True


# def test():
# 	list = ['LO-202008009374', 'LO-202008009375', 'LO-202008009376', 'LO-202008009377', 'LO-202008009378']
# 	dict = {}
# 	for i in list:
# 		print('循环：',i)
# 		sql = "SELECT freight_id FROM tms_wl_freight WHERE first_order_id ='{}';".format(i)
# 		data = mysqls.Data().query('tms_test', sql)
# 		dict[i] = data[0]['freight_id']
# 	return dict
# # print(max('4','0','1'))
#
# a= mysqls.Data().query('tms_test',"SELECT driver_day_count FROM tms_sys_order_limit WHERE c_id = (SELECT c_id FROM tms_wl_user WHERE user_name = 'AHD0285');")
#
# print(a)


# f = open("data1.txt","r")   #设置文件对象
# f.close() #关闭文件


# 为了方便，避免忘记close掉这个文件对象，可以用下面这种方式替代
def read():
	print(123456789)
	data = '123456789asdf'
	try:

		with open('data.txt', "a", encoding="utf-8") as f:  # 设置文件对象
			f.write(str(data) + "\n")  # 可以是随便对文件的操作
			return True
	except Exception as e:
		return '异常：{}'.format(e)
	finally:
		f.close()


# read()

# 导入 base64模块
import base64

# 给定需要转换的字符串
str1 = "18007530111"

# 需要转成2进制格式才可以转换，所以我们这里再手动转换一下
result = base64.b64encode(str1.encode())

# 打印转换后的结果
# print('转换后的结果 -->  ',result)

# 再把加密后的结果解码7483
temp = base64.b64decode('6Zq+6YGT5Yeg54K557uT5p2f')


# 同样的，解码后的结0果是二进制，我们再转换一下
# print(temp.decode())
# A = base64.b64encode(temp.encode(encoding='utf8'))
# print(str(A, 'utf8'))
# read('ahuau')
def is_num_by_except(num):
	try:
		int(num)
		return True
	except ValueError:
		return False


from test_server.data.sql import sql_select, sql_exec


def update_base64():
	# data = sql_select("SELECT id,recommend_mobile FROM biz_invite_code WHERE recommend_mobile LIKE 'MT%';")
	data = sql_select("SELECT id,recommend_mobile FROM biz_invite_code WHERE recommend_mobile != ''")
	for i in data:
		if not is_num_by_except(i[1]):
			try:
				temp = base64.b64decode(i[1].replace('\n', '').replace('\r', ''))
				sql_exec(
					"UPDATE biz_invite_code SET recommend_mobile = '{}' WHERE id = {};".format(temp.decode(), i[0]))
				print(i[1], '转换为：', temp.decode())
			except:
				continue


# update_base64()

mobile = {}
import requests, json


def requestsPort(user_id, new_mobile):
	'''
	TP5修改手机号
	:param user_id:
	:param new_mobile:
	:return:
	'''
	# url=None
	url = "https://myadmin-api.zyb56.com/customer/changeUserMobile"
	re_data = {
		"token": "53d1ad19e6487f17b9b728f928837143",
		"id": str(user_id),
		"mobile": new_mobile
	}
	try:
		headers = {
			"Content-Type": "application/json; charset=UTF-8"
		}
		response = requests.post(url, data=json.dumps(re_data), headers=headers)
		return response.json()
	except:
		return '异常'


from test_server.data.mysqls import Data


def updateMobile():
	for index, i in mobile.items():
		print('index:', index, "i", i)
		user_id = Data().query('zyb_live_r',
							   "SELECT id FROM `zyb_db`.`zyb_customer` WHERE `mobile` = '{}';".format(index))
		if user_id == ():
			continue
		print('user_id：', user_id[0]["id"], '旧手机号：', index, '新手机号：', i)
	# print(requestsPort(user_id[0]["id"], i))


# updateMobile()
import datetime

# def getYesterday():
# 	yesterday = datetime.date.today() + datetime.timedelta(-1)
# 	return yesterday
# 输出
# print(getYesterday())

import time
# print()


import urllib
import urllib.request


def get_image(url, stuNum):
	try:
		request = urllib.request.Request(url)
		response = urllib.request.urlopen(request)
		get_img = response.read()
		with open('C:\\test_server\picture' + '_' + str(stuNum) + '.jpg',
				  'wb') as fp:
			fp.write(get_img)
			print('图片下载完成')
	except:
		print('访问空')


get_image('http://app.juyuanpark.com/Resources/UserPicture/13599/d1bce3c59db4e4bac18b017e9616e19.png','222')