from django.db import models
from PIL import Image
from django_resized import ResizedImageField
from django.utils import timezone


class Category(models.Model):
    name =  models.CharField(max_length=20)

    def __str__(self):
        return self.name
#-------------------------------------------------------------------------------

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name =  models.CharField(max_length=24)
    slug = models.SlugField(max_length=24, unique=True, editable = False)

    def __str__(self):
        return f'{self.name} / {self.category}'
#-------------------------------------------------------------------------------

class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    name =  models.CharField(max_length=40)
    slug = models.SlugField(max_length=40, unique=True, editable = False, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(blank=True, null=True)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    old_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    quantity = models.IntegerField(null=True)
    image = ResizedImageField(default='product_images/default.jpeg',size=[640, 480], quality=90,
                              upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return f'{self.name} / {self.subcategory}'
