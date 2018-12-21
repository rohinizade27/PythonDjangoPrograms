"""
purpose   : To create urls for login app
@Author   : Rohini Zade
@version  : 1.0
@since    : 19-11-2018

"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.contrib.auth import views as auth_views


urlpatterns = [
    # this will redirect to default admin page
    path('admin/', admin.site.urls),
    # redirect to auth_view/login
    url(r'^login/$', auth_views.login),
    # redirect to auth_view/logout
    url(r'^logout/$', auth_views.logout),
    # navigate to mysite1/urls file
    url(r'^', include('mysite1.urls')),
]



