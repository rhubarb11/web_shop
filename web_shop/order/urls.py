from django.urls import path
from . import views


urlpatterns = [
    path('shipping-details/', views.orderShippingDetailsView, name='order_shipping_details'),
    path('shipping-summary/', views.orderSummaryView, name='order_summary'),
    path('shipping-pay/', views.payView, name='order_pay'),
]
