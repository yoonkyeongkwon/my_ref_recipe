from django.shortcuts import render
from .models import Recipe

# Create your views here.
def main(request):

    recipe_list = Recipe.objects.all()

    return render(request,'ref/main.html',{'recipe_list':recipe_list})
