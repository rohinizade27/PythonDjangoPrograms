"""
purpose   : To create form with fields username,email and password

@Author   : Rohini Zade
@version  : 1.0
@since    : 19-11-2018

"""
from django import forms


class UserRegistrationForm(forms.Form):
    # Create username field of char type
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    # Create email field of char type
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    # Create email field of char type
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )