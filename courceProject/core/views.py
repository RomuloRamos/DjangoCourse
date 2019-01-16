from django.shortcuts import render
from .models import (
    Pessoa,
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista,
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

def lista_mensalistas(request):
    lista = Mensalista.objects.all() #efetua a busca no banco de todos os objetos dessa classe
    return render(request, 'core/lista_mensalistas.html', {'mensalistas':lista})

def lista_movmensalistas(request):
    lista = MovMensalista.objects.all() #efetua a busca no banco de todos os objetos dessa classe
    return render(request, 'core/lista_movmensalistas.html', {'movmensalistas':lista})