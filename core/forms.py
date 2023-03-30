from django import forms
from django.forms import fields, widgets
from phonenumber_field.modelfields import PhoneNumberField
from .models import Contact, Subscriber


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = (
            'first_name',
            'email',
            'company',
            'telephone',
            'address',
            'message'
        )
        widgets = {
            'first_name' : forms.TextInput(attrs={
                'class' : 'input-text',
            }),
            'email' : forms.EmailInput(attrs={
                'class' : 'input-text'
            }),
            'company' : forms.TextInput(attrs={
                'class' : 'input-text'
            }),
            'telephone' : forms.TextInput(attrs={
                'class' : 'input-text'}),
            'address' : forms.TextInput(attrs={
                'class' : 'input-text'
            }),
            'message' : forms.Textarea(attrs={
                'class' : 'input-text'
            })

        }

    # def save(self, commit=True):
    #     instance = super(ContactForm, self).save(commit=False)
    #     if commit:
    #         instance.save()
    #     return instance




class SubScriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = '__all__'

        widgets = {
          
            'email':forms.EmailInput(attrs={
            'class':'input-text',
            'placeholder':'Enter your email adress',
            }),
        }

        def save(self, commit=True):
            return super().save(commit=commit)