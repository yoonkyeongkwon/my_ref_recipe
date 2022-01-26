from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'community'
urlpatterns = [
    path('community/', views.community_list),
    path('community_insert/', views.community_insert),
    path('community_list/', TemplateView.as_view(template_name='community/community_list.html'), name='list'),
    path('community_modify/', views.community_modify),
    path('test/', views.test),
]