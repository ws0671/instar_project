from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.db.models.fields.related import OneToOneField

# Create your models here.

class Member(models.Model) :
        user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name='member', null=True, blank=True)
        name = models.CharField(max_length=64)
        username = models.CharField(max_length=64)