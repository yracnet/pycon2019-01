from rest_framework import serializers
from project1.app1.models import Libro
class LibroSerializer (serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ['codigo','autor']
