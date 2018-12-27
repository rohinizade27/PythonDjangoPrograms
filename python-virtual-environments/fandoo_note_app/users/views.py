from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UseRegistrationForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == 'POST':
        form = UseRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created..!!You are now able to login')
            return redirect('users-login')
    else:
        form = UseRegistrationForm()

    return render(request, 'users/register.html', {'form' : form})

@login_required
def profile(request):
    return render(register,'users/profile.html')
