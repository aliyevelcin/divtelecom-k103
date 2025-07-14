from core.models import *
from django import forms

class ProductCommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'message-inp', 'placeholder': 'Comment'})
        }