from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE, SET_NULL


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    image = models.ImageField(upload_to='images')
    heading = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.heading} | {self.user.username}"


class PostComment(models.Model):
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=CASCADE)
    text = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post.heading} | {self.user.username}"