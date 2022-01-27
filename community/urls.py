from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'community'
urlpatterns = [
    path('community_insert/', views.community_insert),
    path('community_list/', views.community_list.as_view()),
    path('community_modify/', views.community_modify),
    path('test/', views.test),
    path('test2/', views.test2),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)