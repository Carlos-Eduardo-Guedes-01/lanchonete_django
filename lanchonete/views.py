from django.shortcuts import render
from .models import prato,ingrediente,pedido
def cardapio(request):
    pratos=prato.objects.all()
    print(pratos)
    return render(request, '../../lanchonete/templates/cardapio.html',{'pratos':pratos})
def detalhes_prato(request,id):
    prato2=prato.objects.get(id=id)
    return render(request, '../../lanchonete/templates/detalhes_prato.html',{'prato2':prato2})