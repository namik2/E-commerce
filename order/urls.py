from django.urls import path
from order.views import CartView, CheckoutBill, CheckoutConfirm, CheckoutShipping, QuickView, WishlistView

app_name = 'order'

urlpatterns = [
    path ('checkout/', CheckoutShipping.as_view(), name='checkout'),
    path ('checkout-billing/', CheckoutBill.as_view(), name='checkout-billing'),
    path('checkout-confirm', CheckoutConfirm.as_view(), name='checkout-confirm'),
    path ('quickview/', QuickView),
    path ('shopping-cart/', CartView.as_view(), name='shopping-cart'),
    path ('wishlist/', WishlistView.as_view(), name='wishlist'),
]