from django.contrib import admin
from .models import Vehiculos, Arriendos, Clientes, Usuarios
# Register your models here.

admin.site.register(Vehiculos)
admin.site.register(Clientes)
admin.site.register(Arriendos)
admin.site.register(Usuarios)