from django.db import models
from django.db.models.base import Model
from accounts.models import User
from products.models import Product
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # products = models.ManyToManyField(Product)
    basket = models.ForeignKey('Basket', on_delete=models.SET_NULL, null=True)
    # basket_items = models.ForeignKey('BasketItem', on_delete=models.SET_NULL, null=True)
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey('order.ShippingAddress', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.user_name


class ShippingAddress(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="shipping_address")

    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    address   = models.CharField(max_length=100)
    city        = models.CharField(max_length=50)
    zipcode     = models.CharField(max_length=50)
    country     = models.CharField(max_length=50)
    phone       = PhoneNumberField(blank=True, null=True)

    def __str__(self) -> str:
        return self.address

    class Meta:
        verbose_name = "Shipping Address"
        verbose_name_plural = "Shipping Addresses"


class BillingAddress(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="billing_address")

    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    address     = models.CharField(max_length=100)
    city        = models.CharField(max_length=50)
    zipcode     = models.CharField(max_length=50)
    country     = models.CharField(max_length=50)
    phone       = PhoneNumberField(blank=True, null=True)

    def __str__(self) -> str:
        return self.address

    class Meta:
        verbose_name = "Billing Address"
        verbose_name_plural = "Billing Addresses"


class BasketItem(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="basket_items")
    product     = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, related_name="basket_products")
    quantity    = models.IntegerField(default=0, null=True, blank=True)

    @property
    def price(self):
        return self.product.price * self.quantity

    def __str__(self) -> str:
        return f"{self.product.title} - {self.quantity}"

    class Meta:
        verbose_name = "Basket Item"
        verbose_name_plural = "Basket Items"


class Basket(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name="shoppingcardofUser")
    items       = models.ManyToManyField(BasketItem, related_name="basket_items")

    def total(self):
        total = 0
        for item in self.items.all():
            total += item.price
        return total

    def __str__(self) -> str:
        return f"{self.user.user_name}'s Shopping Card"



class Wishlist(models.Model):
    user      = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name="wishlistofUser")
    product   = models.ManyToManyField(Product, related_name="wishlist_products")

    def __str__(self) -> str:
        return f"{self.user.user_name}'s Wishlist"