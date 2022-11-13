from django.db import models
import sys
sys.path.append("accounts/")
from accounts.models import Usuario
class ingrediente(models.Model):
    nome=models.CharField(max_length=200)
    def __str__(self):
        return self.nome
class prato(models.Model):
    nome=models.CharField(max_length=200)
    img=models.ImageField(null=True)
    preco=models.FloatField(null=True)
    ingredientes=models.ManyToManyField(ingrediente, null=True)
    def __str__(self):
        return self.nome
class pedido(models.Model):
    data_pedido=models.DateField()
    valor_pedido=models.FloatField()
    prato_pedido=models.ManyToManyField(prato, null=True)
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.data_pedido)