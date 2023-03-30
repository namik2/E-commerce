from django import forms
from django.forms import widgets

from .models import Review

class Reviewform(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            'value_rate',
            'quality_rate',
            'price_rate',
            'nickname',
            'summary',
            'review'
        )
        widgets = {

            'value_rate' : forms.RadioSelect(attrs={
                'class' : 'radio'
            }),
            'quality_rate' : forms.RadioSelect(attrs={
                'class' : 'radio'
            }),
            'price_rate' : forms.RadioSelect(attrs={
                'class' : 'radio'
            }),
            'nickname':forms.TextInput(attrs={
            'class':'input-text'
            }),
            'summary':forms.TextInput(attrs={
            'class':'input-text'
            }),
            'review': forms.Textarea(attrs={
                'class': 'input-text',
            }),
        }