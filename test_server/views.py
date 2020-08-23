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
from test_server.data import sql
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

# Create your views here.
# def test(request):
#     print(request.method)
#     if request.method == "POST":
#         id = request.POST.get("order_freight_id")
#         try:
#             types = models.query("tms_test","SELECT count(*) FROM tms_wl_freight WHERE order_id = first_order_id"
#                                             " && status != '18' && freight_id = '{}';".format(id))
#         except:
#             return {"code": 0, "msg": "数据库连接失败","data":[]}
#         # types = 1 是司机模式
#         if types == 1:
#             if id[:2] == "DO":
#                 data = models.query("tms_test","SELECT * FROM tms_wl_freight LEFT JOIN tms_wl_order ON"
#                 " tms_wl_freight.order_id = tms_wl_order.order_id WHERE tms_wl_freight.freight_id = '{}'".format(id))
#                 print(data)
#                 return {"code": 1, "msg": "运单"}
#         elif types == 0:
#             pass
#         else:
#             return {"code": 0, "msg": "多条相同单号，请检查数据库"}
#
#     elif request.method == "GET":
#         print("get")
#     return JsonResponse({"status": "BS.200", "msg": "publish article sucess.", "data": request.method})
# error = {"code": 0, "msg": "单号不存在"}














