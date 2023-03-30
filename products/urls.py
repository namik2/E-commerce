from django.urls import path
from products.views import Productdetailview, Productlistview

urlpatterns = [
    path ('product_detail/<int:pk>/', Productdetailview.as_view(), name='product_detail'),
    path ('product_list/', Productlistview.as_view(), name='product_list'),
]