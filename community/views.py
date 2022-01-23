from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import Community_Board
from django.utils import timezone
from django.http import HttpResponse
from datetime import date


def community_list(request):
    if request.method == 'POST':
         title = request.POST.get('title')
         write_id = request.POST.get('write_id')
         contents = request.POST.get('contents')
         views = request.POST.get('views')
         regdate = request.POST.get('regdate')
         like = request.POST.get('like')
         post_like_id = request.POST.get('post_like_id')

         m = Community_Board()
    #     title=title, write_id=write_id, contents=contents)
    #     m.date_joined = timezone.now()
         m.title=title
         m.write_id=write_id
         m.contents=contents
         m.views=views
         m.regdate=regdate
         m.like=like
         m.post_like_id=post_like_id
         m.save()
    #     return HttpResponse(
    #     '입력완료<br>%s %s %s' % (title, write_id, contents))
         return render(request, 'community/community_list.html',context={'text': title})
    else:
        return render(request, 'community/community_list.html',context={'text':'GET method!!!'})
