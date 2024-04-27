from rest_framework import serializers
from .models import Categoria, Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta: 
        model= Producto
        fields = '__all__'


class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'