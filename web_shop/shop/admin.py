from django.contrib import admin
from . models import Product, Category, SubCategory

class CategoryAdmin(admin.ModelAdmin):
        search_fields = ['name']


class SubCategoryAdmin(admin.ModelAdmin):
        search_fields = ['name']


class ProductAdmin(admin.ModelAdmin):
        search_fields = ['name', 'subcategory__name']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
