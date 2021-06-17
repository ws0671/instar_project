from django.db.models.query import RawQuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import request, JsonResponse

from member.models import Member
from .models import Article, Photo, Comment,Tag
# Create your views here.

def upload(request) :
    if request.method == 'POST' :
        content = request.POST['content']
        tag_name = request.POST['tag_name']
        tag = Tag.objects.filter(name=tag_name)
        article = Article.objects.create(
            content=content,
            writer=request.user,
        )
        print(article)
        if (len(tag) > 0):
            article.tags.add(tag.first())
            return redirect('member:main')
        tag = Tag.objects.create(name=tag_name)
        article.tags.add(tag)
        
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

def tag_detail(request, tag_pk) :
    articles = Article.objects.filter(tags__pk__in=[tag_pk])
    tags = Tag.objects.filter(pk=tag_pk).first()
    context = {'articles': articles, 'tags': tags}
    print(articles)

    return render(request, 'tag_detail.html', context)
