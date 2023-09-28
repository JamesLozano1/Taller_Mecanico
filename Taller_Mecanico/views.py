from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Producto, Categoria
from .forms import Agregar_producto, Agregar_Categoria
from rest_framework import viewsets
from .serializer import CategoriaProductoSerializer

class CatProViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    # queryset2 = Categoria.objects.all()
    serializer_class = CategoriaProductoSerializer

def Inicio(request):
    titulo = '¡Bienvenido a nuestro Taller!'
    return render(request , 'index.html', {
        'titulo':titulo,
    })
    

def producto( request ):
    titulo = '¡Mostrando Productos!'
    producto = Producto.objects.all()
    return render(request, 'Agregar_Producto/producto.html', {
        'titulo': titulo,
        'productos': producto,
    })

# def Añadir_producto(request):
#     if request.method == 'GET':
#         return render( request, 'Agregar_Producto/Agregar_Producto.html', {
#             'form': Agregar_producto(),
#         })
#     else:
#         form = Agregar_producto(request.POST)
#         if form.is_valid():
#             nombre = form.cleaned_data['nombre']
#             descripcion = form.cleaned_data['descripcion']
#             cantidad = form.cleaned_data['cantidad']
#             precio = form.cleaned_data['precio']
#             categoria = form.cleaned_data['categoria']
#             imagen = form.cleaned_data['imagen']
#             Producto.objects.create(nombre=nombre, descripcion=descripcion, cantidad=cantidad, precio=precio, categoria=categoria, imagen=imagen)
#             return redirect('/producto')

def Añadir_producto(request):
    if request.method == 'POST':
        form = Agregar_producto(request.POST, request.FILES)  # Include request.FILES for file uploads
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
                imagen=imagen,  # Save the image
            )
            return redirect('/producto')
    else:
        form = Agregar_producto()
    
    return render(request, 'Agregar_Producto/Agregar_Producto.html', {
        'form': form,
    })

def crear_categoria(request):
    if request.method == 'GET':
        return render( request, 'Agregar_Producto/Añadir_Categoria.html', {
            'form': Agregar_Categoria(),
        })
    else:
        form = Agregar_Categoria(request.POST)
        if form.is_valid():
            Nombre_Categoria = form.cleaned_data['Nombre_Categoria']
            Categoria.objects.create(Nombre_Categoria=Nombre_Categoria)
            return redirect('/producto')

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'Agregar_Producto/detalle_producto.html', {'producto': producto})

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)

    if request.method == 'POST':
        form = Agregar_producto(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto')  # Redirige a la lista de productos después de guardar
    else:
        form = Agregar_producto(instance=producto)

    return render(request, 'Agregar_Producto/editar_producto.html', {
        'form': form
    })


# def editar_producto(request, producto_id):
#     producto = get_object_or_404(Producto, pk=producto_id)

#     if request.method == 'POST':
#         form = Agregar_producto(request.POST, instance=producto)
#         if form.is_valid():
#             form.save()
#             return redirect('producto')  # Redirige a la lista de productos después de guardar
#     else:
#         form = Agregar_producto(instance=producto)

#     return render(request, 'Agregar_Producto/editar_producto.html', {'form': form})


