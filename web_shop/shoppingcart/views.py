from django.shortcuts import render, redirect
from shop.models import Product
from cart.cart import Cart
from django.shortcuts import get_object_or_404


def cart_detail(request):
    return render(request, 'shoppingcart/cart_detail.html')
#-------------------------------------------------------------------------------

def cart_add_item(request, id):
    product=get_object_or_404(Product, pk=id)
    cart = Cart(request)
    cart.add(product=product)
    return redirect("shop_index")
#-------------------------------------------------------------------------------

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")
#-------------------------------------------------------------------------------

def cart_clear_item(request, id):
    product=get_object_or_404(Product, pk=id)
    cart = Cart(request)
    cart.remove(product)
    return redirect("cart_detail")
#-------------------------------------------------------------------------------

def cart_update_item(request, id):
    if request.method == 'GET':
        product=get_object_or_404(Product, pk=id)
        cart = Cart(request)
        i = (int(request.GET['updated_quantity'])) - (int(request.GET['current_quantity']))
        if i < 0:
            i = abs(i)
            for x in range(i):
                cart.decrement(product=product)
        elif i > 0:
            for x in range(i):
                cart.add(product=product)

    return redirect("cart_detail")
#-------------------------------------------------------------------------------
