from django import forms
from django.forms import widgets

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'name',
            'email',
            'comment'
        )
        widgets = {

            'name':forms.TextInput(attrs={
            'class':'input-text'
            }),
        
            'email':forms.EmailInput(attrs={
                'class':'input-text',
            }),

            'comment': forms.Textarea(attrs={
                'class': 'input-text',
            }),
        }