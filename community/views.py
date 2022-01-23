from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import Community_Board
from django.utils import timezone
from django.http import HttpResponse
from datetime import date

def community_insert(request):
    if request.method == 'POST':
         title = request.POST.get('title')
         write_id = request.POST.get('write_id')
         contents = request.POST.get('contents')

         m = Community_Board()
         m.title=title
         m.write_id=write_id
         m.contents=contents
         m.regdate=date.today().isoformat()
         m.save()
         upload_file = request.FILES.get('file') # 파일 객체
         name = upload_file.name # 파일 이름
         size = upload_file.size # 파일 크기
         with open(name, 'wb') as file: # 파일 저장
             for chunk in upload_file.chunks():
              file.write(chunk)
         return HttpResponse('%s<br>%s' % (name, size))
         return render(request, 'community/community_insert.html')
    else:
        return render(request, 'community/community_insert.html',context={'text':'GET method!!!'})
