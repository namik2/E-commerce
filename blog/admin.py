from django.contrib import admin
from .models import Blog, BlogCategory, Comment
from django.utils.html import format_html
# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_image', 'get_categories', 'created_at', 'is_published')
    list_filter = ('title', 'author', 'category')
    search_fields = ('title', 'description')
    list_editable = ['is_published']
    readonly_fields = ['view_count']

    fieldsets = (
        ('General Information', {
            'fields' : ('title', 'author', 'cover_image')
        }),
        ('Content', {
            'fields' : ('category', 'description')
        }),
        ('Statictics', {
            'fields' : ('view_count', 'is_published')
        })
    )

    def get_image(self, obj):
        str = 'No Cover Image'
        if obj.cover_image:
            str = f'<img src="{obj.cover_image.url}" width = "100" height="100" />'
        return format_html(str)
    get_image.short_description = "Cover Images"

    def get_categories(self, obj):
        r = ''
        for c in obj.category.all():
            r += f'{c.category}'
        return format_html(r)
    get_categories.short_description = "Categories"


@admin.register(BlogCategory)
class BlogcategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']
    # list_display_links = ['category']
    list_editable = ['category']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'blog', 'is_active']
    list_filter = ['is_active']
    search_fields = ['blog', 'comment']
    list_editable = ['is_active']

    fieldsets = (
        ('General Information', {
            'fields' : ('name', 'email', 'blog')
        }),
        ('Content', {
            'fields' : ('comment', 'is_active')
        })
    )