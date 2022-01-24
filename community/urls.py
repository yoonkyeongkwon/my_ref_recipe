from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'community'
urlpatterns = [
    path('community_insert/', views.community_insert),
    path('community_insert/', views.community_list),
    path('list/', TemplateView.as_view(template_name='community/community_list.html')),
]