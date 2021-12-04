# Cuando hacemos ENTER, estamos generando una petición. Eso es lo que recibe en parametro, una request es una petición.
from django.shortcuts import render

def inicio(request):
    # Renderizamos un templete
    return render(request, "inicio.html")