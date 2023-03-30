from django.contrib import admin
from .models import Subscriber, Contact

# Register your models here.

admin.site.register(Subscriber)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'email', 'telephone', 'message']
    search_fields = ['first_name', 'message', 'address']

    fieldsets = (
        ('Contact Information' , {
            'fields' : ('first_name', 'email', 'telephone', 'address', 'company')
        }),
        ('Message', {
            'fields' : ['message']
        })
    )