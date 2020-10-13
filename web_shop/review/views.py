from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, UpdateView
from shop.models import Product
from . models import CustomerReview
from . forms import CustomerReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib import messages
from django.utils import timezone


@login_required
def addReviewView(request, slug):
    if request.method == 'POST':
        product = get_object_or_404(Product, slug=slug)
        customer_review = product.reviews.all().filter(user=request.user)
        form = CustomerReviewForm(request.POST)

        if customer_review:
            messages.error(request, 'You have already rated this product')

        elif form.is_valid():
             instance = form.save(commit=False)
             instance.user = request.user
             instance.product = product
             instance.save()
             messages.success(request, 'Thanks for your opinion')

    else:
        form = CustomerReviewForm()

    context = {'form': form}
    return redirect('shop_product_detail', slug=slug)
#-------------------------------------------------------------------------------

class UpdateReviewView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = CustomerReview
    form_class = CustomerReviewForm

    def form_valid(self, form):
        form.instance.date_updated = timezone.now()
        messages.success(self.request, 'Review successfully updated')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Something went åt helskotta')
        slug = self.get_object().product.slug
        return redirect('shop_product_detail', slug=slug)

    def test_func(self):
        customer_review = self.get_object()
        if self.request.user == customer_review.user:
            return True
        else:
            return False

    def get_success_url(self):
        slug = self.get_object().product.slug
        return reverse_lazy('shop_product_detail', kwargs={'slug':slug})





#-------------------------------------------------------------------------------
