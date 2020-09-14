from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True)
    phone = models.CharField(max_length=12)
    address =  models.CharField(max_length=30)
    city =  models.CharField(max_length=30)
    zip_code =  models.CharField(max_length=5)
    country =  models.CharField(max_length=30)
