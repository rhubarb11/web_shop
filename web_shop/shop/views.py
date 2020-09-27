from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from . models import Category, SubCategory, Product


def index(request):
    products = Product.objects.all()
    context = {'products': products }
    return render(request, 'shop/index.html', context)
#-------------------------------------------------------------------------------

class SubCategoryListView(ListView):
    template_name = 'shop/products_sub_category.html'
    context_object_name = 'products'

    def get_queryset(self):
          return Product.objects.filter(subcategory__slug=self.kwargs['slug'])
#-------------------------------------------------------------------------------

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'
