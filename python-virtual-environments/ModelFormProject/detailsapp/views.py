from django.shortcuts import render
from .models import UserDetails
from .forms import UserModelForm


def userDetails(request):
    if request.method == 'POST':
        form = UserModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            users = UserDetails.objects.all()

            return render(request, 'display.html', {'users': users})

    else:
        form_class = UserModelForm

    return render(request, 'userdetails.html',{'form': form_class})

