from django.shortcuts import render, redirect, get_object_or_404
from django.http import request, JsonResponse

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
    
def like(request, article_pk) :
    article = get_object_or_404(Article, pk=article_pk)

    if request.user in article.like_users.all():
        article.like_users.remove(request.user)
        liked = False
    else:
        article.like_users.add(request.user)
        liked = True
    return JsonResponse({'liked':liked})