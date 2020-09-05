from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from bin.test_port.select_port import models
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
import json
import sys,corsheaders
sys.path.append(r'C:\test_server\bin')

from django.shortcuts import render, HttpResponse
import json
from test_server.data import sql,mysqls
from  test_server.utils import is_int

def addMoneys(request):
    return render(request,'config.html')

def addMoney(request):
    if request.method == "POST":
        mobile = json.loads(request.body.decode().replace("'", "\"")).get('mobile')
        money = json.loads(request.body.decode().replace("'", "\"")).get('money')
        if money == "" or mobile == "":
            return HttpResponse(json.dumps({"code": 0, "msg": "金额或金额类型异常", "data": ""}))
        if type(money)!=int:
            money = int(money)
        if is_int.is_number(money) or type(money)!=int:
            return HttpResponse(json.dumps({"code": 0, "msg": "金额或金额类型异常", "data": ""}))
        if money > 4000 or money <1:
            return HttpResponse(json.dumps({"code":0,"msg":"金额充值范围1~4000币","data":""}))
        is_mobile = sql.sql_select("SELECT status FROM biz_user WHERE mobile = '{}';".format(mobile))
        if is_mobile == []:
            return HttpResponse(json.dumps({"code":0,"msg":"用户不存在！","data":""}))
        if is_mobile[0][0] != 4:
            return HttpResponse(json.dumps({"code": 0, "msg": "用户还未完成认证！", "data": ""}))
        sql.sql_exec("exec GiveMeTheMoney '{}',{};".format(mobile,str(money)))
        remaining=sql.sql_select("SELECT currency FROM biz_wallet WHERE user_id=(SELECT id FROM biz_user WHERE mobile ='{}');".format(mobile))
        print("充值手机",mobile)
        return HttpResponse(json.dumps({"code":1,"msg":"充值成功！","data":"当前账户余额:{}".format(remaining[0][0])}))
    else:
        return HttpResponse(json.dumps({"code":0,"msg":"请使用POST请求！","data":""}))

def removeUser(request):
    if request.method == "POST":
        print(request.body)
        mobile = json.loads(request.body.decode().replace("'", "\"")).get('mobile')
        is_mobile = sql.sql_select("SELECT status FROM biz_user WHERE mobile = '{}';".format(mobile))
        if is_mobile == []:
            return HttpResponse(json.dumps({"code":0,"msg":"要删除的用户不存在！","data":""}))
        re = sql.sql_exec("exec RemoveUserByMobile '{}';".format(mobile))
        print("删除手机", mobile)
        return HttpResponse(json.dumps({"code":1,"msg":"删除成功！","data":"{}".format(re)}))
    else:
        return HttpResponse(json.dumps({"code":0,"msg":"请使用POST请求！","data":""}))

import time
def testPortInsert(request):
    if request.method == "POST":
        try:
            mobile = json.loads(request.body.decode().replace("'", "\"")).get('mobile')
            money = json.loads(request.body.decode().replace("'", "\"")).get('money')
            print('mobile:', mobile)
            print('money:', money)
            sql = "INSERT INTO freight_id_payment (freight_id,id_s,`status`) VALUES ('DO-20200585685','{}',1)".format(time.time())
            mysqls.Data().query('localhost',sql)
            return HttpResponse(json.dumps({"code": 1, "msg": "请求成功！", "data": ""}))
        except Exception as err:
            return HttpResponse(json.dumps({"code":0,"msg":"请求失败！","data":"{}".format(err)}))
    else:
        return HttpResponse(json.dumps({"code": 0, "msg": "请使用POST请求！", "data": ""}))

def testPortSelect(request):
    if request.method == "POST":
        try:
            mobile = json.loads(request.body.decode().replace("'", "\"")).get('mobile')
            money = json.loads(request.body.decode().replace("'", "\"")).get('money')
            print('mobile:',mobile)
            print('money:',money)
            sql = "INSERT INTO freight_id_payment (freight_id,id_s,`status`) VALUES ('DO-20200585685','{}',1)".format(
                time.time())
            mysqls.Data().query('localhost', sql)
            return HttpResponse(json.dumps({"code": 1, "msg": "请求成功！", "data": ""}))
        except Exception as err:
            return HttpResponse(json.dumps({"code": 0, "msg": "请求失败！", "data": "{}".format(err)}))
    else:
        return HttpResponse(json.dumps({"code": 0, "msg": "请使用POST请求！", "data": ""}))
def testPort():
    pass

# testPortInsert()