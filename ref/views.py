from distutils.command.check import check
from msilib.schema import ListView
from socket import AI_PASSIVE
from django.http import HttpResponse
from django.shortcuts import render
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
    def __init__(self) -> None:
        super().__init__()
        self.array = []
        
    def get(self, request, *args, **kwargs):
        # recipe_list = Recipe.objects.all()[0]
        userref_list = Mine.objects.all()
        recipe_list = '00'
        request.session['recipe_list'] = recipe_list
        return render(request,'ref/main.html',{'recipe_list':recipe_list,'userref_list':userref_list})
    
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

# Create your views here.
@csrf_exempt
def main(request):

    recipe_list = Recipe.objects.order_by('rcp_sno')[0:5]
    userref_list = Mine.objects.all()

    return render(request,'ref/main.html',{'recipe_list':recipe_list,
                                            'userref_list':userref_list,})

@csrf_exempt
def searchRecipe(request):

    user_check = request.POST.get('user_like') 
    board_info = Board.objects.all()
    recipe_list = Recipe.objects.all()[0:5]
    
    return render(request,'ref/searchRecipe.html',{'recipe_list':recipe_list,
                                                    'user_check':user_check,
                                                    'board_info':board_info,})
    

from django.views.generic import ListView as genlistview ,CreateView,DeleteView,DetailView,UpdateView
from .forms import ViedoForm
from .models import Video

class VideoListView(genlistview):
    model = Video
    # 페이지
    



class VideoCreateView(CreateView):
    model = Video
    form_class = ViedoForm
    template_name = 'youtube.html'


class VideoDetailView(DetailView):
    model = Video

class ViedoUpdateView(UpdateView):
    model = Video
    form_class = ViedoForm
    template_name = 'youtube.html'

class VideoDeleteView(DeleteView):
    model = Video


















@csrf_exempt
def moreNeed(request):
    if request.method == 'POST':







        return 

    else:
        
        return render(request,'ref/moreNeed.html',{})

