from django.urls import reverse
from django.db import models
from shop.models import Product
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class CustomerReview(models.Model):
    product = models.ForeignKey(Product, related_name="reviews", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author =  models.CharField(max_length=16)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(max_length=400)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'review - {self.product} - {self.user}'
