from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Article(models.Model) :
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True, blank=True)

class Photo(models.Model) :
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True ,related_name='photo')
    image = models.ImageField(upload_to='images/', blank=True, null=True)