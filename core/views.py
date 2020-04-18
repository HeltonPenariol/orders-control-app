from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

from core.models import *
from core.forms import *

from datetime import datetime, timedelta
from random import choice
from decimal import Decimal


def index(request):
    template = 'index.html'
    return render(request, template)

def generate_order_id():
    numbers = '0123456789'
    order_number = ''

    for number in range(4):
        order_number += choice(numbers)
    return order_number

# Orders
def order_page(request):
    new_username =  generate_order_id()
    new_user = User.objects.create_user(new_username)
    new_user.set_password('ceara')
    new_user.save()

    new_user = authenticate(username=new_user.username, password='ceara')
    login(request, new_user)
    print('Authenticated user:', request.user)

    template = 'orders/orders_page.html'
    return render(request, template)

def calculate_subtotal(username):
    total = 0
    for obj in Pizza.objects.filter(adicionado_por=username):
        total += obj.calcular_preco()
    for obj in Esfiha.objects.filter(adicionado_por=username):
        total += obj.calcular_preco()
    for obj in Lanche.objects.filter(adicionado_por=username):
        total += obj.calcular_preco()
    for obj in Pastel.objects.filter(adicionado_por=username):
        total += obj.calcular_preco()
    for obj in Beirute.objects.filter(adicionado_por=username):
        total += obj.calcular_preco()
    for obj in Bolo.objects.filter(adicionado_por=username):
        total += obj.calcular_preco()
    for obj in Bebida.objects.filter(adicionado_por=username):
        total += obj.calcular_preco()
    return total

def new_order(request):
    form_pizza = AddPizzaForm(request.POST or None)
    if form_pizza.is_valid():
        nova_pizza = form_pizza.save(commit=False)
        nova_pizza.adicionado_por = request.user
        nova_pizza.save()
        form_pizza.save_m2m()
        messages.add_message(request, messages.INFO, "Pizza adicionada.")
        form_pizza = AddPizzaForm()

    form_esfiha = AddEsfihaForm(request.POST or None)
    if form_esfiha.is_valid():
        nova_esfiha = form_esfiha.save(commit=False)
        nova_esfiha.adicionado_por = request.user
        nova_esfiha.save()
        messages.add_message(request, messages.INFO, "Esfiha adicionada.")
        form_esfiha = AddEsfihaForm()

    form_lanche = AddLancheForm(request.POST or None)
    if form_lanche.is_valid():
        novo_lanche = form_lanche.save(commit=False)
        novo_lanche.adicionado_por = request.user
        novo_lanche.save()
        messages.add_message(request, messages.INFO, "Lanche adicionado.")
        form_lanche = AddLancheForm()
    
    form_pastel = AddPastelForm(request.POST or None)
    if form_pastel.is_valid():
        novo_pastel = form_pastel.save(commit=False)
        novo_pastel.adicionado_por = request.user
        novo_pastel.save()
        messages.add_message(request, messages.INFO, "Pastel adicionado.")
        form_pastel = AddPastelForm()

    form_beirute = AddBeiruteForm(request.POST or None)
    if form_beirute.is_valid():
        novo_beirute = form_beirute.save(commit=False)
        novo_beirute.adicionado_por = request.user
        novo_beirute.save()
        messages.add_message(request, messages.INFO, "Beirute adicionado.")
        form_beirute = AddBeiruteForm()
    
    form_bolo = AddBoloForm(request.POST or None)
    if form_bolo.is_valid():
        novo_bolo = form_bolo.save(commit=False)
        novo_bolo.adicionado_por = request.user
        novo_bolo.save()
        messages.add_message(request, messages.INFO, "Bolo adicionado.")
        form_bolo = AddBoloForm()

    form_bebida = AddBebidaForm(request.POST or None)
    if form_bebida.is_valid():
        nova_bebida = form_bebida.save(commit=False)
        nova_bebida.adicionado_por = request.user
        nova_bebida.save()
        messages.add_message(request, messages.INFO, "Bebida adicionada.")
        form_bebida = AddBebidaForm()

    pizzas = Pizza.objects.filter(adicionado_por=request.user)
    esfihas = Esfiha.objects.filter(adicionado_por=request.user)
    lanches = Lanche.objects.filter(adicionado_por=request.user)
    pasteis = Pastel.objects.filter(adicionado_por=request.user)
    beirutes = Beirute.objects.filter(adicionado_por=request.user)
    bolos = Bolo.objects.filter(adicionado_por=request.user)
    bebidas = Bebida.objects.filter(adicionado_por=request.user)

    subtotal = Decimal(calculate_subtotal(request.user))

    args = {
        'add_pizza': form_pizza,
        'add_esfiha': form_esfiha,
        'add_lanche': form_lanche,
        'add_pastel': form_pastel,
        'add_beirute' : form_beirute,
        'add_bolo': form_bolo,
        'add_bebida': form_bebida,
        'pizzas': pizzas,
        'esfihas': esfihas,
        'lanches': lanches,
        'pasteis': pasteis,
        'beirutes': beirutes,
        'bolos': bolos,
        'bebidas': bebidas,
        'subtotal': subtotal
    }

    template = 'orders/new_order.html'
    return render(request, template, args)

def finalize_order(request):
    form_pedido = PedidoForm(request.POST or None)
    if form_pedido.is_valid():
        novo_pedido = form_pedido.save(commit=False)
        novo_pedido.numero_identificacao = request.user
        novo_pedido.total = calculate_subtotal(request.user)
        novo_pedido.total -= Decimal(novo_pedido.desconto)
        novo_pedido.total += Decimal(novo_pedido.taxa)
        novo_pedido.total += Decimal(novo_pedido.adicional)
        novo_pedido.save()

        for item in Pizza.objects.filter(adicionado_por=request.user, solicitado=False):
            item.solicitado = True
            item.pedido = novo_pedido
            item.save()

        for item in Esfiha.objects.filter(adicionado_por=request.user, solicitado=False):
            item.solicitado = True
            item.pedido = novo_pedido
            item.save()

        for item in Lanche.objects.filter(adicionado_por=request.user, solicitado=False):
            item.solicitado = True
            item.pedido = novo_pedido
            item.save()

        for item in Pastel.objects.filter(adicionado_por=request.user, solicitado=False):
            item.solicitado = True
            item.pedido = novo_pedido
            item.save()

        for item in Beirute.objects.filter(adicionado_por=request.user, solicitado=False):
            item.solicitado = True
            item.pedido = novo_pedido
            item.save()

        for item in Bolo.objects.filter(adicionado_por=request.user, solicitado=False):
            item.solicitado = True
            item.pedido = novo_pedido
            item.save()

        for item in Bebida.objects.filter(adicionado_por=request.user, solicitado=False):
            item.solicitado = True
            item.pedido = novo_pedido
            item.save()
        
        return redirect('/orders/list/')

    pizzas = Pizza.objects.filter(adicionado_por=request.user)
    esfihas = Esfiha.objects.filter(adicionado_por=request.user)
    lanches = Lanche.objects.filter(adicionado_por=request.user)
    pasteis = Pastel.objects.filter(adicionado_por=request.user)
    beirutes = Beirute.objects.filter(adicionado_por=request.user)
    bolos = Bolo.objects.filter(adicionado_por=request.user)
    bebidas = Bebida.objects.filter(adicionado_por=request.user)

    subtotal = Decimal(calculate_subtotal(request.user))

    args = {
        'form_pedido': form_pedido,
        'pizzas': pizzas,
        'esfihas': esfihas,
        'lanches': lanches,
        'pasteis': pasteis,
        'beirutes': beirutes,
        'bolos': bolos,
        'bebidas': bebidas,
        'subtotal': subtotal
    }
    
    template = 'orders/finalize_order.html'
    return render(request, template, args)

def delete_pizza(request, id):
    pizza = Pizza.objects.get(pk=id)
    pizza.delete()
    messages.add_message(request, messages.SUCCESS, "Pizza removida.")
    same_page = request.META.get('HTTP_REFERER')
    return redirect(same_page)

def delete_esfiha(request, id):
    esfiha = Esfiha.objects.get(pk=id)
    esfiha.delete()
    messages.add_message(request, messages.SUCCESS, "Esfiha removida.")
    same_page = request.META.get('HTTP_REFERER')
    return redirect(same_page)

def delete_lanche(request, id):
    lanche = Lanche.objects.get(pk=id)
    lanche.delete()
    messages.add_message(request, messages.SUCCESS, "Lanche removido.")    
    same_page = request.META.get('HTTP_REFERER')
    return redirect(same_page)

def delete_pastel(request, id):
    pastel = Pastel.objects.get(pk=id)
    pastel.delete()
    messages.add_message(request, messages.SUCCESS, "Pastel removido.")
    same_page = request.META.get('HTTP_REFERER')
    return redirect(same_page)

def delete_beirute(request, id):
    beirute = Beirute.objects.get(pk=id)
    beirute.delete()
    messages.add_message(request, messages.SUCCESS, "Beirute removido.")
    same_page = request.META.get('HTTP_REFERER')
    return redirect(same_page)
    
def delete_bolo(request, id):
    bolo = Bolo.objects.get(pk=id)
    bolo.delete()
    messages.add_message(request, messages.SUCCESS, "Bolo removido.")
    same_page = request.META.get('HTTP_REFERER')
    return redirect(same_page)

def delete_bebida(request, id):
    bebida = Bebida.objects.get(pk=id)
    bebida.delete()
    messages.add_message(request, messages.SUCCESS, "Bebida removida.")
    same_page = request.META.get('HTTP_REFERER')
    return redirect(same_page)

def list_orders(request):
    horario_atual = datetime.now()
    horario_limite = horario_atual - timedelta(hours=8)

    pedidos = Pedido.objects.filter(horario_recebimento__range=(horario_limite, horario_atual)).all()

    pedidos_balcao = Pedido.objects.filter(tipo_pedido="Balcão", horario_recebimento__range=(horario_limite, horario_atual)).count()
    pedidos_delivery = Pedido.objects.filter(tipo_pedido="Delivery", horario_recebimento__range=(horario_limite, horario_atual)).count()

    args = {
        'pedidos': pedidos,
        'pedidos_balcao': pedidos_balcao,
        'pedidos_delivery': pedidos_delivery,
    }

    template = 'orders/list_orders.html'
    return render(request, template, args)

def change_status(request, id):
    pedido = Pedido.objects.get(pk=id)
    status = StatusForm(request.POST or None, instance=pedido)

    if status.is_valid():
        status.save()
        return redirect('/orders/list/')

    args = {
        'pedido': pedido,
        'status': status,
    }

    template = 'orders/change_status.html'
    return render(request, template, args)

def money_received(request, id):
    pedido = Pedido.objects.get(pk=id)
    form = RecebidosForm(request.POST or None, instance=pedido)

    if form.is_valid():
        form.save()
        return redirect('/orders/list/')

    args = {
        'form': form,
        'pedido': pedido,
    }

    template = 'orders/money_received.html'
    return render(request, template, args)

def order_detail(request, id):
    pedido = Pedido.objects.get(pk=id)

    pizzas = pedido.pizzas.all()
    esfihas = pedido.esfihas.all()
    lanches = pedido.lanches.all()
    pasteis = pedido.pasteis.all()
    beirutes = pedido.beirutes.all()
    bolos = pedido.bolos.all()
    bebidas = pedido.bebidas.all()

    args = {
        'pedido': pedido,
        'pizzas': pizzas,
        'esfihas': esfihas,
        'lanches': lanches,
        'pasteis': pasteis,
        'beirutes': beirutes,
        'bolos': bolos,
        'bebidas': bebidas,
    }

    template = 'orders/order_detail.html'
    return render(request, template, args)

def delete_order(request, id):
    pedido = Pedido.objects.get(pk=id)
    pedido.delete()
    
    return redirect('/orders/list/')

def edit_order(request, id):
    pedido = Pedido.objects.get(pk=id)
    usuario = authenticate(username=pedido.numero_identificacao.username, password='ceara')
    login(request, usuario)

    form_pizza = AddPizzaForm(request.POST or None)
    if form_pizza.is_valid():
        nova_pizza = form_pizza.save(commit=False)
        nova_pizza.adicionado_por = request.user
        nova_pizza.save()
        form_pizza.save_m2m()
        messages.add_message(request, messages.INFO, "Pizza adicionada.")
        form_pizza = AddPizzaForm()

    form_esfiha = AddEsfihaForm(request.POST or None)
    if form_esfiha.is_valid():
        nova_esfiha = form_esfiha.save(commit=False)
        nova_esfiha.adicionado_por = request.user
        nova_esfiha.save()
        messages.add_message(request, messages.INFO, "Esfiha adicionada.")
        form_esfiha = AddEsfihaForm()

    form_lanche = AddLancheForm(request.POST or None)
    if form_lanche.is_valid():
        novo_lanche = form_lanche.save(commit=False)
        novo_lanche.adicionado_por = request.user
        novo_lanche.save()
        messages.add_message(request, messages.INFO, "Lanche adicionado.")
        form_lanche = AddLancheForm()
    
    form_pastel = AddPastelForm(request.POST or None)
    if form_pastel.is_valid():
        novo_pastel = form_pastel.save(commit=False)
        novo_pastel.adicionado_por = request.user
        novo_pastel.save()
        messages.add_message(request, messages.INFO, "Pastel adicionado.")
        form_pastel = AddPastelForm()

    form_beirute = AddBeiruteForm(request.POST or None)
    if form_beirute.is_valid():
        novo_beirute = form_beirute.save(commit=False)
        novo_beirute.adicionado_por = request.user
        novo_beirute.save()
        messages.add_message(request, messages.INFO, "Beirute adicionado.")
        form_beirute = AddBeiruteForm()
    
    form_bolo = AddBoloForm(request.POST or None)
    if form_bolo.is_valid():
        novo_bolo = form_bolo.save(commit=False)
        novo_bolo.adicionado_por = request.user
        novo_bolo.save()
        messages.add_message(request, messages.INFO, "Bolo adicionado.")
        form_bolo = AddBoloForm()

    form_bebida = AddBebidaForm(request.POST or None)
    if form_bebida.is_valid():
        nova_bebida = form_bebida.save(commit=False)
        nova_bebida.adicionado_por = request.user
        nova_bebida.save()
        messages.add_message(request, messages.INFO, "Bebida adicionada.")
        form_bebida = AddBebidaForm()

    pizzas = Pizza.objects.filter(adicionado_por=request.user)
    esfihas = Esfiha.objects.filter(adicionado_por=request.user)
    lanches = Lanche.objects.filter(adicionado_por=request.user)
    pasteis = Pastel.objects.filter(adicionado_por=request.user)
    beirutes = Beirute.objects.filter(adicionado_por=request.user)
    bolos = Bolo.objects.filter(adicionado_por=request.user)
    bebidas = Bebida.objects.filter(adicionado_por=request.user)

    subtotal = Decimal(calculate_subtotal(request.user))

    args = {
        'add_pizza': form_pizza,
        'add_esfiha': form_esfiha,
        'add_lanche': form_lanche,
        'add_pastel': form_pastel,
        'add_beirute' : form_beirute,
        'add_bolo': form_bolo,
        'add_bebida': form_bebida,
        'pizzas': pizzas,
        'esfihas': esfihas,
        'lanches': lanches,
        'pasteis': pasteis,
        'beirutes': beirutes,
        'bolos': bolos,
        'bebidas': bebidas,
        'subtotal': subtotal,
        'pedido': pedido,
    }

    template = 'orders/edit_order.html'
    return render(request, template, args)

def finalize_edit(request, id):
    pedido = Pedido.objects.get(pk=id)
    form_pedido = PedidoForm(request.POST or None, instance=pedido)

    if form_pedido.is_valid():
        novo_pedido = form_pedido.save(commit=False)
        novo_pedido.numero_identificacao = request.user
        novo_pedido.total = calculate_subtotal(request.user)
        novo_pedido.total -= Decimal(novo_pedido.desconto)
        novo_pedido.total += Decimal(novo_pedido.taxa)
        novo_pedido.total += Decimal(novo_pedido.adicional)
        novo_pedido.save()

        for item in Pizza.objects.filter(adicionado_por=request.user, solicitado=False):
            item.solicitado = True
            item.pedido = novo_pedido
            item.save()

        for item in Esfiha.objects.filter(adicionado_por=request.user, solicitado=False):
            item.solicitado = True
            item.pedido = novo_pedido
            item.save()

        for item in Lanche.objects.filter(adicionado_por=request.user, solicitado=False):
            item.solicitado = True
            item.pedido = novo_pedido
            item.save()

        for item in Pastel.objects.filter(adicionado_por=request.user, solicitado=False):
            item.solicitado = True
            item.pedido = novo_pedido
            item.save()

        for item in Beirute.objects.filter(adicionado_por=request.user, solicitado=False):
            item.solicitado = True
            item.pedido = novo_pedido
            item.save()

        for item in Bolo.objects.filter(adicionado_por=request.user, solicitado=False):
            item.solicitado = True
            item.pedido = novo_pedido
            item.save()

        for item in Bebida.objects.filter(adicionado_por=request.user, solicitado=False):
            item.solicitado = True
            item.pedido = novo_pedido
            item.save()
        
        return redirect('/orders/list/')

    pizzas = Pizza.objects.filter(adicionado_por=request.user)
    esfihas = Esfiha.objects.filter(adicionado_por=request.user)
    lanches = Lanche.objects.filter(adicionado_por=request.user)
    pasteis = Pastel.objects.filter(adicionado_por=request.user)
    beirutes = Beirute.objects.filter(adicionado_por=request.user)
    bolos = Bolo.objects.filter(adicionado_por=request.user)
    bebidas = Bebida.objects.filter(adicionado_por=request.user)

    subtotal = Decimal(calculate_subtotal(request.user))

    args = {
        'pedido': pedido,
        'form_pedido': form_pedido,
        'pizzas': pizzas,
        'esfihas': esfihas,
        'lanches': lanches,
        'pasteis': pasteis,
        'beirutes': beirutes,
        'bolos': bolos,
        'bebidas': bebidas,
        'subtotal': subtotal
    }
    
    template = 'orders/finalize_edit.html'
    return render(request, template, args)

def order_paper(request, id):
    pedido = Pedido.objects.get(pk=id)

    pizzas = pedido.pizzas.all()
    esfihas = pedido.esfihas.all()
    lanches = pedido.lanches.all()
    pasteis = pedido.pasteis.all()
    beirutes = pedido.beirutes.all()
    bolos = pedido.bolos.all()
    bebidas = pedido.bebidas.all()

    args = {
        'pedido': pedido,
        'pizzas': pizzas,
        'esfihas': esfihas,
        'lanches': lanches,
        'pasteis': pasteis,
        'beirutes': beirutes,
        'bolos': bolos,
        'bebidas': bebidas,
    }
    
    template = 'orders/order_paper.html'
    return render(request, template, args)

def create_costumer(request, id):
    pedido = Pedido.objects.get(pk=id)
    form = ClienteForm(instance=pedido)

    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/costumers/list/')
        
    args = {
        'pedido': pedido,
        'form': form,
    }

    template = 'costumers/create_costumer.html'
    return render(request, template, args)

def edit_costumer(request, id):
    cliente = Cliente.objects.get(pk=id)
    form = ClienteForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('/costumers/list/')

    args = {
        'cliente': cliente,
        'form': form,
    }

    template = 'costumers/edit_costumer.html'
    return render(request, template, args)

def list_costumers(request):
    clientes = Cliente.objects.all()
    numero_clientes = len(clientes)

    args = {
        'clientes': clientes,
        'numero_clientes': numero_clientes,
    }

    template = 'costumers/list_costumers.html'
    return render(request, template, args)

def delete_costumer(request, id):
    cliente = Cliente.objects.get(pk=id)
    cliente.delete()

    return redirect('/costumers/list/')

def total_money():
    horario_atual = datetime.now()
    horario_limite = horario_atual - timedelta(hours=8)

    pedidos_dinheiro = Pedido.objects.filter(horario_recebimento__range=(horario_limite, horario_atual)).all()
    total_dinheiro = 0

    for pedido in pedidos_dinheiro:
        total_dinheiro += pedido.checar_dinheiro()
    
    return total_dinheiro

def total_debit():
    horario_atual = datetime.now()
    horario_limite = horario_atual - timedelta(hours=8)

    pedidos_debito = Pedido.objects.filter(horario_recebimento__range=(horario_limite, horario_atual)).all()
    total_debito = 0

    for pedido in pedidos_debito:
        total_debito += pedido.checar_debito()

    return total_debito

def total_credit():
    horario_atual = datetime.now()
    horario_limite = horario_atual - timedelta(hours=8)

    pedidos_credito = Pedido.objects.filter(horario_recebimento__range=(horario_limite, horario_atual)).all()
    total_credito = 0

    for pedido in pedidos_credito:
        total_credito += pedido.checar_credito()
    
    return total_credito

def total_day():
    total = 0
    total += total_money()
    total += total_debit()
    total += total_credit()

    return total

def accounting(request):
    horario_atual = datetime.now()
    horario_limite = horario_atual - timedelta(hours=8)

    delivery = Pedido.objects.filter(tipo_pedido='Delivery', horario_recebimento__range=(horario_limite, horario_atual)).all()
    balcao = Pedido.objects.filter(tipo_pedido='Balcão', horario_recebimento__range=(horario_limite, horario_atual)).all()

    total_dinheiro = total_money()
    total_debito = total_debit()
    total_credito = total_credit()
    total_dia = total_day()

    data_fechamento = horario_atual - timedelta(hours=4)

    args = {
        'numero_delivery': len(delivery),
        'numero_balcao': len(balcao),
        'total_dinheiro': total_dinheiro,
        'total_debito': total_debito,
        'total_credito': total_credito,
        'total_dia': total_dia,
        'data': data_fechamento,
    }

    template = 'contability/accounting.html'
    return render(request, template, args)
