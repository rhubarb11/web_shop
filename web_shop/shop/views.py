from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from . models import Category, SubCategory, Product
from review.models import CustomerReview
from review.forms import CustomerReviewForm
from django.db.models import Avg

from django_seed import Seed
import random
import lorem
from lorem.text import TextLorem

from django.contrib.auth.models import User





def index(request):
    # seeder = Seed.seeder()
    #
    # lorems = TextLorem(srange=(1,1))
    # seeder.add_entity(User, 10, {
    # 'email': lambda x: seeder.faker.email(),
    # 'is_staff': False,
    # 'is_superuser': False,
    # 'first_name': seeder.faker.first_name(),
    # 'last_name': seeder.faker.last_name(),
    # })
    #
    #
    # #lorems = TextLorem(srange=(1,1))
    # seeder.add_entity(Category, 8, {
    # #'name': lambda x: lorems.sentence().replace(".", '')
    # 'name': lambda x: seeder.faker.word(),
    #
    # })
    #
    # lorems = TextLorem(srange=(1,2))
    # seeder.add_entity(SubCategory, 24, {
    # #'name': lambda x: seeder.faker.name(),
    # })
    #
    # lorems = TextLorem(srange=(1,3))
    # lorem2 = TextLorem(srange=(14,22))
    # seeder.add_entity(Product, 100, {
    #
    # 'description': lambda x: lorem2.text(),
    # 'quantity': lambda x: random.randint(0, 1000),
    # 'price': lambda x:  round(random.uniform(0.9, 4999.9), 1),
    # 'image' : "product_images/default.jpeg",
    #
    # })
    #
    # lorems = TextLorem(srange=(1,2))
    # lorem2 = TextLorem(srange=(3,20))
    # seeder.add_entity(CustomerReview, 200, {
    # 'rating': lambda x: random.randint(1, 5),
    # 'comment': lambda x: lorem2.text(),
    # 'author': lambda x: seeder.faker.first_name()
    #
    # })
    # seeder.execute()

    products = Product.objects.all()
    context = {'products': products }
    return render(request, 'shop/index.html', context)
#-------------------------------------------------------------------------------

def ProductSlugView(request, pk):
    product = product = get_object_or_404(Product, pk=pk)
    return redirect("shop_product_detail", slug = product.slug)

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            try:
                customer_review = context['product'].reviews.all().get(user=self.request.user)
                context['form'] = CustomerReviewForm(instance=customer_review)
                context['reviewed'] = True
                context['review_id'] = customer_review.id

            except CustomerReview.DoesNotExist:
                context['form'] = CustomerReviewForm()
                context['reviewed'] = False

        context['avg_rating'] = context['product'].reviews.all().aggregate(Avg('rating'))
        return context
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
