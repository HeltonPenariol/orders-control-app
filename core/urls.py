from django.urls import path
from core.views import *

urlpatterns = [
    path('', index),
    path('orders/', order_page),
    path('orders/new/', new_order),
    path('orders/finalize/', finalize_order),
    path('orders/list/', list_orders),
    path('orders/status/<int:id>', change_status),
    path('orders/money-received/<int:id>', money_received),
    path('orders/detail/<int:id>', order_detail),
    path('orders/delete/<int:id>', delete_order),
    path('orders/edit/<int:id>', edit_order),
    path('orders/edit/finalize/<int:id>', finalize_edit),
    path('orders/order-paper/<int:id>', order_paper),
    path('orders/delete-pizza/<int:id>', delete_pizza),
    path('orders/delete-esfiha/<int:id>', delete_esfiha),
    path('orders/delete-lanche/<int:id>', delete_lanche),
    path('orders/delete-pastel/<int:id>', delete_pastel),
    path('orders/delete-beirute/<int:id>', delete_beirute),
    path('orders/delete-bolo/<int:id>', delete_bolo),
    path('orders/delete-bebida/<int:id>', delete_bebida),
    path('costumers/create/<int:id>', create_costumer),
    path('costumers/edit/<int:id>', edit_costumer),
    path('costumers/list/', list_costumers),
    path('costumers/delete/<int:id>', delete_costumer),
    path('contability/', accounting),
]