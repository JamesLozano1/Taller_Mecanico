from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Producto, Categoria
from .forms import Agregar_producto, Agregar_Categoria

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
        'producto': producto,
    })

def Añadir_producto(request):
    if request.method == 'GET':
        return render( request, 'Agregar_Producto/Agregar_Producto.html', {
            'form': Agregar_producto(),
        })
    else:
        form = Agregar_producto(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            descripcion = form.cleaned_data['descripcion']
            cantidad = form.cleaned_data['cantidad']
            precio = form.cleaned_data['precio']
            categoria = form.cleaned_data['categoria']
            Producto.objects.create(nombre=nombre, descripcion=descripcion, cantidad=cantidad, precio=precio, categoria=categoria)
            return redirect('/producto')

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



def Ver_Informacion():
    producto = Producto.objects.all()
