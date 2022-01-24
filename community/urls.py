from django.urls import path
from . import views
from .views import * 
app_name = 'community'
urlpatterns = [
    path('community_insert/', views.community_insert),
]