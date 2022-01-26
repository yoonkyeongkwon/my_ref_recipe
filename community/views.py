from django.shortcuts import render
from django.http import HttpResponse
from .models import Board
from django.utils import timezone
from django.shortcuts import redirect
from django.urls import path
from . import views
from django.views.generic import TemplateView
import datetime
from django.utils import timezone
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
          boardlist = Board.objects.all()
          print(boardlist)
          context={'boardlist':boardlist}
          return render(request, self.template_name,context)



# 커뮤니티 글 수정
def community_modify(request,post_id):
     post=Board.objects.get(id=post_id)
     if request.method == 'POST':
          file=request.FILES['file']
          title = request.POST['title']
          contents = request.POST['contents']
          try:
               post.image = request.FILES['image']
          except:
               post.image = None
          post.save()
          return redirect('community/community_list.html',{'post':post})
     else:
          post=Board()
          return render(request,'community/community_modify.html',{'post':post})

#커뮤니티 글 삭제
def delete(request, post_id):
  post = Board.objects.get(id=post_id)
  post.delete()
  return redirect('community_list')

#테스트창 완료 후 삭제
def test(request):
     board_list=Board.objects.all()
     return render(request, 'community/test.html',{'board_list':board_list})
