from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
 path('userdetails/', views.userDetails),
 path('display/', views.userDetails),

path('', admin.site.urls),
]