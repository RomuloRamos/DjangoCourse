from django.shortcuts import render, redirect
from .models import (
    Pessoa,
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista,
)
from .form import PessoaForm, VeiculoForm, MovRotForm, MensalistaForm, movMensalistasForm


# Create your views here.
def home(request):
    context = {'mensagem':'Ola mundo'}
    return render(request,'core/index.html', context)

def pessoa_lista(request):
    lista = Pessoa.objects.all() #efetua a busca no banco de todos os objetos dessa classe
    form = PessoaForm()
    data = {'pessoas':lista, 'form':form}
    return render(request, 'core/pessoa_lista.html', data)

def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_pessoa_lista')  

def pessoa_update(request, id):
    data = {} #cria um dicionário
    pessoa = Pessoa.objects.get(id = id) #busca a pessoa que se deseja atualizar no banco, através do ID
    form = PessoaForm(request.POST or None, instance=pessoa) #instancia um formulario, passando a "pessoa" que foi resgatada do banco para que seja preenchido 
    data['pessoa'] = pessoa #insere "pessoa no dicionário"
    data['form'] = form #insere o "form" no dicionário

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_pessoa_lista')
    else:
        return render(request, 'core/pessoa_update.html', data)        

def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id = id)
    
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_pessoa_lista')   
    else:
        return render(request, 'core/pessoa_delete.html', {'pessoa':pessoa})  

def veiculo_lista(request):
    lista = Veiculo.objects.all() #efetua a busca no banco de todos os objetos dessa classe
    form = VeiculoForm()
    data  = {'veiculos':lista, 'form': form}
    return render(request, 'core/veiculo_lista.html', data)

def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_veiculo_lista')  

def veiculo_update(request, id):
    data = {} #cria um dicionário
    veiculo = Veiculo.objects.get(id = id) #busca o veiculo que se deseja atualizar no banco, através do ID
    form = VeiculoForm(request.POST or None, instance=veiculo) #instancia um formulario, passando a "pessoa" que foi resgatada do banco para que seja preenchido 
    data['veiculo'] = veiculo #insere "pessoa no dicionário"
    data['form'] = form #insere o "form" no dicionário

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_veiculo_lista')
    else:
        return render(request, 'core/veiculo_update.html', data)        

def movRotativos_lista(request):
    lista = MovRotativo.objects.all() #efetua a busca no banco de todos os objetos dessa classe
    formulario = MovRotForm()
    data = {'mov_rot':lista, 'form':formulario}
    return render(request, 'core/movRotativos_lista.html',data)

def movRotativos_novo(request):
    form = MovRotForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_movRotativos_lista')    

def movRotativos_update(request, id):
    data = {} #cria um dicionário
    movRot = MovRotativo.objects.get(id = id) #busca o veiculo que se deseja atualizar no banco, através do ID
    form = MovRotForm(request.POST or None, instance=movRot) #instancia um formulario, passando a "pessoa" que foi resgatada do banco para que seja preenchido 
    data['movRot'] = movRot #insere "pessoa no dicionário"
    data['form'] = form #insere o "form" no dicionário

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_movRotativos_lista')
    else:
        return render(request, 'core/movRotativos_update.html', data)        

def mensalistas_lista(request):
    lista = Mensalista.objects.all() #efetua a busca no banco de todos os objetos dessa classe
    form = MensalistaForm()
    data  = {'mensalistas':lista , 'form': form}
    return render(request, 'core/mensalista_lista.html', data)

def mensalistas_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_mensalistas_lista')
  
def mensalistas_update(request, id):
    data = {} #cria um dicionário
    mensalista = Mensalista.objects.get(id = id) #busca o veiculo que se deseja atualizar no banco, através do ID
    form = MensalistaForm(request.POST or None, instance=mensalista) #instancia um formulario, passando a "pessoa" que foi resgatada do banco para que seja preenchido 
    data['mensalista'] = mensalista #insere "pessoa no dicionário"
    data['form'] = form #insere o "form" no dicionário

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_mensalistas_lista')
    else:
        return render(request, 'core/mensalista_update.html', data)            

def movMensalistas_lista(request):
    lista = MovMensalista.objects.all() #efetua a busca no banco de todos os objetos dessa classe
    form = movMensalistasForm()
    data = {'movMensalistas':lista , 'form':form}
    return render(request, 'core/movMensalistas_lista.html', data)

def movMensalistas_novo(request):
    form = movMensalistasForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_movMensalistas_lista')

def movMensalistas_update(request, id):
    data = {} #cria um dicionário
    movMensalista = MovMensalista.objects.get(id = id) #busca o veiculo que se deseja atualizar no banco, através do ID
    form = movMensalistasForm(request.POST or None, instance=movMensalista) #instancia um formulario, passando a "pessoa" que foi resgatada do banco para que seja preenchido 
    data['movMensalista'] = movMensalista #insere "pessoa no dicionário"
    data['form'] = form #insere o "form" no dicionário

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_movMensalistas_lista')
    else:
        return render(request, 'core/movMensalistas_update.html', data)            