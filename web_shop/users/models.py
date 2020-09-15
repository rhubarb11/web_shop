from django.db import models
from django.contrib.auth.models import User


User._meta.get_field('email')._unique = True
User._meta.get_field('email').blank = False
User._meta.get_field('first_name').blank = False
User._meta.get_field('last_name').blank = False


class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, blank=True)
    address =  models.CharField(max_length=30, blank=True)
    city =  models.CharField(max_length=30, blank=True)
    zip_code =  models.CharField(max_length=5, blank=True)
    country =  models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.user.username;
