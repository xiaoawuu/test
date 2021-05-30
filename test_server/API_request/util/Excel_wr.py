import xlrd,json
from test_server.API_request.table_s.port_parameter import add
from test_server.API_request.table_s.variable import set_variable,get_variable,transition_variable
from test_server.API_request.util.parameterization import parameterization_str
from test_server.API_request.util.print_ import *
from test_server.API_request.util.request_fun import fron_data, test_port_from_data
from test_server.API_request.util.responseJSON import *


def portDataVerify(dataList):
	if type(dataList) != list:
		return responseJSON_0(msg='校验Excel接口数据请传List格式数据!',data=dataList)
	if dataList[3] == '':
		return responseJSON_1()
	try:
		jsonData = json.loads(dataList[3])
		return responseJSON_1(msg='转换JSON格式成功!',data=jsonData)
	except json.decoder.JSONDecodeError as ERR:
		return responseJSON_0('接口请求参数非JSON格式!',data=ERR)
	except Exception as ERR:
		return responseJSON_0(msg='portDataVerify function error',data=ERR)


# if __name__ == '__main__':
# 	print(portDataVerify(['/api/captcha/captcha', '获取登录验证token', 'cToken = responses.data.cToken,captcha = responses.data.captcha', '']))
# 	print(portDataVerify(['/api/login/wllogin', '登录', 'wlToken = responses.data.wlToken', '{\n  "username": "XLM0042",\n  "pwd": "123456",\n  "cToken": "4931374c-ba4d-4127-91c4-036e891fa1bd",\n  "captcha": "<captcha>",\n  "isLongLogin": "0"\n}']))
# 	print(portDataVerify(['/api/freight/queryFreightPage', '获取列表', '', '{\n  "wlToken": "<wlToken>",\n  "pageNo": "1",\n  "pageSize": "20",\n  "type": "0"\n}']))


class Excel(object):
	def __init__(self):
		self.url = r'C:\Users\Administrator\Desktop\测试.xls'
		self.open_excel = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\测试.xls')
		self.port_sheet =self.open_excel.sheets()[0] # 打开第一张表
		self.config_sheet = self.open_excel.sheets()[1]  # 打开第二张表

	def config(self):
		config_sheet = self.config_sheet.nrows  # 获取表的行数
		config = dict()
		for i in range(config_sheet):  # 循环逐行打
			if i == 0:  # 跳过第一行
				continue
			config[self.config_sheet.row_values(i)[:2][0]] = self.config_sheet.row_values(i)[:2][1]
		return config

	def ExcelR(self):
		nRows = self.port_sheet.nrows  # 获取表的行数
		for i in range(nRows):  # 循环逐行打
			if i == 0:
				continue
			dataList = self.port_sheet.row_values(i)[:4]  # 取前四列
			# portDataVerify 校验接口数据是否正确！
			verify = portDataVerify(dataList)
			if verify['code'] == 0:
				return verify
			# 请求参数：参数化
			request_data = parameterization_str(json.loads(dataList[3]))
			if request_data['code'] == 0:
				return request_data
			# 请求接口
			responses = test_port_from_data(self.config()['url'] + dataList[0], request_data['data'])
			if responses['code'] ==0:
				return responses
			# 设置变量
			print_suc(responses)
			transition = transition_variable(responses['data'],dataList[2])
			if transition['code'] == 0:
				return transition

		return responseJSON_1()



	def ExcelW(self):
		pass

if __name__ == '__main__':
	Excel = Excel()
	print(Excel.ExcelR())
