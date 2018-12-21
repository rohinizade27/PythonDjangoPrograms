from .forms import StudentDetailsForm
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from . import forms
from . models import Student


def home(request):
    if request.method == 'POST':
        form = forms.StudentDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return HttpResponseRedirect('/thanks/')

    form = forms.StudentDetailsForm()
    context = {'form': form}
    return render(request, 'Registration/home.html/', context)





