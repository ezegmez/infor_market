from django.shortcuts import render
from productos.models import Producto


def inicio(request):
    context = {
        "productos": Producto.objects.all()
    }
    return render(request, "inicio.html", context)


def login(request):
    return render(request, "login.html")

