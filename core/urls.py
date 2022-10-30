from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('error/', views.error, name='error'),
    path('faq/', views.faq, name='faq'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact_information/', views.contact_information, name='contact_information'),
    path('address_book/', views.address_book, name='address_book'),
    path('contact_us/', views.contact_us, name='contact_us'),
]