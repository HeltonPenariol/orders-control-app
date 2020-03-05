from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView, UpdateView
from core.models import *
from core.forms import PedidoForm, StatusPedidoForm
from datetime import datetime, timedelta
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

class PedidoDeliveryCreateView(CreateView):
    raise_exception = True
    form_class = PedidoForm
    template_name = 'criar_pedido_delivery.html'
    success_url = reverse_lazy('pagina_delivery')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        form.save_m2m()
        return redirect('/delivery/pedidos/')

    def get_form_kwargs(self):
        kwargs = super(PedidoDeliveryCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

def listar_pedidos_delivery(request):
    tempo_atual = datetime.now()
    tempo_limite = tempo_atual - timedelta(hours=8)
    pedidos_delivery = Pedido.objects.filter(horario_recebimento__range=(tempo_limite, tempo_atual)).all()
    args = {'pedidos': pedidos_delivery}
    template = 'pedidos_delivery.html'
    return render(request, template, args)

class PedidoDeliveryUpdateView(UpdateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'editar_pedido_delivery.html'
    success_url = reverse_lazy('pagina_delivery')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        form.save_m2m()
        return redirect('/delivery/pedidos/')

    def get_form_kwargs(self):
        kwargs = super(PedidoDeliveryUpdateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

def editar_status_delivery(request, id):
    pedido = Pedido.objects.get(pk=id)
    status_pedido = StatusPedidoForm(request.POST or None, instance=pedido)
    args = {'form': status_pedido}

    if status_pedido.is_valid():
        status_pedido.save()
        return redirect('/delivery/pedidos/')

    template = 'editar_status_delivery.html'
    return render(request, template, args)