from django.shortcuts import render

from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts":posts})


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")