from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from project1.app1 import views;

router = routers.DefaultRouter()
router.register('libro', views.LibroViewSet)

urlpatterns = [
    path('', include(router.urls))
]