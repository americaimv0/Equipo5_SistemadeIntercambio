from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html') # O 'practica/inicio.html' según tu estructura

def Donacion(request):
    return render(request, 'Donacion.html')

def Intercambio(request):
    return render(request, 'Intercambio.html')

def Prestamo(request):
    return render(request, 'Prestamo.html')