from django.shortcuts import render
from .models import Componente, Cliente,Productos, Pedido

# Create your views here.
from django.http import HttpResponse

def index(request):
    pedidos = Pedido.objects.order_by('codigo')
    context = {'titulo_pagina':'Lisado de Pedidos','lista_pedidos' : pedidos}
    return render(request, 'departamentos.html', context)

def cliente(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    context = {'titulo_pagina': 'Detalles de cliente', 'cliente': cliente}
    return render(request, 'empleados.html', context)


def componente(request, componente_id):
    componente = Componente.objects.get(pk=componente_id)
    context = {'titulo_pagina': 'Detalles de componente', 'componente': componente}
    return render(request, 'empleados.html', context)

def productos(request, productos_id):
    productos = Productos.objects.get(pk=productos_id)
    context = {'titulo_pagina': 'Detalles de productos', 'productos': productos}
    return render(request, 'empleados.html', context)

def pedido(request, pedido_id):
    pedido = Pedido.objects.get(pk=pedido_id)
    context = {'titulo_pagina': 'Detalles de pedido', 'pedido': pedido}
    return render(request, 'empleados.html', context)
