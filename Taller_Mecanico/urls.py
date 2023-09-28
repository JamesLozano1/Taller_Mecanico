from django.urls import path, include
from . import views
from rest_framework import routers

from django.conf.urls.static import static
from django.conf import settings



router=routers.DefaultRouter()
router.register(r'Documentacion', views.CatProViewSet)

urlpatterns = [
    path('', views.Inicio, name='home'),
    path('producto/', views.producto, name='producto'),
    path('Agregar_Producto/', views.Añadir_producto, name='Agregar_Producto'),
    path('Agregar_Categoria/', views.crear_categoria, name='Agregar_Categoria'),
    # path('<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('producto/<int:producto_id>/editar/', views.editar_producto, name='editar_producto'),
    path('rout/', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)