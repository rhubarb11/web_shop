from django.db import models
from shop.models import Product
from django.contrib.auth.models import User
from django.utils import timezone



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField()
    processed = models.BooleanField(default=False)
    shipped = models.BooleanField(default=False)
    phone = models.CharField(max_length=14)
    address =  models.CharField(max_length=30)
    city =  models.CharField(max_length=30)
    zip_code =  models.CharField(max_length=5)
    country =  models.CharField(max_length=30)

    def __str__(self):
        return f'#OrderNr {self.pk}'


class OrderDetails(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return f'detail - {order.self}'
