from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('shop.urls')),
    path('user/', include('users.urls')),
    path('cart/', include('shoppingcart.urls')),
    path('review/', include('review.urls')),
    path('order/', include('order.urls')),
    path('admin/', admin.site.urls),
]
