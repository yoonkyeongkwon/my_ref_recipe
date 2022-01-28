from django.urls import path
# from . import views
from .views import *
from ref import views as main_views

app_name = 'ref'

urlpatterns = [
    path('main/', main_v.as_view(), name='main'),
    path('main/mypage/', myPage.as_view(), name='mypage'),
    path('main/mypageINFO/', myPageEditInfo.as_view(), name='mypageINFO'),
    path('main/searchRecipe/', main_views.searchRecipeSSS.as_view(), name='searchRecipe'),
    path('main/searchRecipe2/', main_views.searchRecipeDetail.as_view(), name='searchRecipe2'),
    path('main/mypage/myboard/',myBoard.as_view(), name='myBoard'),
]
