from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
from users import views as users_view
from django.conf import settings


urlpatterns = [
     path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
     path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    
]
