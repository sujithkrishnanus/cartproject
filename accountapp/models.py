from django.db import models

# Create your models here.

class user(models.Model):

    username=models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    password1 = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.username)