from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
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

def pagina_delivery(request):
    novo_username = gerar_numeros(4)
    novo_usuario = User.objects.create_user(novo_username)
    novo_usuario.set_password('ceara')
    novo_usuario.save()

    novo_usuario = authenticate(username=novo_usuario.username, password='ceara')
    login(request, novo_usuario)

    args = {'usuario': novo_usuario}
    template = 'delivery.html'
    return render(request, template, args)

class PedidoDelivery(CreateView):
    raise_exception = True
    form_class = PedidoForm
    template_name = 'criar_pedido_delivery.html'
    success_url = reverse_lazy('pagina_delivery')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect('/')

    def get_form_kwargs(self):
        kwargs = super(PedidoDelivery, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs