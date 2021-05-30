# coding=utf-8
import json
import re


def is_json(myjson):
	try:
		json_object = json.loads(myjson)
		# return json.loads(myjson)
		return type(json.loads(myjson))
	except ValueError as e:
		return False



dict_ = str({
    'name':'ahua',
    'age':'<age>',
    'gender':'<gender>'
})

def test_(string):
	index = 0
	list_s = list()
	for i in dict_:
		if i == '<' or i == '>':
			list_s.append(index)
		index += 1
	index = 0
	for i in list_s:
		if index != 0 and i%2:
			print(dict_[list_s[index-1]+1:i])
		index += 1

import re

str = "/api/captcha/captcha"

regular = re.compile(r'[a-zA-Z]+://[^\s]*[.com|.cn]',str)
print(regular)