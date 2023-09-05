from django.db import models

# Create your models here.

class Vehiculos(models.Model):

    marca=models.TextField(max_length=25)
    modelo=models.TextField(max_length=25)
    year=models.IntegerField()
    cant_vehiculos=models.IntegerField()

class Clientes(models.Model):
    
    nombre=models.TextField(max_length=30)
    apellidos=models.TextField(max_length=30)
    rut=models.TextField(max_length=12)
    telefono=models.TextField(max_length=15)
    email=models.EmailField()

class Usuarios(models.Model):
    nombre=models.TextField(max_length=25)
    apellido=models.TextField(max_length=25)
    telefono=models.TextField(max_length=15)
    cargo=models.TextField(max_length=20)

class Arriendos(models.Model):
    fecha_inicio=models.DateField()
    fecha_termino=models.DateField()
    idVehiculo=models.IntegerField(null=True)
    idCliente=models.IntegerField(null=True)