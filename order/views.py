from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse, reverse_lazy
from django.views.generic.base import View
from django.views.generic.edit import CreateView, DeleteView, FormView
from django.views.generic.list import ListView
from django.contrib import messages
from order.forms import BillingAddressForm, ShippingAddressForm
from order.models import Basket, BillingAddress, Order, ShippingAddress, Wishlist

from order.models import BasketItem

# Create your views here.

class CheckoutShipping(View):
    template_name = 'checkout.html'
    http_method_names = ['get', 'post']


    def get(self, request):
        form = ShippingAddressForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = ShippingAddressForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/checkout-billing')
        else:
            return render(request, 'checkout.html', {'form': form})
    


class CheckoutBill(View):
    template_name = 'checkout_billing_info.html'
    http_method_names = ['get', 'post']


    def get(self, request):
        form = BillingAddressForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = BillingAddressForm(request.POST)
        if form.is_valid():
            form.save()
            order = Order.objects.create(
                user=request.user,
                basket =   Basket.objects.get(user=request.user),
                shipping_address = ShippingAddress.objects.get(user=request.user),
                ordered = False
            )
            order.save()
            return HttpResponseRedirect('/checkout-confirm')
        else:
            return render(request, 'checkout_bill.html', {'form': form})


class CheckoutConfirm(View):
    template_name = 'checkout_confirm.html'
    http_method_names = ['get', 'post']

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


def QuickView(request):
    return render(request, 'quick_view.html')

class WishlistView(ListView):
    model = Wishlist
    template_name = 'wishlist.html'
    quesyset =  Wishlist.objects.all()
    context_object_name = 'wishlist'

class CartView(ListView):
    template_name = 'shopping_cart.html'
    queryset = BasketItem.objects.all()
    context_object_name = 'items'


