from django.db import models
from django.db.models.base import Model
from django.db.models.fields import EmailField
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Subscriber(models.Model):
    """
        This model keeps email-accounts for subscribe
    """

    email       = models.EmailField(max_length=50)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.email


class Contact(models.Model):
    """
        This is for contact page. Keeps contact information
    """

    first_name  = models.CharField(max_length=30)
    email       = models.EmailField(max_length=50)
    company     = models.CharField(max_length=100, blank=True)
    telephone   = PhoneNumberField(null=False, blank=False, unique=True)
    address     = models.TextField(max_length=300)
    message     = models.TextField(max_length=1000)

    def __str__(self) -> str:
        return self.first_name


