from django.shortcuts import render
<<<<<<< HEAD
from .models import Recipe, UserRef
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
        userref_list = UserRef.objects.all()
        recipe_list = '00'
        request.session['recipe_list'] = recipe_list
        return render(request,'ref/main.html',{'recipe_list':recipe_list,'userref_list':userref_list})
    
    def post(self, request, *args, **kwargs):   
        recipe_list = request.session['recipe_list']
        self.array.append(request.POST.get('material_name'))
        temp = self.array
        new_temp = UserRef()
        new_temp.ingredients = temp
        new_temp.save()

        # new_temp_output = new_temp.objects.all()
        
        return render(request, 'ref/main.html', context={'temp' : temp ,'recipe_list': recipe_list, 'new_temp_output': new_temp})

    def init_var(self):
        self.array = []
        
=======
from .models import Recipe, UserRef, UserCheck, Board
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def main(request):

    recipe_list = Recipe.objects.order_by('rcp_sno')[0:5]
    userref_list = UserRef.objects.all()
    user_check = UserCheck.objects.all()
    board_info = Board.objects.all()

    return render(request,'ref/main.html',{'recipe_list':recipe_list,
                                            'userref_list':userref_list,
                                            'user_check':user_check,
                                            'board_info':board_info})

@csrf_exempt
def searchRecipe(request):

    # 처리 필요
    # 내 냉장고 레시피의 재료들과
    # 레시피 테이블에서의 검색 결과를 조합
    # 내가 가지고 있는 재료들과 완벽히 일치하는 리스트
    # 더보기 에는 추가 재료 필요한 것

    recipe_list = Recipe.objects.all()[0:5]
    userref_list = UserRef.objects.all()

    return render(request,'ref/searchRecipe.html',{'recipe_list':recipe_list})

@csrf_exempt
def moreNeed(request):



    return render(request,'ref/moreNeed.html',{})
>>>>>>> ingre_ui
