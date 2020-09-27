from django.urls import path
from . views import SubCategoryListView, ProductDetailView
from . import views


urlpatterns = [
    path('', views.index, name='shop_index'),
    path('cat/<str:slug>/', SubCategoryListView.as_view(), name='shop_sub_category'),
    path('product/<str:slug>/', ProductDetailView.as_view(), name='shop_product_detail'),



]

from django.conf import settings
if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
