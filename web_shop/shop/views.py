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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subcategory = SubCategory.objects.get(slug=self.kwargs['slug'])
        context['sub_category'] = subcategory.name
        return context

    def get_queryset(self):
        sort_by = self.request.GET.get('sort')
        if sort_by:
            return Product.objects.filter(subcategory__slug=self.kwargs['slug']).order_by(sort_by)
        else:
            return Product.objects.filter(subcategory__slug=self.kwargs['slug'])
#-------------------------------------------------------------------------------

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'
#-------------------------------------------------------------------------------

class SearchListView(ListView):
    template_name = 'shop/search.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search')
        context['sort_order'] = self.request.GET.get('sort')
        return context

    def get_queryset(self):
        search_query = self.request.GET.get('search')
        sort_by = self.request.GET.get('sort')
        if search_query:
            return Product.objects.filter(name__icontains=search_query).order_by(sort_by)
        else:
            return Product.objects.all().order_by(sort_by)
