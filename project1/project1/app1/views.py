from django.shortcuts import render
from rest_framework import viewsets
from project1.app1.models import Libro
from project1.app1.serializers import LibroSerializer
# Create your views here.

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
