from django.db import models

# Create your models here.

class Clientes(models.Model):
    nome = models.CharField(max_length = 70, null = False)
    endereco = models.CharField(max_length = 200, blank = False, null = False)
    salario = models.DecimalField(decimal_places=2,max_digits=10)
    idade = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Telefone(models.Model):
    numero = models.CharField(max_length = 16)
    descricao = models.CharField(max_length = 80)
    cliente = models.ForeignKey(Clientes, on_delete = models.CASCADE)

    def __str__(self):
        return self.cliente.nome + '/' + self.descricao + '/' + self.numero