from django import forms
from .models import Student


class StudentDetailsForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'address', 'email']





