from django.db import models

# Create your models here.

class Departamento(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class CPF(models.Model):
    numero = models.CharField(max_length=15)
    data_exp = models.DateTimeField(auto_now = False)

    def __str__(self):
        return self.numero

class Empregado(models.Model):
    nome = models.CharField(max_length = 70, null = False)
    endereco = models.CharField(max_length = 200, blank = False, null = False)
    salario = models.DecimalField(decimal_places=2,max_digits=10)
    idade = models.IntegerField()
    email = models.EmailField()
    cpf = models.OneToOneField(CPF, on_delete = models.CASCADE, null=True, blank = True)
    departamentos = models.ManyToManyField(Departamento, blank = True)

    def __str__(self):
        return self.nome

class Telefone(models.Model):
    numero = models.CharField(max_length = 16)
    descricao = models.CharField(max_length = 80)
    empregado = models.ForeignKey(Empregado, on_delete = models.CASCADE)

    def __str__(self):
        return self.empregado.nome + '/' + self.descricao + '/' + self.numero
