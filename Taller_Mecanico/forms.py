from django import forms 
from django.core.validators import MinValueValidator
from .models import Producto, Categoria

class Agregar_Categoria(forms.Form):
    Nombre_Categoria = forms.CharField(max_length=100, label='Ingrese la categoria')


class Agregar_producto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'cantidad', 'precio', 'categoria', 'imagen']

