import base64


class Base64():
	def __init__(self):
		pass

	def base64Encode(self, str):
		'''
		编码
		:return:编码后的结果
		'''
		try:
			# 想将字符串转编码成base64,要先将字符串转换成二进制数据
			bytes_url = str.encode("utf-8")
			# 被编码的参数必须是二进制数据
			return base64.b64encode(bytes_url).decode()
		except:
			return '编码失败'

	def base64Decode(self, base_64):
		'''
		解码
		:return: 解码后的结果
		'''
		try:
			return base64.b64decode(base_64).decode("utf-8")
		except:
			return "请输入正确的BASE64"

# b = Base64()
# print(b.base64Encode('18007530115'))
# print(b.base64Decode('MTgwMDc1MzAsxMTU='))
