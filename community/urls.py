from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import FileDownloadView

app_name = 'community'
urlpatterns = [
    path('community_insert/', views.community_insert),
    path('community_list/', views.community_list.as_view()),
    path('test/<int:post_id>/community_modify/', views.community_modify,name="community_modify"),
    path('test/<int:post_id>/community_delete/', views.community_delete,name="community_delete"),
    path('test/<int:document_id>/',FileDownloadView.as_view(), name="download"),    
    path('test/', views.test),
    path('test2/', views.test2),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)