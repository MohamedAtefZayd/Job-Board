from django.contrib import admin
from django.urls import include, path
from . import views 

app_name = 'jobs'

urlpatterns = [
    path('', views.job_list , name='job_list' ),
    path('jobs/<str:slug>/<int:id>', views.job_detail , name='job_detail' ),
    path('jobs/<str:slug>/<int:id>/apply', views.applyForm , name='applyForm' ),
]