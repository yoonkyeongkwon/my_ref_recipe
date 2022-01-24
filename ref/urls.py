from django.urls import path
from . import views
from .views import *
from ref import views as main_views

app_name = 'ref'
urlpatterns = [

    path('main/', main_view.as_view(), name='main'),
    # path('material/', main_views.material, name='material'),




    path('main/', main_views.main, name='main'),
    path('main/searchRecipe/', main_views.searchRecipe, name='searchRecipe'),
    path('main/searchRecipe/moreNeed/', main_views.moreNeed, name='moreNeed'),
]
