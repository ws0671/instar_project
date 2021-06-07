from django.shortcuts import render, redirect, get_object_or_404
from django.http import request

from .models import Article, Photo
# Create your views here.

def upload(request) :
    if request.method == 'POST' :
        content = request.POST['content']
        article = Article.objects.create(
            content=content,
            writer=request.user
        )
        for img in request.FILES.getlist('image'):
            Photo.objects.create(
                article=article,
                image=img
            )
        

        return redirect('member:main')
        
    return render(request, 'upload.html')
    