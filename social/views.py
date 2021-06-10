from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import request, JsonResponse

from member.models import Member
from .models import Article, Photo, Comment
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
    print(article.like_users.count())
    return JsonResponse({'liked':liked, 'count':article.like_users.count()})

def comment(request, **kwargs) :
    comment = request.POST['comment']
    article_pk = kwargs['article_pk']

    article = Article.objects.get(pk=article_pk)
    writer = Member.objects.get(user=request.user)
    comment = Comment.objects.create(
        writer=writer,
        content=comment,
        article=article
    )    
    

    return redirect('member:main')

