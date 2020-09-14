 # coding=utf-8
'''
python——json操作

'''
import json

# dumps 和 loads

jsonData = {'name': '阿华', 'age': 18, 'gender': '男'}
# 将dict转为str
#  ensure_ascii=False ——>不使用ascii编码
a = json.dumps(jsonData, ensure_ascii=False)
print(type(a))
print(a)
# 将str转为dict
b = json.loads(a)
print(b)
print(type(b))

# dump 和 load

data = {
    'name':'ming',
    'a':[1,2,3,4],
    'b':(1,2,3)
}


with open('json_test.txt','w') as f:
    json.dump(data,f)






