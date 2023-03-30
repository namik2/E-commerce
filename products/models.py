from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class Product(models.Model):
    category        = models.ManyToManyField('products.ProductCategory', related_name='product_category')
    tag             = models.ManyToManyField('products.Tag', related_name='product_tags')

    title           = models.CharField(max_length=50)
    description     =  models.CharField(max_length=50)
    cover_image     = models.ImageField(upload_to="product_cover_images", null=True, blank=True)
    old_price       = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    price           = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    is_published    = models.BooleanField(default=False)
    view_count      = models.IntegerField(default=0)

    def get_quantity(self, obj):
        p_versions = obj.product_version.all()
        q = 0
        for e in p_versions:
            q += e.quantity
        return q

    def get_stock(self, obj):
        stock = 'Not available'
        count = 0
        for elem in obj.product_version.all():
            if elem.quantity != 0:
                count += 1
        if count > 0:
            stock = 'True'
        return stock
    

    def __str__(self) -> str:
        return self.title


class ProductVersion(models.Model):
    product         = models.ForeignKey('products.Product', related_name='product_version', on_delete=models.CASCADE)
    size            = models.ManyToManyField('products.Size', related_name='product_size', blank=True)
    color           = models.ManyToManyField('products.Color', related_name='product_color', blank=True)
    quantity        = models.IntegerField()

    def get_stock(self, obj):
        stock = 'True'
        if obj.quantity == 0:
            stock = "Not available"
        return stock

    def __str__(self) -> str:
        return f'{self.product}, Size: {self.size.all()[0]}, Color: {self.color.all()[0]}'


class ProductCategory(models.Model):
    """
        This model contains all products' categories and subcategories.
    """
    parent       = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='categories')
    title        = models.CharField(max_length=50)

    def __str__(self) -> str:
        if self.parent:
            return f'{self.parent} > {self.title}'
        return self.title

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = 'Product Categories'


class Size(models.Model):
    """
        This models contains all products' sizes.
    """

    size = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.size


class Color(models.Model):
    """
        This model contains all products' colors
    """

    color = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.color


class Tag(models.Model):
    """
        This model contains all products' tags.
    """
    
    tag     = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.tag


class Image(models.Model):
    """
        This model contains photos which related with the products
    """
    product  = models.ForeignKey("Product", on_delete=models.CASCADE, null=True, blank=True, related_name="product_image")

    image    = models.ImageField(upload_to="product_images", null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.product}'


class Review(models.Model):
    """
        This model contains reviews for each products
    """

    product         = models.ForeignKey("Product", on_delete=models.CASCADE, null=True, blank=True, related_name="product_reviews")

    RATES =[
        (1, "20"),
        (2, "40"),
        (3, "60"),
        (4, "80"),
        (5, "100"),
    ]

    value_rate      = models.IntegerField(choices=RATES)
    quality_rate    = models.IntegerField(choices=RATES)
    price_rate      = models.IntegerField(choices=RATES)
    nickname        = models.CharField(max_length=50)
    summary         = models.CharField(max_length=100)
    review          = models.CharField(max_length=500)
    


    def __str__(self) -> str:
        return self.summary