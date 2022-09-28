from django.shortcuts import render
from .models import Prestamo, Libro
# Create your views here.

def index(request):
    libros = Libro.objects.all()
    context = {
        'libros': libros
    }
    return render(request, 'prestamo/index.html', context)

def detalle(request, libro_id):
    libro = Libro.objects.get(pk=libro_id)
    context = {
        'libro':libro
    }
    return render(request, 'prestamo/detalle.html', context)

def prestar(request, libro_id):
    libroPrestamo = Libro.objects.get(pk=libro_id)

    prestamo = Prestamo()
    prestamo.alumno = request.POST['alumno']
    prestamo.libro = libroPrestamo
    prestamo.save()

    context = {
        'libro': libroPrestamo
    }
    return(render, 'prestamo/detalle.html', context)