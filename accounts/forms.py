from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.db.models import fields
from django.forms.fields import EmailField
from django.forms.models import ModelForm
from django.shortcuts import render
# from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import (
    PasswordChangeForm, UserCreationForm, UsernameField, AuthenticationForm, PasswordResetForm,SetPasswordForm
)

User = get_user_model()


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
                'class': 'input-text',
                'placeholder': 'Password'
            }),
        help_text=password_validation.password_validators_help_text_html(),
        
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={
                'class': 'input-text',
                'placeholder': 'Confirm Password'
            }),
        strip=False,
        help_text=("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'input-text',
                'placeholder': 'First Name*'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'input-text',
                'placeholder': 'Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input-text',
                'placeholder': 'Email'
            }),
        }


class LoginForm(AuthenticationForm):
    username    = UsernameField(widget=forms.TextInput(attrs={
        'autofocus': True,
        'class': 'input-text',
        'name': 'email'
    }))
    password    = forms.CharField(
        label   = ("Password"),
        strip   = False,
        widget  = forms.PasswordInput(attrs={
            'class': 'input-text',
            'name': 'password',            
        }),
    )

    class Meta:
        model   = User
        fields  = ['username', 'password']




# Password Reset 

class PwdResetForm(PasswordResetForm):

    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'input-text', 'placeholder': 'Email', 'id': 'form-email'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        u = User.objects.filter(email=email)
        if not u:
            raise forms.ValidationError(
                'Unfortunatley we can not find that email address')
        return email


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New password', widget=forms.PasswordInput(
            attrs={'class': 'input-text', 'placeholder': 'New Password', 'id': 'form-newpass'}))
    new_password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput(
            attrs={'class': 'input-text', 'placeholder': 'New Password', 'id': 'form-new-pass2'}))


class AccountForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'input-text'}),
            'last_name': forms.TextInput(attrs={
                'class': 'input-text'}),
            'email': forms.EmailInput(attrs={
                'class': 'input-text'}),
        }
