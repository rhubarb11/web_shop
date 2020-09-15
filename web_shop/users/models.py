from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, blank=True)
    address =  models.CharField(max_length=30, blank=True)
    city =  models.CharField(max_length=30, blank=True)
    zip_code =  models.CharField(max_length=5, blank=True)
    country =  models.CharField(max_length=30, blank=True)
