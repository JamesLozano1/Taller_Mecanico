from rest_framework import serializers
from .models import Categoria, Producto

class CategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta: 
        model= Producto
        fields = '__all__'