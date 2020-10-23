from django.shortcuts import render, redirect, get_object_or_404
from . forms import OrderShippingDetailForm
from . models import Order
from . forms import OrderShippingDetailForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def orderShippingDetailsView(request):

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
    """form = OrderShippingDetailForm(request.POST)
    context = {'form': form}"""
    return render(request, 'order/order_summary.html')


@login_required
def payView(request):
    """form = OrderShippingDetailForm(request.POST)
    context = {'form': form}"""
    return render(request, 'order/order_summary.html')
