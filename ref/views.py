from distutils.command.check import check
from msilib.schema import ListView
from socket import AI_PASSIVE
from typing import Dict
from django.http import HttpResponse
from django.shortcuts import render
from myref import settings

from myref.settings import YOUTUBE_DATA_API_KEY
from .models import *
from django.views import View
 

# Create your views here.
# def main(request):
#     if request.method == "GET":    
#         recipe_list = Recipe.objects.order_by('rcp_sno')[0:1]
#         userref_list = UserRef.objects.all()
#         request.session['recipe_list'] = recipe_list
#         return render(request,'ref/main.html',{'recipe_list':recipe_list,'userref_list':userref_list})
    
#     elif request.method == "POST":
#         recipe_list = request.session['recipe_list']
#         temp = request.POST.get('material_name')
#         return render(request, 'ref/main.html', context={'recipe_list': recipe_list, 'text': temp})

# def material(request):
#     if request.method == "POST":
#         temp = request.POST.get('material_name')
#         new_temp = UserRef()
#         new_temp
#         return render(request, 'ref/main.html', context={'text': temp})
#     else:
#         return render(request, 'ref/main.html', context={'text':'GET METHOD!!!'})
        
class main_view(View):
    array =[]        
    def get(self, request, *args, **kwargs):
        star = Recipe.objects.order_by('-inq_cnt')[0:10]
        # recipe_list = Recipe.objects.all()[0]
        userref_list = Mine.objects.all()
        recipe_list = '00'
        request.session['recipe_list'] = recipe_list
        return render(request,'ref/main.html',{'recipe_list':recipe_list,'userref_list':userref_list, 'star':star})
    
    def post(self, request, *args, **kwargs):   
        recipe_list = request.session['recipe_list']
        self.array.append(request.POST.get('material_name'))
        temp = self.array
        new_temp = Mine()
        new_temp.ingredients = temp
        new_temp.save()
        # new_temp_output = new_temp.objects.all()
        
        return render(request, 'ref/main.html', context={'temp' : temp ,'recipe_list': recipe_list, 'new_temp_output': new_temp})


def myPage(request):
    return render(request, 'ref/mypage.html', {})






        
from .models import *
from django.views.decorators.csrf import csrf_exempt
import requests
from isodate import parse_duration
from account.models import Userinfo
from itertools import *

@csrf_exempt
def searchRecipe(request):

    user_check = request.POST.get('user_like') 
    board_info = Board.objects.all()
    
    username = ""
    if 'username' in request.session:
        username = request.session.get('username')
    else:
        username = request.session.get('default','guest')


    cntr=Recipe.objects.all().count()
    cntm=Mine.objects.all().count()
    listscore = []
    score = 0
    listmtrl=[]
    for i in range(0,cntm):
        mtrl = Recipe.objects.filter(ckg_mtrl_cn__contains=Mine.objects.get(pk=i+1,id='admin').ingredients).values('mtrl')
        mtrl_cnt = Recipe.objects.filter(ckg_mtrl_cn__contains=Mine.objects.get(pk=i+1,id='admin').ingredients).values('mtrl_cnt')
        for j in (0,cntr):
            reci = Recipe.objects.all().values('mtrl')

    reci = dict(reci)
    print(type(reci))

    


    # # 어레이는 레시피데이터 배열 처리
    # for i in range(0,cnt):
    #     FT = Recipe.objects.filter(ckg_mtrl_cn__contains=Mine.objects.get(pk=i+1,id='admin').ingredients).values('ckg_mtrl_cn')
    #     leng = Recipe.objects.filter(ckg_mtrl_cn__contains=Mine.objects.get(pk=i+1,id='admin').ingredients).values('ckg_mtrl_cn').count()
    #     ST = ""
    #     for j in range(0,leng):
    #         ST += str(FT.values('ckg_mtrl_cn')[j]['ckg_mtrl_cn'])+"/"
    #         array += [FT.values('ckg_mtrl_cn')[j]['ckg_mtrl_cn']]

    # array = set(array)
    # array = list(array)
    # array.sort()
    
    # ## mo는 내 냉장고 재료
    # print(array,'@@@@@@@@@@@@@@@@@@@@@@')
    # newarray = []
    # for i in range(0,cnt):
    #     mo = Mine.objects.get(pk=i+1,id='admin').ingredients
    #     for s in array:
    #         if s.__contains__(mo):
    #             print(s)
    #     print(s,'&&&&&&&&&&&&&&&&&&&&&')
    #     print(mo,'$$$$$$$$$$$$$$$$$$')


    # print(ST,'#########################')
    


    # recipe_list = ST[0:10]    

    recipe_list = Recipe.objects.all()[0:5]
    query = str(recipe_list[0].ckg_nm)

    # 

    # def filtering(num,FT):
    #     FT = FT(ckg_mtrl_cn__contains=Mine.objects.get(pk=num).ingredients)
    #     num -= 1
    #     filtering(num,FT)  
    #     if(num==0):
    #         return FT
        
    # filtering(cnt,FT)


    search_url = 'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'
    search_params = {
        'part' : 'snippet',
        'q' : query,
        'key' : settings.YOUTUBE_DATA_API_KEY,
        'maxResults' : 4,
        'type':'video'
    }
    video_ids = []
    r = requests.get(search_url,params=search_params)

    results = (r.json()['items'])
    for result in results:
        video_ids.append(result['id']['videoId'])
    
    video_params = {
        'key' : settings.YOUTUBE_DATA_API_KEY,
        'part' : 'snippet,contentDetails',
        'id' : ','.join(video_ids),
        'maxResults' : 4,
    }
    r = requests.get(video_url,params=video_params)
    results = (r.json()['items'])
    videos=[]
    for result in results:
        video_data = {
            'title' : result['snippet']['title'],
            'id' : result['id'],
            'url': f'https://www.youtube.com/watch?v={result["id"]}',
            'duration' : int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60 ),
            'thumbnail' : result['snippet']['thumbnails']['high']['url'],
        }
        print(result['id'])

        videos.append(video_data)

        context ={
            'videos':videos,
            'recipe_list':recipe_list,
            'user_check':user_check,
            'board_info':board_info,
        }

    # context ={
    #     'recipe_list':recipe_list,
    #     'user_check':user_check,
    #     'board_info':board_info,
    # }
        

    return render(request,'ref/searchRecipe.html',context)

