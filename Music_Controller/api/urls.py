from django.contrib import admin
from django.urls import path, include
from .views import RoomAPIView

urlpatterns = [
    path('home/',RoomAPIView.as_view())
]