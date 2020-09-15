from django.db import models


class Category(models.Model):
    name =  models.CharField(max_length=20)

    def __str__(self):
        return self.name



class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name =  models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} / {self.category}'



class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    name =  models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return f'{self.name} / {self.subcategory}'
