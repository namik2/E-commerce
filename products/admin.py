from django.contrib import admin
from .models import Image, ProductVersion, Size, Color, ProductCategory, Product, Tag, Review
from django.utils.html import format_html


# Register your models here.

class ProductVersionInline(admin.TabularInline):
    model = ProductVersion
    extra = 2

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines     = [ProductVersionInline]
    list_display = ['title', 'get_image', 'price', 'get_stock', 'get_quantity', 'is_published', 'view_count']
    list_editable = ['is_published']

    def get_image(self, obj):
        str = 'No cover image'
        if obj.cover_image:
            str = f'<img src="{obj.cover_image.url}" width="100" height="100" >/'
        return format_html(str)
    get_image.short_description = "Cover Image"


    def get_quantity(self, obj):
        q = 0
        for e in obj.product_version.all():
            q += e.quantity
        return q
    get_quantity.short_description = 'Quantity'

    def get_stock(self, obj):
        stock = 'Not available'
        count = 0
        for elem in obj.product_version.all():
            if elem.quantity != 0:
                count += 1
        if count > 0:
            stock = 'True'
        return stock
    get_stock.short_description = 'stock'


    fieldsets = (
        ('General information', {
            'fields' : ('title', 'cover_image', 'old_price', 'price')
        }),
        ('Spesification', {
            'fields' : ('tag', 'category')
        }),
        ('Content', {
            'fields' : ('description', 'is_published')
        })
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'product', 'value_rate', 'quality_rate', 'price_rate']
    list_filter = ['value_rate', 'quality_rate', 'price_rate']

    fieldsets = (
        ('Product', {
            'fields' : ['product']
        }),
        ('User Information', {
            'fields' : ['nickname']
        }),
        ('Content', {
            'fields' : ('summary', 'review')
        }),
        ('Ratings', {
            'fields' : ('value_rate', 'quality_rate', 'price_rate')
        })
    )


@admin.register(ProductVersion)
class ProductVersionAdmin(admin.ModelAdmin):
    list_display = ['product', 'get_size', 'get_color', 'quantity', 'get_stock']
    # list_editable = ['get_color', 'get_size']

    fieldsets = (
        ('Product', {
            'fields' : ['product']
        }),
        ('Characteristics', {
            'fields' : ['size', 'color']
        }),
        ('Statistics', {
            'fields' : ['quantity']
        }),
    )

    def get_color(self, obj):
        return obj.color.all()[0]
    get_color.short_description = 'color'

    def get_size(self, obj):
        return obj.size.all()[0]
    get_size.short_description = 'size'

    def get_stock(self, obj):
        r = 'True'
        if obj.quantity == 0:
            r = "Not available"
        return format_html(r)
    get_stock.short_description = 'stock'
    

admin.site.register(Tag)
admin.site.register(Image)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(ProductCategory)
