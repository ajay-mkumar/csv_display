from django.urls import path
from . import views

urlpatterns=[
    path('',views.profile_upload,name='profile_upload'),
  
    ]