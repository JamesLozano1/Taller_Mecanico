from django import forms 
from django.core.validators import MinValueValidator
from .models import Producto, Categoria, Servicios


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class Agregar_producto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'cantidad', 'precio', 'categoria', 'imagen']

class Agregar_Servicios(forms.Form):
    class Meta:
        model = Servicios
        fields = '__all__'