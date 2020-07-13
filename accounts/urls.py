from django.contrib import admin
from django.urls import include, path
from . import views 
from django.contrib.auth import views as auth_views
import django.contrib.auth.urls

app_name = 'accounts'

urlpatterns = [
    path('singup/' , views.sing_up , name='singup'),
    path('profile/' , views.profile_information , name='profile'),
    path('profile/edit/' , views.edit_profile , name='edit_profile'),
]
