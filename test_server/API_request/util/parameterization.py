
# coding=utf-8
from test_server.API_request.table_s.variable import get_variable
from test_server.API_request.util.print_ import *
from test_server.API_request.util.responseJSON import *
import json

def parameterization(data):
    """
    接受json字符串进行参数化
    :param data:
    :return:
    """
    if type(data) != str:
        return responseJSON_0(msg='请求参数错误',data='fun> parameterization')
    try:

        data = json.loads(data)
        for i in data.keys():
            if data[i][0] == '{' and data[i][-1] == '}':
                variable = get_variable('/api/captcha/captcha',i)
                if variable['code'] == 0:
                    return responseJSON_0(msg='缺少变量：{}'.format(i))
                data[i] = variable['data']
        return data
    except json.decoder.JSONDecodeError as ERR:
        return responseJSON_0(msg='参数转换json错误!',data=ERR)



def parameterization_str(data,part='global'):
    """
    接收json字符串进行参数化
    :param data:json字符串
    :param part:变量名
    :return:json
    """
    try:
        if type(data) != dict:
            return responseJSON_0(msg='parameterization_str,参数非JSON格式!')
        data = json.dumps(data)
        if '<' not in data:
            return responseJSON_1(data=json.loads(data))
        index = 0
        list_s = list()
        for i in data:
            if i == '<' or i == '>':
                list_s.append(index)
            index += 1
        index = 0
        dicts = dict()
        for i in list_s:
            if index%2:

                variable_name = data[list_s[index - 1]+1:i]
                variable = get_variable(part,variable_name)
                if variable['code'] == 0:
                    return variable
                dicts[variable_name] = variable['data']
            index += 1
        for i in dicts:
            data = data.replace('<{}>'.format(i),dicts[i])
        return responseJSON_1(data=json.loads(data))
    except Exception as ERR:
        return responseJSON_0(msg='parameterization_str fun error!',data=ERR)



if __name__ == '__main__':
    dict_ = {'username': 'XLM0042', 'pwd': '123456', 'cToken': '<cToken>', 'captcha': {'captcha':'<captcha>'}, 'isLongLogin': '0'}
    print(parameterization_str(dict_))



















