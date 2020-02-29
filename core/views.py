from django.shortcuts import render
from django.contrib.auth import authenticate, login
from core.models import *
from core.forms import PedidoForm
from random import choice

def pagina_inicial(request):
    template = 'index.html'
    return render(request, template)

def gerar_numeros(tamanho):
    numeros = '0123456789'
    numero_pedido = ''

    for numero in range(tamanho):
        numero_pedido += choice(numeros)
    return numero_pedido

def criar_pedido_delivery(request):
    novo_username = gerar_numeros(4)
    novo_usuario = User.objects.create_user(novo_username)
    novo_usuario.set_password('ceara')
    novo_usuario.save()

    novo_usuario = authenticate(username=novo_usuario.username, password='ceara')
    login(request, novo_usuario)

    novo_pedido = PedidoForm(request.POST or None)

    args = {
        'usuario': novo_usuario,
        'form': novo_pedido,
    }
    template = 'criar_pedido_delivery.html'
    return render(request, template, args)