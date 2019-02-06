from django.urls import path, include
from .views import (
    home, 

    pessoa_lista,
    pessoa_novo,
    pessoa_update,
    pessoa_delete,

    veiculo_lista,
    veiculo_novo,
    veiculo_update,
    veiculo_delete,

    movRotativos_lista,
    movRotativos_novo,
    movRotativos_update,
    movRotativos_delete,

    mensalistas_lista,
    mensalistas_novo,
    mensalistas_update,
    mensalistas_delete,
    
    movMensalistas_lista,
    movMensalistas_novo,
    movMensalistas_update,
    movMensalistas_delete,
)

urlpatterns = [
    path('', home, name='core_home'), 

    path('pessoa', pessoa_lista, name='core_pessoa_lista'),
    path('pessoas', pessoa_lista, name='core_pessoas_lista'),
    path('pessoa-novo', pessoa_novo, name='core_pessoa_novo'),
    path('pessoa-update/<int:id>', pessoa_update, name='core_pessoa_update'),
    path('pessoa-delete/<int:id>', pessoa_delete, name='core_pessoa_delete'),
    
    path('veiculo', veiculo_lista, name='core_veiculo_lista'),
    path('veiculos', veiculo_lista, name='core_veiculo_lista'),
    path('veiculo-novo', veiculo_novo, name='core_veiculo_novo'),
    path('veiculo-update/<int:id>', veiculo_update, name='core_veiculo_update'),
    path('veiculo-delete/<int:id>', veiculo_delete, name='core_veiculo_delete'),

    path('mov_rotativos', movRotativos_lista, name='core_movRotativos_lista'),
    path('mov_rotativos-novo', movRotativos_novo, name = 'core_movRotativos_novo'),
    path('mov_rotativos-update/<int:id>', movRotativos_update, name='core_movRotativos_update'),
    path('mov_rotativos-delete/<int:id>', movRotativos_delete, name='core_movRotativos_delete'),

    path('mensalistas', mensalistas_lista, name='core_mensalistas_lista'),
    path('mensalistas-novo', mensalistas_novo, name = 'core_mensalistas_novo'),
    path('mensalistas-update/<int:id>', mensalistas_update, name='core_mensalistas_update'),
    path('mensalistas-delete/<int:id>', mensalistas_delete, name='core_mensalistas_delete'),

    path('mov_mensalistas', movMensalistas_lista, name='core_movMensalistas_lista'),
    path('mov_mensalistas-novo', movMensalistas_novo, name = 'core_movMensalistas_novo'),
    path('mov_mensalistas-update/<int:id>', movMensalistas_update, name='core_movMensalistas_update'),
    path('mov_mensalistas-delete/<int:id>', movMensalistas_delete, name='core_movMensalistas_delete'),
]