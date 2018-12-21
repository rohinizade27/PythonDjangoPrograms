"""
purpose   : To create view for register the user
@Author   : Rohini Zade
@version  : 1.0
@since    : 19-11-2018

"""
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm
def home(request):
    """
    This method is to redirect html request to home.html page
    :param request: get http request as parameter
    :return: redirect to home.html
    """
    return render(request, 'mysite/home.html')


def register(request):
    """
    This method is to register new user
    :param request: get http request as parameter
    :return: redirect to home page
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        # check if user entered data is valid or not
        if form.is_valid():
            user_obj = form.cleaned_data
            username = user_obj['username']
            email = user_obj['email']
            password = user_obj['password']
            # check user entered data is already not exist
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username=username, password=password)
                # if all fields with new entry then login
                login(request, user)
                # redirect to home page
                return HttpResponseRedirect('/')
            else:
                # if user already exits then it throws validation error
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'mysite/register.html', {'form': form})
