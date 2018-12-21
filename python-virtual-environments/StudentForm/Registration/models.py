from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User



class Student(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(max_length=2000,)
    email = models.EmailField(max_length=254)

    author= models.ForeignKey(User,default=None)





