from distutils.command.check import check
from msilib.schema import ListView
from socket import AI_PASSIVE
from typing import Dict
from django.http import HttpResponse
from django.shortcuts import render
from myref import settings
from account.models import Userinfo
from myref.settings import YOUTUBE_DATA_API_KEY
from .models import *
from django.views import View

class main_v(View):
    array = []       
    def get(self, request, *args, **kwargs):
        star = Recipe.objects.order_by('-inq_cnt')[0:10]
        recipe_list = Recipe.objects.all()
        userref_list = Mine.objects.all()
        # # request.session['recipe_list'] = star
        return render(request,'ref/main.html',{'recipe_list':recipe_list,'userref_list':userref_list, 'star':star})
    
    def post(self, request, *args, **kwargs):   
        # recipe_list = request.session['recipe_list']
        star = Recipe.objects.order_by('-inq_cnt')[0:10]
        mn = request.POST.get('material_name')
        ed = request.POST.get('expire_date')
        array = self.array
        username= request.session['username']
        temp = mn
        new_temp = Mine()
        if mn not in array:
            self.array.append(mn)
            new_temp.ingredients = temp
            if ed != "":
                new_temp.expiry_date = ed
            new_temp.id = username
            new_temp.save()
        
        return render(request, 'ref/main.html', context={'array' : array, 'star':star})

class myPage(View):
    def get(self, request, *args, **kwargs):
        # nickname = Userinfo.objects.get(username=self.user.username)
        username= request.session['username']
        uinfo = Userinfo.objects.get(name=username)
        return render(request,'ref/mypage.html',{'uinfo':uinfo})


        
from .models import *
from django.views.decorators.csrf import csrf_exempt
import requests
from isodate import parse_duration
from account.models import Userinfo
from itertools import *

@csrf_exempt
def searchRecipe(request):
    from collections import defaultdict
    user_check = request.POST.get('user_like') 
    board_info = Board.objects.all()
    username= request.session['username']

    # username = ""
    # if 'username' in request.session:
    #     username = request.session.get('username')
    # else:
    #     username = request.session.get('default','guest')


    cntr=Recipe.objects.all().count()
    cntm=Mine.objects.filter(id=username).count()
    print(cntm)
 

# user의 재료 목록 가져와 일치하는 레시피 정렬
    dic = defaultdict(int)
    for i in range(0,cntm):
        filter_rcp= Recipe.objects.filter(ckg_mtrl_cn__contains=Mine.objects.filter(id=username)[i].ingredients).values('rcp_sno')
        filter_mtrl= Recipe.objects.filter(ckg_mtrl_cn__contains=Mine.objects.filter(id=username)[i].ingredients).values('mtrl_cnt')
        print("여기",filter_mtrl[0]['mtrl_cnt'])
        
        for j in range(len(filter_rcp)):
            
            if dic[filter_rcp[j]['rcp_sno']]:
                dic[filter_rcp[j]['rcp_sno']] +=1
            else:
                dic[filter_rcp[j]['rcp_sno']] = 1
                            
    arr1 =[]
    for i,v in dic.items():
        get_mtrl_cnt= Recipe.objects.get(rcp_sno=i)
        arr1.append((i,v,get_mtrl_cnt.mtrl_cnt))
    import operator
    result = sorted(arr1, key= lambda x : (-x[1], x[2]))
    print(result[:5])    
    


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
    arrays = []  
    print("어레이기존",len(arrays))
    for i in range(5):
        query = Recipe.objects.get(rcp_sno=result[i][0])   
        ckgnm = Recipe.objects.get(rcp_sno=result[i][0]).ckg_nm   
        arrays.append(query)
    print("후",len(arrays))
    
    
    
    
    # samgubsal = Recipe.objects.filter(rcp_sno=result[0][0])
    # for i in range(4):
    #     recipe_list = Recipe.objects.filter(rcp_sno=result[i][0])
    #     samgubsal.union(recipe_list)
        
    #     print(samgubsal,'###############')
    # print(samgubsal)
    
    # recipe_list = samgubsal
    
    # query = str(recipe_list[0].ckg_nm)
    

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
        'q' : ckgnm,
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
            'recipe_list':arrays,
            'user_check':user_check,
            'board_info':board_info,
            # 'arrays' :arrays,
        }

    # context ={
    #     'recipe_list':recipe_list,
    #     'user_check':user_check,
    #     'board_info':board_info,
    # }
        

    return render(request,'ref/searchRecipe.html',context)

