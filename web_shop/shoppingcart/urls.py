from django.urls import path
from . import views


urlpatterns = [
    path('cart-add/<int:id>/', views.cart_add_item, name='cart_add_item'),
    path('cart-clear/', views.cart_clear, name='cart_clear'),
    path('cart-update-item/<int:id>/', views.cart_update_item, name='cart_update_item'),
    path('cart-clear-item/<int:id>/', views.cart_clear_item, name='cart_clear_item'),
    path('cart-detail/',views.cart_detail,name='cart_detail'),
]
