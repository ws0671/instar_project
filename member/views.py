from social.models import Article
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

from .models import Member
from social.models import Comment
# Create your views here.
ERROR_MSG = {
    'MISSING_INPUT': '필수항목을 작성해주세요.',
    'MISSING_PW' : '잘못된 비밀번호입니다. 다시 확인하세요'
}
def index(request) :
    context = {
        'error' : {
            'state' : False,
            'msg' : ''
        }
    }
    if request.method == 'POST' :
        useremail = request.POST['useremail']
        password = request.POST['password']
        auth_user = auth.authenticate(username=useremail, password=password)

        if (auth_user) :
            auth.login(request, auth_user)
            return redirect('member:main')

        else :
            context['error']['state'] = True
            context['error']['msg'] = ERROR_MSG['MISSING_PW']

        if (not useremail or not password) :
            context['error']['state'] = True
            context['error']['msg'] = ERROR_MSG['MISSING_INPUT']

    return render(request, 'index.html', context)

def signup(request) :

    if request.method == 'POST' :
        useremail = request.POST['useremail']
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(
            username=useremail,        
            password=password
        )

        Member.objects.create(
            user=user,
            name=name,
            username=username,
        )

        auth.login(request, user)

        return redirect('index')
    return render(request, 'signup.html')

def logout(request) :
    auth.logout(request)

    return redirect('index')

def main(request) :
    article = Article.objects.all()
    context = {
        'article': article,
    }
    return render(request, 'main.html', context)

def profile(request) :
    user = request.user
    member = Member.objects.filter(user=user).first()
    context = {
        'member' : member
    }
    return render(request, 'profile.html', context)

def edit(request) :
    user = request.user
    member = Member.objects.filter(user=user)
    context ={
        'member' : member.first()
    }

    if request.method == 'POST' :
        name = request.POST['name']
        username = request.POST['username']

        member.update(
            name=name,
            username=username
        )
        return redirect('member:edit')       
        
    return render(request, 'edit.html', context)
