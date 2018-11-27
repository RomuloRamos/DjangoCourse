from django.http import HttpResponse

def home(request):
    return HttpResponse('Ola Mundo')

def clientes(request):
    return HttpResponse('Ola Clientes')

def cliente_detalhe(request, id):
    return HttpResponse('Ola Cliente:' + id)

def cliente_nome(request, nome):
    return HttpResponse('Ola Cliente:' + nome)