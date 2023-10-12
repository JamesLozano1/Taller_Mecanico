from django.urls import path, include
from . import views
from .views import CatViewSet, ProViewSet, agregar_categoria
from rest_framework import routers

from django.conf.urls.static import static
from django.conf import settings



router=routers.DefaultRouter()
router.register(prefix='categoria', basename='categoria', viewset=CatViewSet)
router.register(prefix='producto', basename='producto', viewset=ProViewSet)

urlpatterns = [
    path('', views.Inicio, name='home'),
    path('producto/', views.producto, name='producto'),
    path('Agregar_Producto/', views.Añadir_producto, name='Agregar_Producto'),
    path('Agregar_Categoria/', views.agregar_categoria, name='Agregar_Categoria'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('producto/<int:producto_id>/editar/', views.editar_producto, name='editar_producto'),
    path('servicios/', views.Servicio, name='Servicios'),
    path('contacto/', views.contacto, name='contacto'),
    path('rout/', include(router.urls)),
    path('buscar-productos/', views.buscar_productos, name='buscar_productos'),
    path('buscar-productos/', views.buscar_productos_vista, name='buscar_productos_vista'),

    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar_del_carrito/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('ver_carrito/', views.ver_carrito, name='ver_carrito'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)