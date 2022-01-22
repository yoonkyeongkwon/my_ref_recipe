from ref import views as main_views
from django.urls import path

app_name = 'ref'
urlpatterns = [

    path('main/', main_views.main, name='main'),

]