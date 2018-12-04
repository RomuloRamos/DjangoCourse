from django.contrib import admin
from .models import Empregado, Telefone, CPF, Departamento

# Register your models here.

#Essa classe defini o que será exibido no model do admin. 
# Porém é necessáio cuidado para não "esconder" campos 
# cujo o preenchimento é obrigatório!

#filds - define quais campos serão mostrados ao usuário
#list_display - define campos as serem mostrados no grid
#list_filter - define um tipo de filtro a ser aplicado pelo usuário
#search_fields - cria campo de busca
class EmpregadoAdmin(admin.ModelAdmin):
    fields = ('nome', 'endereco')
    list_display = ('id','nome', 'endereco', 'email')
    list_filter = ('departamentos',)
    search_fields = ('id', 'nome')

admin.site.register(Empregado, EmpregadoAdmin)
admin.site.register(Telefone)
admin.site.register(CPF)   
admin.site.register(Departamento)