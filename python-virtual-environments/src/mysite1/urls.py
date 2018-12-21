
from django.conf.urls import url
from .views import home, register

urlpatterns = [

    # url redirect home method of view
    url(r'^$', home),
    # url redirect to register method of view
    url(r'^register/', register),
]
