from Home import views
from django.conf.urls import url, include

urlpatterns = [
	url(r'^$', views.home,name="home"),
	url(r'^register/$', views.register,name="register"),
	]
