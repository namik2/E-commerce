from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic.base import TemplateView
from accounts.views import AccountView, CustomLoginView, CustomLogoutView, CustomPasswordResetCompleteView, CustomPasswordResetConfirmView, CustomPasswordResetView, AddressBook, CustomResetEmailConfirmView, account_register, activate

app_name = "accounts"

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', account_register, name='register'),
    path('confirmation/<str:uidb64>/<str:token>/',
         activate, name='confirmation'),

    # Password reset
    path('password_reset/', CustomPasswordResetView.as_view(), name='pwdreset'),
    path('password_reset_confirm/<uidb64>/<token>',
         CustomPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password_reset/password_reset_email_confirm/',
         CustomResetEmailConfirmView.as_view(), name="password_reset_done"),
    path('password_reset_confirm/password_reset_complete/',
         CustomPasswordResetCompleteView.as_view(), name="password_reset_complete"),

    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('account/', AccountView.as_view(), name='account'),
    path('address-book/', AddressBook, name='address-book')
]
