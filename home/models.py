from django.db import models


class Post(models.Model):
    image = models.ImageField(upload_to='images')
    heading = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)
