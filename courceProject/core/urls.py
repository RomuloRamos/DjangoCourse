from django.urls import path, include
from .views import (
    home, 
    lista_pessoas,
    lista_veiculos,
    lista_movrotativos,
    lista_mensalistas,
    lista_movmensalistas,
    pessoa_novo,
    veiculo_novo,
    movrotativos_novo,
)

urlpatterns = [
    path('', home, name='core_home'), 
    path('pessoa', lista_pessoas, name='core_lista_pessoas'),
    path('pessoa-novo', pessoa_novo, name='core_pessoa_novo'),
    path('veiculo-novo', veiculo_novo, name='core_veiculo_novo'),
    path('mov-rot-novo', movrotativos_novo, name = 'core_mov_rot_novo'),
    path('pessoas', lista_pessoas, name='core_lista_pessoas'),
    path('veiculos', lista_veiculos, name='core_lista_veiculos'),
    path('mov_rotativos', lista_movrotativos, name='core_lista_movrot'),
    path('mensalistas', lista_mensalistas, name='core_lista_mensalistas'),
    path('mov_mensalistas', lista_movmensalistas, name='core_lista_movmensalistas'),
]