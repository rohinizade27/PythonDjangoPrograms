from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    #address = models.CharField(max_length=1000)
    roll_no = models.IntegerField()
    date_of_birth = models.DateField()
