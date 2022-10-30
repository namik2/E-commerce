from django.shortcuts import render

# Create your views here.


def blog_detail(request):
    return render(request, 'blog_detail.html')

def blog(request):
    return render(request, 'blog.html')

def product_detail(request):
    return render(request, 'product-detail.html')

def product_list(request):
    return render(request, 'product-list.html')

def quick_view(request):
    return render(request, 'quick_view.html')