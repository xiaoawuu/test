from django.conf.urls import url, include
from jy_server import views

urlpatterns = [
	url(r'^addMoney', views.Member),
	url(r'^Logout', views.Logout),
]
