from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_out
from django.contrib.auth.models import User
from django.dispatch import receiver
from . models import UserDetails
from django.contrib import messages


@receiver(post_save, sender=User)
def create_userdetails(sender, instance, created, **kwargs):
    if created:
        UserDetails.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_userdetails(sender, instance, **kwargs):
    instance.userdetails.save()


@receiver(user_logged_out)
def on_user_logged_out(sender, request, user, **kwargs):
    messages.success(request, 'You have logged out')
