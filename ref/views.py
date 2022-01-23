from django.shortcuts import render
from .models import Recipe, UserRef

# Create your views here.
def main(request):

    recipe_list = Recipe.objects.order_by('rcp_sno')[0:1]
    userref_list = UserRef.objects.all()

    return render(request,'ref/main.html',{'recipe_list':recipe_list,'userref_list':userref_list})

