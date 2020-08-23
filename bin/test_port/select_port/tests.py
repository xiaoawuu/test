from django.test import TestCase
from django.http import HttpResponse, JsonResponse
# Create your tests here.
# 连接database
import pymysql
import pymysql.cursors
import configparser
from bin.test_port.select_port import models
# def test(a):
#     print(request.method)
#     if request.method == "POST":
#         # id = request.POST.get("order_freight_id")
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

import sys
sys.path.append(r'C:\test_server\bin\test_port')