from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db.models import Count

# from .forms import RegisterForm, LoginForm
from .forms import DeleteProfileForm, PostCreationForm, PostCommentForm, PostLikeForm
from .models import Post, PostComment, PostLike, Category


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
    return render(request, "create_post.html", {"form": form, "command":"Create"})


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
    post_likes = PostLike.objects.filter(post_id=post_id)
    like_form = PostLikeForm()
    user = request.user
    already_liked = False
    for like in post_likes:
        if like.user == user:
            already_liked = True
            break
        else:
            already_liked = False

    return render(request, "post_comments.html",
                {
                    "form": form,
                    "post": post,
                    "post_comments": post_comments,
                    "likes": post_likes,
                    "like_form": like_form,
                    "already_liked": already_liked,
                }
    )


def commented_posts(request):

    posts = Post.objects.filter(postcomment__user_id=request.user.id).distinct()
    return render(request, "commented_posts.html", {"posts": posts})


def like_post(request, post_id):
    if request.method == "POST":
        form = PostLikeForm(request.POST)
        post_likes = PostLike.objects.filter(post_id=post_id)
        if form.is_valid():
            for like in post_likes:
                if like.user == request.user:
                    like.delete()
                    return redirect(f"/posts/{post_id}/")
            instance = form.save(commit=False)
            instance.user = request.user
            instance.post = Post.objects.get(id=post_id)
            form.save()

    return redirect(f"/posts/{post_id}/")


def category_chooser(request):
    categories = Category.objects.all()

    posts_counter = Post.objects.annotate(total_categories=Count('category'))

    return render(request, "category_chooser.html", {"categories": categories})


def category(request, category_id):
    choosen_category = Category.objects.get(id=category_id)
    posts = Post.objects.filter(category=choosen_category)
    return render(request, "category.html", {"posts":posts, "category": choosen_category})


def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        form = PostCreationForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            form.save()
            return redirect("/")
    else:
        form = PostCreationForm(instance=post)
    return render(request, "create_post.html", {"form": form, "command":"Edit"})


def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        form = PostCreationForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post.delete()
            return redirect("/")
    else:
        form = PostCreationForm(instance=post)
    return render(request, "create_post.html", {"form": form, "command":"Delete"})


def edit_comment(request, comment_id):
    comment = PostComment.objects.get(id=comment_id)
    if request.method == "POST":
        form = PostCommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            form.save()
            return redirect("/")
    else:
        form = PostCommentForm(instance=comment)
    return render(request, "edit_comment.html", {"form": form, "command":"Edit"})


def delete_comment(request, comment_id):
    comment = PostComment.objects.get(id=comment_id)
    if request.method == "POST":
        form = PostCommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment.delete()
            return redirect("/")
    else:
        form = PostCommentForm(instance=comment)
        form.fields['text'].widget.attrs['readonly'] = True
    return render(request, "edit_comment.html", {"form": form, "command":"Delete"})
