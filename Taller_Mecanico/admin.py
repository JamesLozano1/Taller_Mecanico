from django.contrib import admin
from .models import Producto, Categoria, Servicios

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Servicios)

# Register your models here.
