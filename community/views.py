from compileall import compile_dir
from distutils.command.upload import upload
from hmac import compare_digest
from importlib.resources import contents
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from .models import Board
from .models import Comment
from contextlib import redirect_stderr
from django.shortcuts import render
from django.http import HttpResponse, request
from django.views import View
from .models import Board,Comment
from django.utils import timezone
from django.shortcuts import redirect
from django.views.generic import TemplateView
import datetime
from django.views.generic.detail import SingleObjectMixin
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

#
import urllib
import os
from django.http import HttpResponse, Http404
import mimetypes


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
  return redirect('home')

#테스트창 완료 후 삭제
def test(request):
     return render(request, 'community/test.html')

def test2(request):
     return render(request, 'community/test2.html')


#테스트창 완료 후 삭제
def test(request):
     board_list=Board.objects.all()
     return render(request, 'community/test.html',{'board_list':board_list})


#파일 다운로드
class FileDownloadView(SingleObjectMixin, View):
    queryset = Board.objects.all()

    def get(self, request, document_id):
        object = self.get_object(id=document_id)

        file_path = object.attached.path
        file_type = object.content_type  # django file object에 content type 속성이 없어서 따로 저장한 필드
        fs = FileSystemStorage(file_path)
        response = FileResponse(fs.open(file_path, 'rb'), content_type=file_type)
        response['Content-Disposition'] = f'attachment; filename={object.file()}'
        
        return response



def downloads(request):
     id = request.GET.get('id')
     print(id,22222222222)
     uploadFile = Board.objects.get(id=id)
     print(uploadFile,3333333333333)
     filepath = str(settings.BASE_DIR) + ('/media/%s' % uploadFile.file.name)
     filename = os.path.basename(filepath)
     with open(filepath, 'rb') as f:
          response = HttpResponse(f, content_type='application/octet-stream')
          response['Content-Disposition'] = 'attachment; filename=%s' % filename
          return response