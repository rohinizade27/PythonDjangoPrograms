from django.urls import path
from . import views
# from users.views import loginview


urlpatterns = [
     path('register', views.register, name='register'),
     path('profile/', views.profile, name='profile'),

     #path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
     #path('login/', views.loginview, name='login'),
     path('login/', views.user_login, name='login'),
     path('home/', views.home, name='home'),
]



