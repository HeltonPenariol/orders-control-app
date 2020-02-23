from django.shortcuts import render

def pagina_inicial(request):
    template = 'index.html'
    return render(request, template)
