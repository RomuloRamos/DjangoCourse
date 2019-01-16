from django.shortcuts import render
from .models import (
    Pessoa,
    Veiculo,
    MovRotativo,
)

# Create your views here.
def home(request):
    context = {'mensagem':'Ola mundo'}
    return render(request,'core/index.html', context)

def lista_pessoas(request):
    lista = Pessoa.objects.all() #efetua a busca no banco de todos os objetos dessa classe
    return render(request, 'core/lista_pessoas.html', {'pessoas':lista})

def lista_veiculos(request):
    lista = Veiculo.objects.all() #efetua a busca no banco de todos os objetos dessa classe
    return render(request, 'core/lista_veiculos.html', {'veiculos':lista})

def lista_movrotativos(request):
    lista = MovRotativo.objects.all() #efetua a busca no banco de todos os objetos dessa classe
    return render(request, 'core/lista_movRotativos.html', {'mov_rot':lista})