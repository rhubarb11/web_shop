from django.shortcuts import render, redirect, get_object_or_404
from . forms import OrderShippingDetailForm
from . models import Order
from . forms import OrderShippingDetailForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone


@login_required
def orderShippingDetailsView(request):
    cart_items = request.session['cart']
    if not cart_items:
        return redirect("cart_detail")

    if request.method == 'POST':
        form = OrderShippingDetailForm(request.POST)
        if form.is_valid():
            request.session['address'] = form['address'].value()
            request.session['city'] = form['city'].value()
            request.session['zip_code'] = form['zip_code'].value()
            request.session['country'] = form['country'].value()
            request.session['phone'] = form['phone'].value()
            return redirect('order_summary')
    else:
        form = OrderShippingDetailForm(instance=request.user.userdetails)

    context = {'form': form}
    return render(request, 'order/order_shipping_details.html', context)


@login_required
def orderSummaryView(request):
    cart_items = request.session['cart']
    if not cart_items:
        return redirect("cart_detail")

    return render(request, 'order/order_summary.html')


@login_required
def payView(request):
    if request.method == 'POST':
        order = Order()
        order.user = request.user
        order.date_created = timezone.now()
        order.phone = request.session['phone']
        order.address = request.session['address']
        order.city = request.session['city']
        order.zip_code = request.session['zip_code']
        order.country = request.session['country']
        order.save()
        return redirect("cart_detail")

    else:
        return redirect("cart_detail")
