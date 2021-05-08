import json


def is_json(myjson):
	try:
		json_object = json.loads(myjson)
		# return json.loads(myjson)
		return type(json.loads(myjson))
	except ValueError as e:
		return False


print(is_json("{}"))  # prints True
print(is_json("{asdf}"))  # prints False
print(is_json('{ "age":100}'))  # prints True
print(is_json("{'age':100 }"))  # prints False
print(is_json("{\"age\":100 }"))  # prints True
print(is_json('{"age":100 }'))  # prints True
print(is_json('{"foo":[5,6.8],"foo":"bar"}'))  # prints True
print(is_json('{"foo":[5,6.8],"foo":{"name":"ahua"}}'))  # prints True

