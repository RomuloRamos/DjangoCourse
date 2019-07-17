from django.shortcuts import render

# Create your views here.
def website_home(request):
    return render(request,'website/index.html')

def website_contatos(request):
    return render(request, 'website/contatos.html')    