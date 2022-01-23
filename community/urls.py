from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('community_insert/', views.community_insert),
  
]