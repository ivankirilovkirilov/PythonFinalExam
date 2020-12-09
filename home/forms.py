from django import forms
from django.contrib.auth.models import User

from home.models import Post, PostComment


# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = User
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'username', 'name': 'username', 'placeholder': 'Username'}),
#             'email': forms.EmailInput(attrs={'class': 'email', 'name': 'email', 'placeholder': 'Email'}),
#             'password': forms.PasswordInput(attrs={'class': 'password', 'name': 'password', 'placeholder': 'Password'}),
#         }
#         fields = ["username", "email", "password"]


# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'username', 'name': 'username', 'placeholder': 'Username'}),
#             'password': forms.PasswordInput(attrs={'class': 'password', 'name': 'password', 'placeholder': 'Password'}),
#         }
#         fields = ["username", "password"]


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ['user']


class DeleteProfileForm(forms.Form):
    username = forms.CharField(label='', max_length=100, widget = forms.HiddenInput())


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = "__all__"
        exclude = ['user', 'post']