from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserForm
from datetime import datetime
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.contrib import auth
from django.contrib.auth.models import User
from ref.models import *


# Create your views here.
# 회원가입
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                                            username=request.POST['username'],
                                            password=request.POST['password1'],
                                            email=request.POST['email'],
                                            last_name=request.POST['last_name'],)
            auth.login(request, user)
            return render(request, 'login.html')
        return render(request, 'signup.html')
    return render(request, 'signup.html')

# 로그인
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            star = Recipe.objects.order_by('-inq_cnt')[0:10]
            request.session['username'] = username
            return render(request,'ref/main.html', {'star':star})
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

# 로그아웃
def logout(request):
    auth.logout(request)
    star = Recipe.objects.order_by('-inq_cnt')[0:10]
    return render(request,'ref/main.html', {'star':star})

# home
def home(request):
    return render(request, 'home.html')


#개별구현 로그인

from .models import Userinfo
from django.utils import timezone
from django.http import HttpResponse

def signup_custom(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        password = request.POST.get('password')
        name = request.POST.get('name')
        email= request.POST.get('email')
        last_name= request.POST.get('last_name')

        m = Userinfo(
            id=id, password=password, name=name, email=email, last_name=last_name)
        m.date_joined = timezone.now()
        m.save()
        return HttpResponse(
            '가입 완료<br>%s %s %s' % (id, password, name, email, last_name))
    else:
        return render(request, 'account/signup_custom.html')


def login_custom(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        password = request.POST.get('password')
        m = Userinfo(id=id, password=password)

        try:
            m = Userinfo.objects.get(id=id, password=password)
        except Userinfo.DoesNotExist as e:
            return HttpResponse('로그인 실패')
        else:
            request.session['user_id'] = m.user_id
            request.session['user_name'] = m.user_name 
            print(m.user_id)
        return redirect('account:login')

    else:
        return render(request, 'account/login_custom.html')

def logout_custom(request):
    del request.session['id'] # 개별 삭제
    del request.session['name'] # 개별 삭제
    request.session.flush() # 전체 삭제
    return redirect('index')

