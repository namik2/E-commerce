from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
from accounts.models import User

# Create your models here.

class BlogCategory(models.Model):
    """
        Keeps all blog categories
    """

    category = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.category

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"


class Comment(models.Model):
    """
        This model keeps blog post's comments
    """

    blog        = models.ForeignKey('Blog', on_delete=models.CASCADE, null=True, blank=True, related_name='comments')

    name        = models.CharField(max_length=50)
    email       = models.EmailField(max_length=100, blank=True)
    comment     = models.TextField(max_length=700)
    is_active   = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name


class Blog(models.Model):
    category    = models.ManyToManyField('BlogCategory', related_name='blogs')
    author      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', null=True, blank=True)

    title       = models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to='category_images')
    description = models.CharField(max_length=50)
    is_published= models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    update_at   = models.DateTimeField(auto_now=True)
    view_count  = models.BigIntegerField(default=0)

    def __str__(self) -> str:
        return self.title