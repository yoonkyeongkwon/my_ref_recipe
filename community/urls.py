from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'community'
urlpatterns = [
    path('community_insert/', views.community_insert),
    path('community_list/', views.community_list.as_view()),
    path('test/<int:post_id>/community_modify/', views.community_modify,name="community_modify"),
    path('test/<int:post_id>/community_delete/', views.community_delete,name="community_delete"),
    path('test/', views.test),
]