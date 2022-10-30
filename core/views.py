
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def error(request):
    return render(request, '404error.html')

def faq(request):
    return render(request, 'faq.html')

def about_us(request):
    return render(request, 'about_us.html')

def contact_information(request):
    return render(request, 'contact_information.html')

def address_book(request):
    return render(request, 'address_book.html' )

def contact_us(request):
    return render(request,'contact_us.html')



