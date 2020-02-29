from django.urls import path
from core.views import *

urlpatterns = [
    path('', pagina_inicial),
    path('delivery/', pagina_delivery, name='pagina_delivery'),
]