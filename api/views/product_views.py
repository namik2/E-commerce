from django.http.response import JsonResponse
from api.serializers.product_serializers import ProductCategorySerializer, ProductSerializer
from products.models import Product, ProductCategory
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status


class ProductCategoryAPIView(APIView):
    serializer_class = ProductCategorySerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        serializer = ProductCategorySerializer(
            ProductCategory.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = ProductCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        arr = []
        for item in Product.objects.all():
            serializer = ProductSerializer(item)
            arr.append(serializer.data)
        return Response(arr, status=status.HTTP_200_OK)    
            

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

