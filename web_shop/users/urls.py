from django.contrib.auth import views as auth_views
from django.urls import path
from users import views as user_views
from django.conf import settings
from django.contrib.auth.decorators import login_required


urlpatterns = [

     # Built in authentication views
     path('login/', auth_views.LoginView.as_view(
          template_name='users/login.html', redirect_authenticated_user=True), name='login'),

     path('logout/', auth_views.LogoutView.as_view(
          template_name='users/logout.html'), name='logout'),

     path('password-change/', auth_views.PasswordChangeView.as_view(
          template_name='users/password_change.html'), name='password_change'),

     path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(
          template_name='users/password_change_done.html'), name='password_change_done'),

     path('password-reset/', auth_views.PasswordResetView.as_view(
          template_name='users/password_reset.html'), name='password_reset'),

     path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
          template_name='users/password_reset_done.html'),name='password_reset_done'),

     path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
          template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),

     path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
          template_name='users/password_reset_complete.html'), name='password_reset_complete'),
     #--------------------------------------------------------------------------------------------

     path('register/', user_views.userRegisterView, name='register'),

     path('account/', user_views.userInfoView, name='user'),

     path('email-change/', user_views.emailChangeView, name='email_change'),

     path('details-change/', user_views.detailsChangeView, name='details_change'),








]
