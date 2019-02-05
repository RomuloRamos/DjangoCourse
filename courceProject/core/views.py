from django.shortcuts import render, redirect
from .models import (
    Pessoa,
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista,
)
from .form import PessoaForm, VeiculoForm, MovRotForm, MensalistaForm, MovMensalistasForm


# Create your views here.
def home(request):
    context = {'mensagem':'Ola mundo'}
    return render(request,'core/index.html', context)

def lista_pessoas(request):
    lista = Pessoa.objects.all() #efetua a busca no banco de todos os objetos dessa classe
    form = PessoaForm()
    data = {'pessoas':lista, 'form':form}
    return render(request, 'core/lista_pessoas.html', data)

def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')  

def pessoa_update(request, id):
    data = {} #cria um dicionário
    pessoa = Pessoa.objects.get(id = id) #busca a pessoa que se deseja atualizar no banco, através do ID
    form = PessoaForm(request.POST or None, instance=pessoa) #instancia um formulario, passando a "pessoa" que foi resgatada do banco para que seja preenchido 
    data['pessoa'] = pessoa #insere "pessoa no dicionário"
    data['form'] = form #insere o "form" no dicionário

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update_pessoa.html', data)        


def lista_veiculos(request):
    lista = Veiculo.objects.all() #efetua a busca no banco de todos os objetos dessa classe
    form = VeiculoForm()
    data  = {'veiculos':lista, 'form': form}
    return render(request, 'core/lista_veiculos.html', data)

def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')  

def veiculo_update(request, id):
    data = {} #cria um dicionário
    veiculo = Veiculo.objects.get(id = id) #busca o veiculo que se deseja atualizar no banco, através do ID
    form = VeiculoForm(request.POST or None, instance=veiculo) #instancia um formulario, passando a "pessoa" que foi resgatada do banco para que seja preenchido 
    data['veiculo'] = veiculo #insere "pessoa no dicionário"
    data['form'] = form #insere o "form" no dicionário

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/update_veiculo.html', data)        

def lista_movrotativos(request):
    lista = MovRotativo.objects.all() #efetua a busca no banco de todos os objetos dessa classe
    formulario = MovRotForm()
    data = {'mov_rot':lista, 'form':formulario}
    return render(request, 'core/lista_movRotativos.html',data)

def movrotativos_novo(request):
    form = MovRotForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrot')    

def movRotativos_update(request, id):
    data = {} #cria um dicionário
    movRot = MovRotativo.objects.get(id = id) #busca o veiculo que se deseja atualizar no banco, através do ID
    form = MovRotForm(request.POST or None, instance=movRot) #instancia um formulario, passando a "pessoa" que foi resgatada do banco para que seja preenchido 
    data['movRot'] = movRot #insere "pessoa no dicionário"
    data['form'] = form #insere o "form" no dicionário

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movrot')
    else:
        return render(request, 'core/update_movRot.html', data)        

def lista_mensalistas(request):
    lista = Mensalista.objects.all() #efetua a busca no banco de todos os objetos dessa classe
    form = MensalistaForm()
    data  = {'mensalistas':lista , 'form': form}
    return render(request, 'core/lista_mensalistas.html', data)

def mensalistas_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalistas')
  
def mensalistas_update(request, id):
    data = {} #cria um dicionário
    mensalista = Mensalista.objects.get(id = id) #busca o veiculo que se deseja atualizar no banco, através do ID
    form = MensalistaForm(request.POST or None, instance=mensalista) #instancia um formulario, passando a "pessoa" que foi resgatada do banco para que seja preenchido 
    data['mensalista'] = mensalista #insere "pessoa no dicionário"
    data['form'] = form #insere o "form" no dicionário

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/update_mensalista.html', data)            

def lista_movmensalistas(request):
    lista = MovMensalista.objects.all() #efetua a busca no banco de todos os objetos dessa classe
    form = MovMensalistasForm()
    data = {'movmensalistas':lista , 'form':form}
    return render(request, 'core/lista_movmensalistas.html', data)

def movmensalistas_novo(request):
    form = MovMensalistasForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movmensalistas')

def mov_mensalistas_update(request, id):
    data = {} #cria um dicionário
    mensalista = Mensalista.objects.get(id = id) #busca o veiculo que se deseja atualizar no banco, através do ID
    form = MovMensalistasForm(request.POST or None, instance=mensalista) #instancia um formulario, passando a "pessoa" que foi resgatada do banco para que seja preenchido 
    data['mensalista'] = mensalista #insere "pessoa no dicionário"
    data['form'] = form #insere o "form" no dicionário

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movmensalistas')
    else:
        return render(request, 'core/update_movMensalista.html', data)            