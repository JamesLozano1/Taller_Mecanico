from django import forms 
from django.core.validators import MinValueValidator
from .models import Producto, Categoria, Servicios


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class Agregar_producto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class Agregar_Servicios(forms.Form):
    class Meta:
        model = Servicios
        fields = '__all__'