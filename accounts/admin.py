from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_display_links = ['email']
    fieldsets = (
        ('General Information', {
            'fields' : ('email', 'password')
        }),
        ('Personal Information' , {
            'fields' : ('user_name', 'first_name', 'last_name', 'image')
        }),
        ('Permissions', {
            'fields' : ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Statistics', {
            'fields' : ['last_login']
        })
    )


# admin.site.register(User)