from django.urls import path
from . import views

urlpatterns = [
    path('account_info/', views.account_info, name='account_info'),
    path('login/', views.login, name='login'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('register/', views.register, name='register'),
] 