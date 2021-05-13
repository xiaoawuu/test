import xlrd,json
from test_server.API_request.table_s.port_parameter import add
from test_server.API_request.table_s.variable import set_variable,get_variable
from test_server.API_request.util.request_fun import fron_data, test_port_from_data
from test_server.utils.responseJSON import *


def Excel_r():
	try:
		data = xlrd.open_workbook(r'C:\Users\admin\Desktop\测试.xls')  # 打开xls文件
		table1 = data.sheets()[0]  # 打开第一张表
		table2 = data.sheets()[1]  # 打开第一张表
		nrows2 = table2.nrows  # 获取表的行数
		config = dict()
		for i in range(nrows2):  # 循环逐行打
			if i == 0:  # 跳过第一行
				continue
			config[table2.row_values(i)[:2][0]] = table2.row_values(i)[:2][1]
		print('配置数据',config)
		nrows = table1.nrows  # 获取表的行数
		for i in range(nrows):  # 循环逐行打
			if i == 0:  # 跳过第一行
				continue
			data_list = table1.row_values(i)[:4]  # 取前四列
			print(data_list)
			responses = test_port_from_data(config['url']+data_list[0],json.loads(data_list[3]))
			if responses['code'] == 1:
				w = set_variable(data_list[0],json.loads(data_list[3]))
				print(w)
			else:
				print(False)

	except xlrd.biffh.XLRDError:
		return responseJSON_0(msg='接口只支持.xls文件！')


if __name__ == '__main__':
	Excel_r()
