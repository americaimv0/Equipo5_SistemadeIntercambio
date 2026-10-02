from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html') # O 'practica/inicio.html' según tu estructura

def datos(request):
    return render(request, 'datos.html')

def usuarios(request):
    return render(request, 'usuarios.html')