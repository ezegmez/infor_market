from django.shortcuts import render
from productos.models import Producto 
def inicio(request):
    productos = Producto.objects.all()
    usuario = {
        "nombre": "Ezequiel",
        "apellido": "Gómez"
    }
    context = {
        "usuario": usuario,
        "productos": productos
    }
    return render(request, "inicio.html", context)

def login(request):
    print(request.GET.get("username"))
    return render(request, "login.html")