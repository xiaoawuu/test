"""test_port URL Configuration

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
from select_port import views

urlpatterns = [
    url(r'^select/', views.test),
    url(r'^admin/', admin.site.urls),
    # url(r'^docs/', views.get_schema_view()),
    # url(r'^api/getjson', views.ReturnJson.as_view()),
    # url(r'^test/', include("requestTest.urls")),
    # url(r'^app02/', include("app02.urls")),
    # url(r'^monitor/', views.index,name="indexs"),
]
