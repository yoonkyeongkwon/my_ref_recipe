from compileall import compile_dir
from hmac import compare_digest
from importlib.resources import contents
from django.shortcuts import render
from django.http import HttpResponse
from .models import Board
from .models import Comment
from django.utils import timezone
from django.shortcuts import redirect
from django.views.generic import TemplateView

#커뮤니티 글 쓰기
def community_insert(request):
    
    if request.method == 'POST':
         file=request.FILES['file']
         title = request.POST.get('title')
         write_id = request.POST.get('write_id')
         contents = request.POST.get('contents')
         m = Board()
         m.title=title
         m.write_id=write_id
         m.contents=contents
   
         m.views=0
         m.like=0
         m.file=file
         m.save()
    
         return render(request, 'community/community_insert.html')
    else:
        return render(request, 'community/community_insert.html',context={'text':'GET method!!!'})

class community_list(TemplateView):
     template_name = "community/community_list.html"
     def get(self, request):
          comment = Comment.objects.all()
          # comm.contents = contents
          community_list = Board.objects.all()
          print(community_list)
          list = {'comment':comment, 'board':community_list}
          return render(
               request, self.template_name, 
               {
                    'list':list
               }
          )
     # return render(request, TemplateView.as_view(template_name='/community/community_list.html'), {'board_list':board_list})


# 커뮤니티 글 수정
def community_modify(request):
     post=Board.objects.get()
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
     return redirect('home')

#테스트창 완료 후 삭제
def test(request):
     return render(request, 'community/test.html')

def test2(request):
     return render(request, 'community/test2.html')




