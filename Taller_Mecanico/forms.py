from django import forms 
from django.core.validators import MinValueValidator
from .models import Producto, Categoria

class Agregar_Categoria(forms.Form):
    Nombre_Categoria = forms.CharField(max_length=100, label='Ingrese la categoria')


class Agregar_producto(forms.Form):
    nombre = forms.CharField(max_length=100, label='Ingrese el nombre del producto')
    descripcion = forms.CharField(max_length=500, label='Ingrese la descripcion del producto')
    cantidad = forms.IntegerField(label='Ingrese la cantidad del producto')
    precio = forms.DecimalField(max_digits=10, decimal_places=2, label='Ingrese el Precio del producto', validators=[MinValueValidator(0)])
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), label='Seleccione la categoría')
    
    def __init__(self, *args, **kwargs):
        super(Agregar_producto, self).__init__(*args, **kwargs)
        self.fields['categoria'].empty_label = 'Seleccione una categoría'