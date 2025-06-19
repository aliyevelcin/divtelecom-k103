from django import forms
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'reg-inp', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'reg-inp', 'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ['first_name',  'last_name', 'username', 'image', 'bio', 'email', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'reg-inp', 'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'class': 'reg-inp', 'placeholder': 'Last name'}),
            'username': forms.TextInput(attrs={'class': 'reg-inp', 'placeholder': 'Username'}),
            'image': forms.FileInput(attrs={'class': 'reg-inp', 'placeholder': 'Image'}),
            'bio': forms.Textarea(attrs={'class': 'reg-inp', 'placeholder': 'bio'}),
            'email': forms.EmailInput(attrs={'class': 'reg-inp', 'placeholder': 'Email'}),
        }