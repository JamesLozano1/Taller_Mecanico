from django.urls import path
from . import views

urlpatterns = [
    path('', views.Inicio, name='home'),
    path('producto/', views.producto, name='producto'),
    path('Agregar_Producto/', views.Añadir_producto, name='Agregar_Producto'),
    path('Agregar_Categoria/', views.crear_categoria, name='Agregar_Categoria')
]