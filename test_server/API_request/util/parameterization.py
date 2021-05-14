
# coding=utf-8
from test_server.API_request.table_s.variable import get_variable
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


if __name__ == '__main__':
    dict_ = {
        'name':'ahua',
        'age':'{age}',
        'gender':'{gender}'
    }
    print(parameterization(json.dumps(dict_)))

