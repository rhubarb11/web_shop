from django.db.models.signals import pre_save
from django.dispatch import receiver
from . models import SubCategory, Product
from django.utils.text import slugify


@receiver(pre_save, sender=Product)
def create_slugfield_product(sender, instance, *args, **kwargs):
    slug = slugify(instance.name)
    instance.slug = slug
    instance.price = round(instance.price, 2)


@receiver(pre_save, sender=SubCategory)
def create_slugfield_subcategory(sender, instance, *args, **kwargs):
    slug = slugify(instance.name)
    instance.slug = slug
