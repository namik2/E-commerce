from django.contrib import admin
from .models import Basket, BasketItem, BillingAddress, Wishlist, ShippingAddress, Order

# Register your models here.

admin.site.register(Wishlist)
admin.site.register(Basket)
admin.site.register(BasketItem) 
admin.site.register(Order)
admin.site.register(BillingAddress)

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'zipcode']
    list_filter = ['user', 'city']
    search_fields = ['customer']

