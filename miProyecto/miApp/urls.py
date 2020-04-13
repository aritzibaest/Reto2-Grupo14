from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name = 'index'),
    path('cliente/<int:cliente_id>',views.cliente, name='detail'),
    path('componente/<int:componente_id>',views.componente, name='detail'),
    path('pedido/<int:pedido_id>',views.pedido, name='detail'),
    path('producto/<int:producto_id>', views.productos, name='detail')
]