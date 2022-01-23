from django.urls import path
from . import views
from .views import *
app_name = 'ref'
urlpatterns = [

    path('main/', main_view.as_view(), name='main'),
    # path('material/', main_views.material, name='material'),

]