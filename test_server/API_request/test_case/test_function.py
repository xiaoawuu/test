def test_captcha(response_data):
	print('test:', response_data)


def test_wllogin(response_data):
	print('test:', response_data)


class TestFunction(object):
	def __init__(self, test_value_1):
		self.test_value_1 = test_value_1

	def equal(self, test_values_2):  # 同等于
		return 1 if self.test_value_1 == test_values_2 else 0

	def unequal(self, test_values_2):  # 不等于
		return 1 if self.test_value_1 != test_values_2 else 0

	def inside(self, test_values_2):  # 包含
		return 1 if test_values_2 in self.test_value_1 else 0

	def not_in(self, test_values_2):  # 不包含
		return 1 if test_values_2 not in self.test_value_1 else 0


if __name__ == '__main__':
	Test = TestFunction('')
	print(Test.equal('123456'))
	print(Test.unequal('123456'))
	print(Test.inside('12345'))
	print(Test.not_in('123457'))
