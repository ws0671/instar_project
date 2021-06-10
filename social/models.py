from django.db import models
from django.contrib.auth.models import User
from member.models import Member
# Create your models here.

class Article(models.Model) :
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True, blank=True)
    like_users = models.ManyToManyField(User,related_name='like_articles' )

class Photo(models.Model) :
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True ,related_name='photo')
    image = models.ImageField(upload_to='images/', blank=True, null=True)

class Comment(models.Model) :
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True, related_name='comment')
    writer = models.ForeignKey(Member, on_delete=models.SET_NULL, related_name='comment', null=True, blank=True)
    content = models.TextField()
    is_deleted = models.BooleanField(default=False)
