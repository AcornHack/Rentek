from user import views
from django.conf.urls import url, include

urlpatterns = [
	url(r'^user/$', views.user,name="user"),
	url(r'^signup/$', views.signup,name="signup"),
	]