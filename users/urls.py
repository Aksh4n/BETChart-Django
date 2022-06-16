from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login_user', views.login_user , name="login"),
    path('logout_user', views.logout_user , name="logout" ),
    path('register_user', views.register_user , name="register_user" ),
    path('profile', views.profile , name="profile"),
    path('walletaddress', views.walletaddress , name="walletaddress"),



    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = "registration/reset_password.html"), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "registration/password_reset_sent.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = "registration/reset_form.html"), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "registration/finished.html"), name ='password_reset_complete'),



]
