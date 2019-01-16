from django.urls import path, include
from .views import (
    home, 
    lista_pessoas,
    lista_veiculos,
    lista_movrotativos,
)

urlpatterns = [
    path('', home, name='core_home'), 
    path('pessoa', lista_pessoas, name='core_lista_pessoas'),
    path('pessoas', lista_pessoas, name='core_lista_pessoas'),
    path('veiculos', lista_veiculos, name='core_lista_veiculos'),
    path('mov_rotativos', lista_movrotativos, name='core_lista_movrot'),
]