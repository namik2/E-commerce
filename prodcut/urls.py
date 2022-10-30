from django.urls import path
from . import views

urlpatterns = [
    path('blog_detail/', views.blog_detail, name='blog_detail'),
    path('blog/', views.blog, name='blog'),
    path('product_detail/', views.product_detail, name='product_detail'),
    path('product_list/', views.product_list, name='product_list'),
    path('quick_view/', views.quick_view, name='quick_view'),
 
]