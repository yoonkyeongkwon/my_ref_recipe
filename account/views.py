from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserForm

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'account/signup.html', {'form': form})


'''
개별구현 로그인

from .models import Userinfo
from django.utils import timezone
from django.http import HttpResponse

def signup_custom(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        password = request.POST.get('password')
        name = request.POST.get('name')
        email= request.POST.get('email')

        m = Userinfo(
            id=id, password=password, name=name, email=email)
        m.date_joined = timezone.now()
        m.save()
        return HttpResponse(
            '가입 완료<br>%s %s %s' % (id, password, name, email))
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
        return redirect('account:login')

    else:
        return render(request, 'account/login_custom.html')

def logout_custom(request):
    del request.session['id'] # 개별 삭제
    del request.session['name'] # 개별 삭제
    request.session.flush() # 전체 삭제
    return redirect('index')
'''
