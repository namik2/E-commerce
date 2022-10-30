from django.shortcuts import render


# Create your views here.

def account_info(request):
    return render(request, 'account_information.html')

def forgot_password(request):
    return render(request, 'forgot_password.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')