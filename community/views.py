from django.shortcuts import render
#from django.utils import timezone
from django.http import HttpResponse
from .models import Board
from django.utils import timezone
from django.http import HttpResponse
from datetime import date
from datetime import datetime
import datetime
from pytz import timezone

def community_insert(request):
    
    if request.method == 'POST':
         now = datetime.datetime.now(timezone('Asia/Seoul'))
         print(now)
         print(request.POST)
         file=request.FILES['file']
         title = request.POST.get('title')
         write_id = request.POST.get('write_id')
         contents = request.POST.get('contents')
         m = Board()
         m.title=title
         m.write_id=write_id
         m.contents=contents
     #     m.regdate=now.strftime('%Y-%m-%d')

         m.views=0
         m.like=0
         m.file=file
         m.save()
    
         return render(request, 'community/community_insert.html')
    else:
        return render(request, 'community/community_insert.html',context={'text':'GET method!!!'})

def community_list(request):
     return render(request, 'community/community_list.html')