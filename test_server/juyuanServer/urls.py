

from django.conf.urls import url, include
from test_server import views
from test_server.Order import Process

urlpatterns = [
    url(r'^addMoney', views.addMoney),
]