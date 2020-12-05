from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .forms import RegisterForm, LoginForm
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts":posts})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = form['username'].value()
        password = form['password'].value()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/login/')

    else:
        form = LoginForm()

    return render(request, "registration/login.html", {"form":form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form":form})
