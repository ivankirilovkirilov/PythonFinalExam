from django.db import models


class Post(models.Model):
    image = models.ImageField(upload_to='images')
    heading = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
