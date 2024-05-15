from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserForm(UserCreationForm):
    username = forms.CharField(max_length=150, help_text='Enter your username')
    phone_number = forms.CharField(max_length=15, required=True, help_text='Enter your phone number')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control my-2', 'placeholder': 'enter password1'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control my-2', 'placeholder': 'confirm password'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'phone_number', 'password1', 'password2']
