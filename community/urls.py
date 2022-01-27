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
    path('detail/<int:post_id>/community_modify/', views.community_modify,name="community_modify"),
    path('detail/<int:document_id>/', FileDownloadView.as_view(), name="download"),
    path('test/', views.test),
    path('test2/', views.test2),
    path('test/downloads/<int:id>/', views.downloads, name='downloads'),
    path('detail/', views.detail, name='detail'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)