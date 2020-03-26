from django.urls import path
from core.views import *
from core.popups import *

urlpatterns = [
    path('', pagina_inicial, name='pagina_inicial'),
    path('delivery/', pagina_delivery, name='pagina_delivery'),
    path('delivery/criar-pedido/', PedidoDeliveryCreateView.as_view(), name='criar_pedido_delivery'),
    path('delivery/pedidos/', listar_pedidos_delivery, name='listar_pedidos_delivery'),
    path('delivery/pedidos/visualizar/<int:id>', visualizar_comanda_delivery, name='visualizar_comanda_delivery'),
    path('delivery/pedidos/editar/<int:pk>', PedidoDeliveryUpdateView.as_view(), name='editar_pedido_delivery'),
    path('delivery/pedidos/status/<int:id>', editar_status_delivery, name='editar_status_delivery'),
    path('delivery/pedidos/deletar/<int:id>', deletar_pedido_delivery, name='deletar_pedido_delivery'),
    path('balcao/', pagina_balcao, name='pagina_balcao'),
    path('balcao/criar-pedido/', PedidoBalcaoCreateView.as_view(), name='criar_pedido_balcao'),
    path('balcao/pedidos/', listar_pedidos_balcao, name='listar_pedidos_balcao'),
    # path('balcao/pedidos/visualizar/<int:id>', visualizar_comanda_balcao, name='visualizar_comanda_balcao'),
    path('balcao/pedidos/editar/<int:pk>', PedidoBalcaoUpdateView.as_view(), name='editar_pedido_balcao'),
    path('balcao/pedidos/status/<int:id>', editar_status_balcao, name='editar_status_balcao'),

    PizzaGrandePopupCRUDViewSet.urls(),
    PizzaBrotoPopupCRUDViewSet.urls(),
    EsfihaPopupCRUDViewSet.urls(),
    LanchePopupCRUDViewSet.urls(),
    SobremesaPopupCRUDViewSet.urls(),
    BebidaPopupCRUDViewSet.urls(),
]