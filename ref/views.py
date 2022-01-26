from distutils.command.check import check
from msilib.schema import ListView
from socket import AI_PASSIVE
from django.http import HttpResponse
from django.shortcuts import render
from myref import settings
from account.models import Userinfo
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
        
class main_v(View):
    array =[]        
    def get(self, request, *args, **kwargs):
        star = Recipe.objects.order_by('-inq_cnt')[0:10]
        # recipe_list = Recipe.objects.all()[0]
        userref_list = Mine.objects.all()
        recipe_list = '00'
        # # request.session['recipe_list'] = star
        return render(request,'ref/main.html',{'recipe_list':recipe_list,'userref_list':userref_list, 'star':star})
    
    def post(self, request, *args, **kwargs):   
        # recipe_list = request.session['recipe_list']
        self.array.append(request.POST.get('material_name'))
        username= request.session['username']
        temp = self.array
        new_temp = Mine()
        new_temp.ingredients = temp
        new_temp.username = username
        new_temp.id = 1234
        new_temp.save()
        # new_temp_output = new_temp.objects.all()
        
        return render(request, 'ref/main.html', context={'temp' : temp, 'new_temp' : new_temp})

class myPage(View):
    def get(self, request, *args, **kwargs):
        # nickname = Userinfo.objects.get(username=self.user.username)
        username= request.session['username']
        uinfo = Userinfo.objects.get(name=username)
        return render(request,'ref/mypage.html',{'uinfo':uinfo})
    
    # def post(self, request, *args, **kwargs):   
    #     recipe_list = request.session['recipe_list']
    #     self.array.append(request.POST.get('material_name'))
    #     temp = self.array
    #     new_temp = Mine()
    #     new_temp.ingredients = temp
    #     new_temp.save()
    #     # new_temp_output = new_temp.objects.all()
        
    #     return render(request, 'ref/main.html', context={'temp' : temp ,'recipe_list': recipe_list, 'new_temp_output': new_temp})



# def myPage(request):
#     return render(request, 'ref/mypage.html', {})


        
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

    

    ## 내 재료안에 있는 모든걸 레시피에 검색
    cnt = count(Mine.objects.all)
    myingre = ""

    num = 0
    for mine in Mine.objects.all():
        myingre = str(Mine.ingredients)
        while(num<cnt-1):

            num += 1
        
    #     myingre += str(mine.ingredients)+'|'
    # myingre.split

    recipe_list = Recipe.objects.all()[0:10]
    
    
    




    search_url = 'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'
    search_params = {
        'part' : 'snippet',
        'q' : '검색바꾼결과',
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
        print(result['id'],'###################################')

        videos.append(video_data)

        context ={
            'videos': videos,
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
    




@csrf_exempt
def moreNeed(request):
    if request.method == 'POST':







        return 

    else:
        
        return render(request,'ref/moreNeed.html',{})

