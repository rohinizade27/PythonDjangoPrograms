from django.shortcuts import render
from .models import Student
from django.http import HttpResponse


def studentview(request):
    student_list = Student.objects.all()
    context = {'student_list': student_list}
    return render(request,'student/studentview.html', context)


