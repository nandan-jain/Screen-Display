from django.urls import path,include
from .import views

urlpatterns = [    
    
    path('index/', views.index, name='index'),
    path('video_feed/', views.video_feed, name='video_feed'),
]
