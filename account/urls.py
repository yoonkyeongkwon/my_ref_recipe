from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'
urlpatterns = [
    path('home/signup/', views.signup, name='signup'),
    path('home/login/', views.login, name='login'),
    path('home/logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),

    
    path('signup/custom/', views.signup_custom, name='signup_custom'),
    path('logout/custom/', views.logout_custom, name='logout_custom'),
    path('login/custom/', views.login_custom, name='login_custom'),
    path('login/test/', auth_views.LoginView.as_view(
            template_name='account/login_test.html'), name='login_test'),

]