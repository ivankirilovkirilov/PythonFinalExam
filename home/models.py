from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    image = models.ImageField(upload_to='images')
    heading = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)
