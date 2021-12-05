from django.shortcuts import render
from productos.models import Producto 
def inicio(request):
    productos = Producto.objects.all()
    p1 = Producto.objects.get(id=1)
    print("=============")
    print(p1)
    print(productos.query)
    print("=============")


    usuario = {
        "nombre": "Ezequiel",
        "apellido": "Gómez"
    }
    context = {
        "usuario": usuario,
        "productos": productos
    }
    return render(request, "inicio.html", context)