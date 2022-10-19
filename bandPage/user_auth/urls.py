from django.urls import path, include, re_path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

''' This urls.py script pertains to user_auth pages provides a url to each corresponding view outlined in views.py. '''

app_name = 'user_auth'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': 'login'}, name='logout'),
    path('register/', views.register, name='register'),
]
