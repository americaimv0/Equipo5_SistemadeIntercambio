from django.shortcuts import render
def inicio(request):
    return render(request, 'inicio.html')

def datos(request):
    return render(request, 'datos.html')
