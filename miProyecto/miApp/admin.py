from django.contrib import admin
from .models import Cliente, Componente, Pedido, Productos

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Componente)
admin.site.register(Productos)
admin.site.register(Pedido)

