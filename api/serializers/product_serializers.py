from django.db.models import fields
from order.models import BasketItem
from rest_framework import serializers
from products.models import Product, ProductCategory


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'parent', 'title']
        

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'tag', 'price', 'category', 'cover_image', 'old_price', 'price', 'is_published']








