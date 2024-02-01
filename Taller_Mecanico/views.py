from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .models import Producto, Categoria, Servicios
from .forms import Agregar_producto, CategoriaForm, Agregar_Servicios
from rest_framework import viewsets
from .serializer import ProductoSerializer, CategoriaSerializers
from django.contrib import messages
from collections import Counter

def buscar_productos_vista(request):
    query = request.GET.get('q', '')  
    productos = Producto.objects.filter(nombre__icontains=query)  
    return render(request, 'Agregar_Producto/producto.html', {'productos': productos})

def buscar_productos(request):
    query = request.GET.get('q', '')  
    productos = Producto.objects.filter(nombre__icontains=query) 
    return render(request, 'Agregar_Producto/productos_table.html', {'productos': productos})

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)

    carrito = request.COOKIES.get('carrito')
    if carrito:
        carrito = carrito.split(',')
    else:
        carrito = []

    carrito.append(str(producto_id))

    response = redirect('detalle_producto', producto_id=producto_id)
    response.set_cookie('carrito', ','.join(carrito))

    return response

def eliminar_del_carrito(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)

    carrito = request.COOKIES.get('carrito')
    if carrito:
        carrito = carrito.split(',')
    else:
        carrito = []

    if str(producto_id) in carrito:
        carrito.remove(str(producto_id))

    response = redirect('ver_carrito')
    response.set_cookie('carrito', ','.join(carrito))

    return response

def ver_carrito(request):
    carrito = request.COOKIES.get('carrito')
    productos_en_carrito = []
    productos = Producto.objects.all()

    if carrito:
        carrito = carrito.split(',')
        carrito_count = Counter(carrito)  
        producto_ids = carrito_count.keys()
        productos = Producto.objects.filter(id__in=producto_ids)

        for producto in productos:
            cantidad = carrito_count[str(producto.id)]  # Obtenemos la cantidad de este producto
            productos_en_carrito.append({'producto': producto, 'cantidad': cantidad})

    return render(request, 'carrito.html', {
        'productos_en_carrito': productos_en_carrito,
        'producto':productos,

    })




def contacto(request):
    return render(request, 'Agregar_Producto/Contacto.html')

def Servicio(request):
    servicio = Servicios.objects.all()
    return render(request, 'Agregar_Producto/servicios.html', {
        'servicio': servicio,
    })

class ProViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class CatViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializers

def Inicio(request):
    titulo = '¡Bienvenido a nuestro Taller!'
    return render(request , 'index.html', {
        'titulo':titulo,
    })

def producto(request):
    titulo = '¡Mostrando Productos!'
    vista = request.GET.get('vista', None) 

    if vista == 'tabla':
        productos = Producto.objects.all()
        return render(request, 'Agregar_Producto/productos_table.html', {
            'titulo': titulo,
            'productos': productos,
        })
    else:
        productos = Producto.objects.all()
        return render(request, 'Agregar_Producto/producto.html', {
            'titulo': titulo,
            'productos': productos,
        })



def Añadir_producto(request):
    if request.method == 'POST':
        form = Agregar_producto(request.POST, request.FILES)  
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            descripcion = form.cleaned_data['descripcion']
            cantidad = form.cleaned_data['cantidad']
            precio = form.cleaned_data['precio']
            categoria = form.cleaned_data['categoria']
            imagen = form.cleaned_data['imagen']
            Producto.objects.create(
                nombre=nombre,
                descripcion=descripcion,
                cantidad=cantidad,
                precio=precio,
                categoria=categoria,
                imagen=imagen,  
            )
            return redirect('/producto')
    else:
        form = Agregar_producto()
    
    return render(request, 'Agregar_Producto/Agregar_Producto.html', {
        'form': form,
    })

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/productos')  
    else:
        form = CategoriaForm()
    
    return render(request, 'Agregar_Producto/Añadir_Categoria.html', {'form': form})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'Agregar_Producto/detalle_producto.html', {'producto': producto})

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)

    if request.method == 'POST':
        form = Agregar_producto(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto')  
    else:
        form = Agregar_producto(instance=producto)

    return render(request, 'productos/editar_producto.html', {
        'form': form
    })

