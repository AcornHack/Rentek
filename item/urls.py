from item import views
from django.conf.urls import url, include

urlpatterns = [
	url(r'^item/(?P<pk>\d+)$', views.item,name="item"),
	]