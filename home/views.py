from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# from .forms import RegisterForm, LoginForm
from .forms import DeleteProfileForm, PostCreationForm, PostCommentForm
from .models import Post, PostComment


def index(request):
    posts = Post.objects.all()
    users = User.objects.all()
    return render(request, "index.html", {"posts":posts})


def create_post(request):
    if request.method == "POST":
        form = PostCreationForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            form.save()
            return redirect("/")
    else:
        form = PostCreationForm()
    return render(request, "create_post.html", {"form": form})


def user_posts(request):
    posts = Post.objects.all().filter(user_id=request.user.id)
    return render(request, "user_posts.html", {"posts": posts})


# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         username = form['username'].value()
#         password = form['password'].value()
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('/')
#         else:
#             return redirect('/login/')
#
#     else:
#         form = LoginForm()
#
#     return render(request, "registration/login.html", {"form":form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(request, username=request.POST['username'], password=request.POST['password1'])
            if user is not None:
                login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form":form})


def logout(request):
    logout(request)
    return redirect(index)


def profile(request):
    return render(request, 'registration/profile.html')


def password_change(request):
    instance = User.objects.filter(username=request.user.username).first()
    if request.method == 'POST':
        form = UserCreationForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm(instance=instance)

    return render(request, "registration/password_change_form.html", {"form":form, "user":instance})


def delete_account(request):
    if request.method == 'POST':
        user = User.objects.filter(username=request.user.username).first()
        if user is not None:
            user.delete()
            return redirect('/')
    else:
        form = DeleteProfileForm()

    return render(request, "registration/delete_account.html", {"form":form})


def post_info(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        form = PostCommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.post = post
            form.save()
            return redirect(f"/posts/{post_id}/")
    else:
        form = PostCommentForm()
    post_comments = PostComment.objects.filter(post_id=post_id).order_by('id')

    return render(request, "post_comments.html", {"form": form, "post": post, "post_comments": post_comments})


def commented_posts(request):

    posts = Post.objects.filter(postcomment__user_id=request.user.id).distinct()
    return render(request, "commented_posts.html", {"posts": posts})