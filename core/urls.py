from django.urls import path
from core.views import *

urlpatterns = [
    path('', pagina_inicial),
    path('delivery/criar-pedido/', criar_pedido_delivery),
]