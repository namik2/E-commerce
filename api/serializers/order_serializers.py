from django.db.models import fields
from api.serializers.product_serializers import ProductSerializer
from order.models import Wishlist
from rest_framework import serializers
from order.models import Basket, BasketItem

class BasketSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Basket
        fields = ['user', 'items']


class BasketItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = BasketItem
        fields = ['user', 'product', 'quantity']


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ['user', 'product']