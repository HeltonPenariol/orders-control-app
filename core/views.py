from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView, UpdateView
from core.models import *
from core.forms import *
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
    template = 'delivery/delivery.html'
    return render(request, template, args)

class PedidoDeliveryCreateView(CreateView):
    raise_exception = True
    form_class = PedidoForm
    template_name = 'delivery/criar_pedido_delivery.html'
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
    template = 'delivery/pedidos_delivery.html'
    return render(request, template, args)

def visualizar_comanda_delivery(request, id):
    comanda = Pedido.objects.get(pk=id)
    args = {'comanda':comanda}
    template = 'delivery/visualizar_comanda_delivery.html'
    return render(request, template, args)

class PedidoDeliveryUpdateView(UpdateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'delivery/editar_pedido_delivery.html'
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
    args = {
        'form': status_pedido,
        'pedido': pedido,
    }

    if status_pedido.is_valid():
        status_pedido.save()
        return redirect('/delivery/pedidos/')

    template = 'delivery/editar_status_delivery.html'
    return render(request, template, args)

def deletar_pedido_delivery(request, id):
    pedido = Pedido.objects.get(pk=id)
    pedido.delete()
    return redirect('/delivery/pedidos/')

def cadastrar_cliente(request, id):
    instance = get_object_or_404(Pedido, id=id)
    form = ClienteForm(instance=instance)

    args = {
        'form': form,
        'instance': instance
    }

    template = 'delivery/cadastrar_cliente.html'

    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/delivery/pedidos/')

    return render(request, template, args)

def pagina_balcao(request):
    novo_username = gerar_numeros(4)
    novo_usuario = User.objects.create_user(novo_username)
    novo_usuario.set_password('ceara')
    novo_usuario.save()

    novo_usuario = authenticate(username=novo_usuario.username, password='ceara')
    login(request, novo_usuario)

    args = {'usuario': novo_usuario}
    template = 'balcao/balcao.html'
    return render(request, template, args)

class PedidoBalcaoCreateView(CreateView):
    raise_exception = True
    form_class = PedidoBalcaoForm
    template_name = 'balcao/criar_pedido_balcao.html'
    success_url = reverse_lazy('pagina_balcao')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        form.save_m2m()
        return redirect('/balcao/pedidos/')

    def get_form_kwargs(self):
        kwargs = super(PedidoBalcaoCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

def listar_pedidos_balcao(request):
    tempo_atual = datetime.now()
    tempo_limite = tempo_atual - timedelta(hours=8)
    pedidos_balcao= PedidoBalcao.objects.filter(horario_recebimento__range=(tempo_limite, tempo_atual)).all()
    args = {'pedidos': pedidos_balcao}
    template = 'balcao/pedidos_balcao.html'
    return render(request, template, args)

def visualizar_comanda_balcao(request, id):
    comanda = PedidoBalcao.objects.get(pk=id)
    args = {'comanda':comanda}
    template = 'balcao/visualizar_comanda_balcao.html'
    return render(request, template, args)

class PedidoBalcaoUpdateView(UpdateView):
    model = PedidoBalcao
    form_class = PedidoBalcaoForm
    template_name = 'balcao/editar_pedido_balcao.html'
    success_url = reverse_lazy('pagina_balcao')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        form.save_m2m()
        return redirect('/balcao/pedidos/')

    def get_form_kwargs(self):
        kwargs = super(PedidoBalcaoUpdateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

def editar_status_balcao(request, id):
    pedido = PedidoBalcao.objects.get(pk=id)
    status_pedido = StatusPedidoBalcaoForm(request.POST or None, instance=pedido)
    args = {
        'form': status_pedido,
        'pedido': pedido,
    }

    if status_pedido.is_valid():
        status_pedido.save()
        return redirect('/balcao/pedidos/')

    template = 'balcao/editar_status_balcao.html'
    return render(request, template, args)

def deletar_pedido_balcao(request, id):
    pedido = PedidoBalcao.objects.get(pk=id)
    pedido.delete()
    return redirect('/balcao/pedidos/')