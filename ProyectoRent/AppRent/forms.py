from django import forms

class FormularioUsuario(forms.Form):
    nombre = forms.CharField(required=True)
    apellidos = forms.CharField(required=True)
    telefono = forms.CharField(required=True)
    cargo = forms.CharField(required=True)

class BusquedaClientesForm(forms.Form):
    busqueda = forms.CharField(label='Nombre Cliente', max_length=100)

class AgregarClienteForm(forms.Form):
    nombre = forms.CharField(required=True)
    apellidos = forms.CharField(required=True)
    rut = forms.CharField(required=True)
    telefono = forms.CharField(required=True)
    email = forms.EmailField(required=True)

class AgregarVehiculos(forms.Form):
    Marca= forms.CharField(required=True)
    Modelo= forms.CharField(required=True)
    Año= forms.IntegerField(required=True)
    Cantidad= forms.IntegerField(required=True)

class ReservarVehiculo(forms.Form):

    fechaInicio=forms.DateField(required=True)
    fechaTermino=forms.DateField(required=True)
    idVehiculo=forms.IntegerField(required=True)
    idCliente=forms.IntegerField(required=True)