from django.core.mail import send_mail
from django.db import models

# from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from accounts.managers import UserManager

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    
    email           = models.EmailField(('email address'), unique=True)
    user_name       = models.CharField(max_length=150, unique=True, blank=True, null=True)
    first_name      = models.CharField(max_length=150)
    last_name       = models.CharField(max_length=150)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=False)
    image           = models.ImageField(upload_to='profile_photos', null=True, blank=True)
    
    objects         = UserManager()

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name']

    def email_user(self, subject, message):
        send_mail(
            subject,
            message,
            recipient_list = [self.email],
            from_email='superbmyproject@gmail.com'
        )

    def __str__(self):
        return self.email