from os import name
from django.db import router
from django.urls import path
from django.urls.conf import include
from api.views.core_views import SubscribeAPIView
from api.views.order_views import BasketItemDeleteAPIView, BasketView, WishlistAPIView, WishlistDeleteAPIView
from api.views.product_views import ProductAPIView, ProductCategoryAPIView


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path ('basket/', BasketView.as_view(), name='basket'),
    path ('wishlist/', WishlistAPIView.as_view(), name='wishlist'),
    path ('wishlist/delete', WishlistDeleteAPIView.as_view(), name='wishlist_delete'),
    path ('subscribe/', SubscribeAPIView.as_view(), name='subscribe'),
    path ('productcategory/', ProductCategoryAPIView.as_view(), name='product-category'),
    path ('product/' , ProductAPIView.as_view(), name='product'),
    path ('basket-item/delete/', BasketItemDeleteAPIView.as_view(), name='basket-item-delete'),
]