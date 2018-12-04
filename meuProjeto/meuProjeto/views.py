from django.http import HttpResponse
from django.shortcuts import render

def home(request):
#    return HttpResponse('Ola Mundo')
    minha_variavel = 'Programe Facil' #Variável a ser enviada para o template (html)
    return render(request, 'index.html', {'nome_que_dei_pra_variavel': minha_variavel})
