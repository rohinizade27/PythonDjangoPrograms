from django.http import HttpResponseRedirect, HttpResponse
from .forms import UseRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, resolve_url,render_to_response
from django.contrib import messages
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate, login, REDIRECT_FIELD_NAME
from rest_framework import response
import requests


def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == 'POST':
        form = UseRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created..!!You are now able to login')
            return redirect('login')
    else:
        form = UseRegistrationForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)


def get_jwt_token(user):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    payload = jwt_payload_handler(user)
    print(payload)
    return jwt_encode_handler(payload)

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                jwt_token = get_jwt_token(user)

                # headers= {'Content-Type': 'application/json', 'Authorization': jwt_token}
                url = '/profile/'
                response = redirect(url)
                response['Token'] = jwt_token
                return response


                # r = requests.post(url, data=json.dumps(payload), headers=headers)
                # response = HttpResponseRedirect('/profile/')
                # return response
                # return HttpResponse(jwt_token)

            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'users/login.html', {})







