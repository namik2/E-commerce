from django.db.models import fields
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.generic import CreateView, FormView
from blog.models import Blog
from products.models import Product, ProductCategory
from .models import Contact
from core.forms import ContactForm, SubScriberForm

# Create your views here.
   
   
class HomePageView(TemplateView):
    template_name = 'index.html'
    http_method_names = ['post', 'get']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_posts'] = Blog.objects.filter(is_published=True).order_by('-id')[:2]
        context['products'] = Product.objects.filter(is_published=True).order_by('id')[:9]
        context['popular_products'] = Product.objects.order_by('-view_count')[:4]
        context['new_products'] = Product.objects.order_by('-id')[:4]
        context['categories'] = ProductCategory.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data(**kwargs) )


def AboutUs(request):
    return render(request, "about_us.html")


class ContactView(View):
    template_name = 'contact_us.html'
    http_method_names = ['post', 'get']

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('contact'))
        return render(request, self.template_name, {'form': form})




def Error404(request):
    return render(request, '404error.html')

def FAQ(request):
    return render(request, 'faq.html')