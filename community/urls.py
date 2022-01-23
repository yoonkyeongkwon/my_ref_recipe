from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('community_list/', views.community_list),
  
]