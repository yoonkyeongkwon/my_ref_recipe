from audioop import reverse
from distutils.command.check import check
from msilib.schema import ListView
from socket import AI_PASSIVE
from typing import Dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from myref import settings
from account.models import Userinfo
from myref.settings import YOUTUBE_DATA_API_KEY
from .models import *
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import requests
from isodate import parse_duration
from account.models import Userinfo
from itertools import *



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
        username= request.session['username']
        uinfo = Userinfo.objects.get(name=username)
        return render(request,'ref/mypage.html',{'uinfo':uinfo})



@csrf_exempt
def searchRecipe(request):
    from collections import defaultdict
    # user_check = request.POST.get('user_like') 
    # board_info = Board.objects.all()
    username= request.session['username']
    cntr=Recipe.objects.all().count()
    cntm=Mine.objects.filter(id=username).count()
    print(cntm)
 

# user의 재료 목록 가져와 일치하는 레시피 정렬
    dic = defaultdict(int)
    for i in range(0,cntm):
        filter_rcp= Recipe.objects.filter(ckg_mtrl_cn__contains=Mine.objects.filter(id=username)[i].ingredients).values('rcp_sno')
        filter_mtrl= Recipe.objects.filter(ckg_mtrl_cn__contains=Mine.objects.filter(id=username)[i].ingredients).values('mtrl_cnt')
        # print("여기",filter_mtrl[0]['mtrl_cnt'])
        
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

    
    arrays,keys_list = [],[]
    for i in range(5):
        query = Recipe.objects.get(rcp_sno=result[i][0])   
        ckgnm = Recipe.objects.get(rcp_sno=result[i][0]).ckg_nm
        keys_list.append(query.rcp_sno)
        arrays.append(query)
  

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
        # print(result['id'])

        videos.append(video_data)

    context ={
        'videos':videos,
        'recipe_list':arrays,
    }
    print("레시피 가져왔어요!")
    request.session["recipe_list"] = keys_list
    return render(request,'ref/recipe.html',context)

    # return render(request,'ref/recipedetail.html',context)


        
class searchRecipeDetail(View):
    # 처음 보이는 화면
    def get(self,request, *args, **kwargs):
        print("가져왔냐? ",request.POST.get("detailViews"),0)
        print("레시피 디테일에서 GET으로 받았다.")
        array = request.session["recipe_list"]
        print("컨텐츠 제발 : ",request.POST.get("content"))
        print("배열 가져왓습니다.", array)
        return render(request,'ref/recipedetail.html')
    
    # 보이는 화면에서 처리할때 결과 나오는것.
    # def post(self,request, *args, **kwargs):
        # print("레시피 디테일에서 POST으로 받았다.")
        # if request.POST.get("bf",0) =="이전으로":
        #     return HttpResponseRedirect(reverse('ref:searchRecipe'))
            
        # if request.POST.get("nxt",0) =="홈으로":
        #     return render(request,'ref/main.html')
    
    
    
class searchRecipeSSS(View):
    # 처음 보이는 화면
    def get(self,request, *args, **kwargs):
        from collections import defaultdict
        # user_check = request.POST.get('user_like') 
        # board_info = Board.objects.all()
        username= request.session['username']
        cntr=Recipe.objects.all().count()
        cntm=Mine.objects.filter(id=username).count()
        print(cntm)
    

    # user의 재료 목록 가져와 일치하는 레시피 정렬
        dic = defaultdict(int)
        for i in range(0,cntm):
            filter_rcp= Recipe.objects.filter(ckg_mtrl_cn__contains=Mine.objects.filter(id=username)[i].ingredients).values('rcp_sno')
            filter_mtrl= Recipe.objects.filter(ckg_mtrl_cn__contains=Mine.objects.filter(id=username)[i].ingredients).values('mtrl_cnt')
            # print("여기",filter_mtrl[0]['mtrl_cnt'])
            
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

        
        arrays,keys_list = [],[]
        for i in range(5):
            query = Recipe.objects.get(rcp_sno=result[i][0])   
            ckgnm = Recipe.objects.get(rcp_sno=result[i][0]).ckg_nm
            keys_list.append(query.rcp_sno)
            arrays.append(query)
    

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
            # print(result['id'])

            videos.append(video_data)

        context ={
            'videos':videos,
            'recipe_list':arrays,
        }
        print("레시피 가져왔어요!")
        request.session["recipe_list"] = keys_list
        return render(request,'ref/recipe.html',context)

    
    # 보이는 화면에서 처리할때 결과 나오는것.
    def post(self,request, *args, **kwargs):
        # print("레시피에서 POST으로 받았다.")
        # print("가져왔냐? ",request.POST.get("detailViews",0))
        print("rcp_sno 가져왔냐? ",request.POST.get("rcp_sno",0))
        # if request.POST.get("detailViews",0) =="자세히":
        #     pass
        # if request.POST.get("next",0) =="다음":
        #     pass
        
        rcp_sno1 = request.POST.get("rcp_sno",0)
        query = Recipe.objects.get(rcp_sno=rcp_sno1)
        
        return render(request,'ref/recipedetail.html', {"query": query })