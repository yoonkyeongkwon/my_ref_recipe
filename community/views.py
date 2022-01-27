from contextlib import redirect_stderr
from django.shortcuts import render
from django.http import HttpResponse
from .models import Board,Comment
from django.utils import timezone
from django.shortcuts import redirect
from django.urls import path
from . import views
from django.views.generic import TemplateView
import datetime

#커뮤니티 글 쓰기
def community_insert(request):
    
    if request.method == 'POST':
         file=request.FILES['file']
         write_id = request.POST.get('write_id')
         contents = request.POST.get('contents')
         m = Board()
         m.write_id=write_id
         m.contents=contents
         m.views=0
         m.like=0
         m.file=file
         m.save()
    
         return render(request, 'community/community_insert.html')
    else:
        return render(request, 'community/community_insert.html',context={'text':'GET method!!!'})


# 커뮤니티 글 리스트 보기

class community_list(TemplateView):
     template_name = "community/community_list.html"
     def get(self, request):
          comm = Comment.objects.all()
          community_list = Board.objects.all()
          return render(
               request, self.template_name, 
               {
                    'comment':comm, 'board':community_list}
          )
     # return render(request, TemplateView.as_view(template_name='/community/community_list.html'), {'board_list':board_list})


# 커뮤니티 글 수정
def community_modify(request,post_id):
     post=Board.objects.get(id=post_id)
     print(post)
     if request.method == 'POST':
          contents = request.POST['contents']
          try:
               post.file = request.FILES['file']
          except:
               post.file = None
          post.save()
          return redirect('/community/community_list')
     else:
          return render(request,'community/community_modify.html',{'post':post})

#커뮤니티 글 삭제
def community_delete(request, post_id):
  post = Board.objects.get(id=post_id)
  post.delete()
  return render(request,'community/community_list.html')

#테스트창 완료 후 삭제
def test(request):
     board_list=Board.objects.all()
     return render(request, 'community/test.html',{'board_list':board_list})


