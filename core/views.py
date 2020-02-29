from django.shortcuts import render

def pagina_inicial(request):
    template = 'index.html'
    return render(request, template)

def criar_pedido_delivery(request):
    template = 'criar_pedido_delivery.html'
    return render(request, template)