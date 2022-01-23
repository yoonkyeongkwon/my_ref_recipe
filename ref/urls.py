from ref import views as main_views
from django.urls import path

app_name = 'ref'
urlpatterns = [

    path('main/', main_views.main, name='main'),
    path('main/searchRecipe/', main_views.searchRecipe, name='searchRecipe'),
    path('main/searchRecipe/moreNeed/', main_views.moreNeed, name='moreNeed'),

]