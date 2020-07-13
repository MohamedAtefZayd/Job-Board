from django.contrib import admin
from django.urls import include, path
from . import views 

app_name = 'contact'

urlpatterns = [
    path('', views.send_email , name='contact' ),
]