"""test_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from test_server import views
from test_server.Order import Process

urlpatterns = [
	url(r'^juyuanServer/', include('jy_server.urls')),
	url(r'^addMoney', views.addMoney),
	url(r'^weixin_main', views.weixin_main),
	url(r'^addMembers', views.addMembers),
	url(r'^removeUser', views.removeUser),
	url(r'^testPortInsert', views.testPortInsert),
	url(r'^$', views.addMoneys),
	url(r'^addOrder', Process.Process().orderProcess),
	url(r'^test_fun', views.test_fun),
]
