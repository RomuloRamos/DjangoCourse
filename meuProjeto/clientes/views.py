from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def clientes(request):
    return HttpResponse('Ola Clientes')

def cliente_detalhe(request, id):
    return HttpResponse('Ola Cliente:' + id)

def cliente_nome(request, nome):
    return HttpResponse('Ola Cliente:' + nome)