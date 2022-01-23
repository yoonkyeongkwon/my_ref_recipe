from django.shortcuts import render
from .models import Recipe, UserRef
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def main(request):

    recipe_list = Recipe.objects.order_by('rcp_sno')[0:5]
    userref_list = UserRef.objects.all()

    return render(request,'ref/main.html',{'recipe_list':recipe_list,'userref_list':userref_list})

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
