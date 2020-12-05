from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
            'username': forms.TextInput(attrs={'class': 'username', 'name': 'username', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'email', 'name': 'email', 'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'class': 'password', 'name': 'password', 'placeholder': 'Password'}),
        }
        fields = ["username", "email", "password"]


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
            'username': forms.TextInput(attrs={'class': 'username', 'name': 'username', 'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'class': 'password', 'name': 'password', 'placeholder': 'Password'}),
        }
        fields = ["username", "password"]