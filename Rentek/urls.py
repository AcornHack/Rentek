from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^', include("Home.urls")),
	url(r'^', include("user.urls")),
	url(r'^', include("item.urls")),
]
