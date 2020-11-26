from django.db.models.signals import post_save, pre_save
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


@receiver(pre_save, sender=User)
def username_equals_email(sender, instance, *args, **kwargs):
    instance.username = instance.email
    
