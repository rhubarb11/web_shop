from django.contrib.auth import views as auth_views
from django.urls import path
from users import views as user_views
from django.conf import settings
from django.contrib.auth.decorators import login_required


urlpatterns = [
     path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),

     path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

     path('register/', user_views.UserRegisterView, name='user-register'),

]
