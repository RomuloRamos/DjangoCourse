from django.http import HttpResponse
from django.shortcuts import render

def home(request):
#    return HttpResponse('Ola Mundo')
    sexo = 'm'
    nome = 'Alfredo'
    lista = [
        {'nome': 'Pedro', 'sexo': 'm'},
        {'nome': 'Maria', 'sexo': 'f'},
        {'nome': 'Joaquina', 'sexo': 'f'},
        {'nome': 'Joao', 'sexo': 'm'},
    ]
    data = {'nome_da_lista': lista, 'var_sexo':sexo, 'var_nome': nome} #Aqui estou concentrando todos os dados em uma unica variável, para entao passa-la
    return render(request, 'index.html', data)
