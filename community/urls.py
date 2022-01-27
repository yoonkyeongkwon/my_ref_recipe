from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'community'
urlpatterns = [
    path('community_insert/', views.community_insert),
    path('community_list/', views.community_list.as_view()),
    path('community_modify/', views.community_modify),
    path('test/', views.test),
    path('test2/', views.test2),
]