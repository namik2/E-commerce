from django.contrib.auth import get_user_model
from django.core.checks import messages
from django.shortcuts import render
from order.models import Basket, BasketItem, Wishlist
from products.models import Product
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from api.serializers.order_serializers import BasketItemSerializer, BasketSerializer, WishlistSerializer

User = get_user_model()

# Create your views here.



class BasketView(APIView):
    serializer_class = BasketSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user.shoppingcardofUser)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        quantity = request.data.get('quantity')
        product_id = request.data.get('product_id')
        product = Product.objects.filter(pk=product_id).first()
        if product:
            basket_item = BasketItem.objects.get_or_create(product=product,user=request.user)
            basket_item2 = BasketItem.objects.get(product=product,user=request.user)
            basket_item2.quantity += quantity
            basket_item2.save()
            basket, created = Basket.objects.get_or_create(user = request.user)
            basket.items.add(basket_item2)
            arr = []
            for item in basket.items.all():
                serializer = BasketItemSerializer(item)
                arr.append(serializer.data)
            message = {'success': True, 'message' : 'Product added to your card.'}
            return Response(arr, status = status.HTTP_201_CREATED)
        message = {'success' : False, 'message': 'Product not found.'}
        return Response(message, status = status.HTTP_400_BAD_REQUEST)



class BasketItemDeleteAPIView(APIView):
    serializer_class = BasketItemSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        basket_item_id = request.data.get('basket_item_id')
        BasketItem.objects.get(pk=basket_item_id).delete()
        

class WishlistAPIView(APIView):
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user.wishlistofUser)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product_id')
        product = Product.objects.filter(pk=product_id).first()
        if product:
            wishlist, created = Wishlist.objects.get_or_create(user = request.user)
            wishlist2 = Wishlist.objects.filter(user = request.user).first()
            wishlist2.product.add(product)
            message = {'success': True, 'message' : 'Product added to your wishlist.'}
            return Response(message, status = status.HTTP_201_CREATED)
        message = {'success' : False, 'message': 'Product not found.'}
        return Response(message, status = status.HTTP_400_BAD_REQUEST)


    
class WishlistDeleteAPIView(APIView):
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        productId = request.data.get('productId')
        Wishlist.objects.get(pk=productId).delete()


