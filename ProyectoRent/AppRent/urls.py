from django.urls import path 
from AppRent.views import *
from . import views

urlpatterns = [

    path('arriendos/', arriendos, name='Arriendos'),
    path('clientes/', clientes, name='Clientes'),
    path('usuarios/', usuarios, name='Usuarios'),
    path('', vehiculos, name='Vehiculos'),
    path('lista-usuarios/', lista_usuarios),
    path('formulario-usuario/', formulario_usuario, name='FormularioUsuario'),
    path('formulario-reserva/', formulario_reserva, name='FormularioReserva'),
    path('agregar-cliente/', agregar_cliente, name='agregar_cliente'),
    path('lista-vehiculos/', views.lista_vehiculos, name='lista_vehiculos'),
    path('arriendos-realizados/', views.arriendos_realizados, name='arriendos_realizados'),


]