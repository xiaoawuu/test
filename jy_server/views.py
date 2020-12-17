import sys, corsheaders

from jy_server.Modules.DeleteUser import Logout_user
from jy_server.Modules.addMoney import addMoney

sys.path.append(r'C:\test_server\bin')

from django.shortcuts import HttpResponse
import json

from test_server.utils.responseJSON import responseJSON_1, responseJSON_0


def Member(request):
	if request.method == "POST":
		mobile = json.loads(request.body.decode().replace("'", "\"")).get('mobile')
		money = json.loads(request.body.decode().replace("'", "\"")).get('money')
		return HttpResponse(json.dumps(addMoney(mobile, money)))
	else:
		return HttpResponse(json.dumps(responseJSON_0('请使用POST请求！')))


def Logout(request):
	if request.method == "POST":
		mobile = json.loads(request.body.decode().replace("'", "\"")).get('mobile')
		return HttpResponse(json.dumps(Logout_user(mobile)))
	else:
		return HttpResponse(json.dumps(responseJSON_0('请使用POST请求！')))