from django.urls import path
from core.views import *
from core.popups import PedidoItemPopupCRUDViewSet

urlpatterns = [
    path('', pagina_inicial, name='pagina_inicial'),
    path('delivery/', pagina_delivery, name='pagina_delivery'),
    path('delivery/criar-pedido/', PedidoDelivery.as_view(), name='criar_pedido_delivery'),

    PedidoItemPopupCRUDViewSet.urls(),
]