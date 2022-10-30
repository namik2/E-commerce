from django.urls import path
from . import views

urlpatterns = [
    path('checkout_billing_info/', views.checkout_billing_info, name='checkout_billing_info'),
    path('checkout/', views.checkout, name='checkout'),
    path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
    path('wishlist/', views.wishlist, name='wishlist'),
]