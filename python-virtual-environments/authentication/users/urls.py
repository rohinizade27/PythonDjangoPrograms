from .views import RegistrationAPIView,LoginAPIView,UserRetrieveUpdateAPIView
from django.urls import path

urlpatterns = [
    path('user/',UserRetrieveUpdateAPIView.as_view()),
    path('users/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
]