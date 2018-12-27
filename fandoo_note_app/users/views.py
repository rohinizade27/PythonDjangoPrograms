from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UseRegistrationForm,UserUpdateForm,ProfileUpdateForm
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
            return redirect('login')
    else:
        form = UseRegistrationForm()

    return render(request, 'users/register.html', {'form' : form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES, instance=request.user.profile)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request,'users/profile.html', context)
