
def get_cart_total_amount(request):
    total_amount = 0;
    cart = request.session.get('cart')

    if cart:
        for value in cart.values():
            total_amount += float(value.get('price'))*float(value.get('quantity'))

    context = {'cart_total_amount': total_amount}
    return context
