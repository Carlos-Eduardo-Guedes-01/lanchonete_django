from django.contrib import admin
from .models import ingrediente, pedido, prato, categoria
admin.site.register(ingrediente)
admin.site.register(pedido)
admin.site.register(prato)
admin.site.register(categoria)