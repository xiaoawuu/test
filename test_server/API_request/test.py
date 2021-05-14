import json



def is_json(myjson):
	try:
		json_object = json.loads(myjson)
		# return json.loads(myjson)
		return type(json.loads(myjson))
	except ValueError as e:
		return False

import re
a = 'hello word'

print(a.replace('word', 'python'))

strinfo = re.compile('word')
b = strinfo.sub('python',a)
print(b)




