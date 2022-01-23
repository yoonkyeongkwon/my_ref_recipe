from django.shortcuts import render
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
    def get(self, request, *args, **kwargs):
        # recipe_list = Recipe.objects.all()  ---> 에러남 DB문제
        userref_list = UserRef.objects.all()
        recipe_list = '00'
        request.session['recipe_list'] = recipe_list
        return render(request,'ref/main.html',{'recipe_list':recipe_list,'userref_list':userref_list})
    
    def post(self, request, *args, **kwargs):   
        recipe_list = request.session['recipe_list']
        temp = request.POST.get('material_name')
        new_temp = UserRef()
        new_temp.ingredients = temp
        new_temp.save()
        return render(request, 'ref/main.html', context={'recipe_list': recipe_list, 'new_temp_output': new_temp})
