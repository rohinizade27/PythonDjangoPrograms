from django.db import models
class UserDetails(models.Model):

    name = models.CharField(max_length=100)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    def __str__(self):
        return self.name

