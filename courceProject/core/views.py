from django.shortcuts import render
from .models import Pessoa

# Create your views here.
def home(request):
    context = {'mensagem':'Ola mundo'}
    return render(request,'core/index.html', context)

def lista_pessoas(request):
    lista = Pessoa.objects.all()
    return render(request, 'core/lista_pessoas.html', {'pessoas':lista})