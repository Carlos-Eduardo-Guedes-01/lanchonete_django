from django.contrib import admin
from django.urls import path
from .views import cardapio,detalhes_prato
name_app='lanchonete'
urlpatterns=[
    path('cardapio/',cardapio, name='cardapio'),
    path('detalhes-produtos/<int:id>/',detalhes_prato,name='detalhar_prato')
]