from audioop import reverse
from distutils.command.check import check
from msilib.schema import ListView
from socket import AI_PASSIVE
from typing import Dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from myref import settings
from account.models import Userinfo
from .models import *
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import requests
from isodate import parse_duration
from account.models import Userinfo
from itertools import *
from django.shortcuts import get_object_or_404

class main_v(View):
    array = []
    current_ingred = []       
    def get(self, request, *args, **kwargs):
        star = Recipe.objects.order_by('-inq_cnt')[0:10]
        recipe_list = Recipe.objects.all()
        userref_list = Mine.objects.all()
        return render(request,'ref/main.html',{'recipe_list':recipe_list,'userref_list':userref_list, 'star':star})
    
    def post(self, request, *args, **kwargs):
        try:
            username= request.session['username']    
        except KeyError as e:
            return render(request, 'ref/main.html')
        star = Recipe.objects.order_by('-inq_cnt')[0:10]
        mn = request.POST.get('material_name')
        if mn == '':
            return render(request, 'ref/main.html')
        ed = request.POST.get('expire_date')
        
        self.array =[]
        ingred = Mine.objects.filter(id=username)
        for i in range(len(ingred)):
            self.array.append(ingred[i].ingredients)
        temp = mn
        new_temp = Mine()
        if str(mn) not in self.array:
            self.array.append(mn)
            new_temp.ingredients = temp
            if ed != "":
                new_temp.expiry_date = ed
            new_temp.id = username
            new_temp.save()
        
        return render(request, 'ref/main.html', context={'array' : self.array, 'star':star})

class myPage(View):
    def get(self, request, *args, **kwargs):
        username= request.session['username']
        uinfo = Userinfo.objects.get(name=username)
        return render(request,'ref/mypage.html',{'uinfo':uinfo})
    
    def post(self, request, *args, **kwargs):
        uuu = Userinfo.objects.get(name=request.session["username"])
        return render(request,'ref/editMyinfo.html',{'uinfo':uuu})

class myPageEditInfo(View):
    def get(self, request, *args, **kwargs):
        username= request.session['username']
        uinfo = Userinfo.objects.get(name=username)
        return render(request,'ref/editMyinfo.html',{'uinfo':uinfo})
    
    def post(self, request, *args, **kwargs):
        uuu = Userinfo.objects.get(name=request.session["username"])
        uuu.password = request.POST.get("PW", uuu.password)
        uuu.last_name = request.POST.get("NICK")
        uuu.email = request.POST.get("email")
        return render(request,'ref/mypage.html',{'uinfo':uuu})

        
class searchRecipeDetail(View):
    def get(self,request, *args, **kwargs):
        array = request.session["recipe_list"]
        return render(request,'ref/recipedetail.html')
    
    
class searchRecipeSSS(View):
    def get(self,request, *args, **kwargs):
        from collections import defaultdict
        username= request.session['username']
        cntr=Recipe.objects.all().count()
        cntm=Mine.objects.filter(id=username).count()
        if cntm == 0:
            return render(request,'ref/main.html')

    # user의 재료 목록 가져와 일치하는 레시피 정렬
        dic = defaultdict(int)
        for i in range(0,cntm):
            filter_rcp= Recipe.objects.filter(ckg_mtrl_cn__contains=Mine.objects.filter(id=username)[i].ingredients).values('rcp_sno')
            filter_mtrl= Recipe.objects.filter(ckg_mtrl_cn__contains=Mine.objects.filter(id=username)[i].ingredients).values('mtrl_cnt')
            
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
        for i in range(12):
            query = Recipe.objects.get(rcp_sno=result[i][0])   
            keys_list.append(query.rcp_sno)
            arrays.append(query)
        request.session["recipe_list"] = keys_list
        return render(request,'ref/recipe.html',{'recipe_list':arrays})

    # 보이는 화면에서 처리할때 결과 나오는것.
    def post(self,request, *args, **kwargs):
        rcp_sno1 = request.POST.get("rcp_sno",0)
        query = Recipe.objects.get(rcp_sno=rcp_sno1)
        return render(request,'ref/recipedetail.html', {"query": query})
