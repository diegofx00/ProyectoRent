from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.db.models import Q
from AppRent.models import *
from .forms import  *
from datetime import date


# Create your views here.

def vehiculos(req):
    if req.method == 'POST':
        form_agregar = AgregarVehiculos(req.POST)
        if form_agregar.is_valid():
            print(form_agregar.cleaned_data)
            data = form_agregar.cleaned_data
            Vehic = Vehiculos(marca = data["Marca"],
            modelo = data["Modelo"],
            year = data["Año"],
            cant_vehiculos = data["Cantidad"]) 
            Vehic.save()
            return redirect('Vehiculos')
    else:
        form_agregar = AgregarVehiculos()
        

    lista = Vehiculos.objects.all()

    context = {
        'form': form_agregar,
        'vehiculos_context': lista,
    }
    
    return render(req, "vehiculos.html", context)

def arriendos(req):
    # Obtener la lista de clientes y películas
    lista_clientes = Clientes.objects.all()
    lista_vehiculos = Vehiculos.objects.all()
    miFormulario2 = ReservarVehiculo()

    context = {
        'clientes_context': lista_clientes,
        'vehiculos_context': lista_vehiculos,
        "miFormulario2": miFormulario2
    }

    return render(req, "arriendos.html", context)

def clientes(req):
    resultados = []  

    if req.method == 'POST':
        form_busqueda = BusquedaClientesForm(req.POST)
        if form_busqueda.is_valid():
            busqueda = form_busqueda.cleaned_data['busqueda']
            resultados = Clientes.objects.filter(
                nombre__icontains=busqueda
            )  
        form_agregar = AgregarClienteForm(req.POST)
        if form_agregar.is_valid():
            print(form_agregar.cleaned_data)
            data = form_agregar.cleaned_data
            clientes = Clientes(nombre = data["nombre"],
            apellidos = data["apellidos"],
            rut = data["rut"],
            telefono = data["telefono"]) 
            clientes.save()
            return redirect('Clientes')
    else:
        form_busqueda = BusquedaClientesForm()
        form_agregar = AgregarClienteForm()

    context = {
        'resultados': resultados,
        'form_busqueda': form_busqueda,
        'form_agregar': form_agregar,
    }

    return render(req, 'clientes.html', context)

def usuarios(req):
    lista = Usuarios.objects.all()
    miFormulario = FormularioUsuario()
    return render(req,"usuarios.html", {"lista_usuarios": lista, "miFormulario": miFormulario})

def lista_usuarios(req):

    lista = Usuarios.objects.all()
    miFormulario = FormularioUsuario()
    return render(req,"usuarios.html",{"lista_usuarios": lista, "miFormulario": miFormulario})


def formulario_usuario(req: HttpRequest):

    print('method', req.method)
    print('post', req.POST)

    if req.method== 'POST':
        miFormulario = FormularioUsuario(req.POST)
        if miFormulario.is_valid():
            print(miFormulario.cleaned_data)
            data = miFormulario.cleaned_data

            usuarios = Usuarios(nombre = data["nombre"],
            apellido = data["apellidos"],
            telefono = data["telefono"],
            cargo = data["cargo"])        
            usuarios.save()
            return redirect('Usuarios')
        else:
            return render(req, "index.html",{"mensaje": "Formulario Invalido"})
    else:

        miFormulario = FormularioUsuario()
        
    return render(req, "usuarios.html", {"miFormulario": miFormulario})

def agregar_cliente(request):
    if request.method == 'POST':
        form = AgregarClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Clientes') 
    else:
        form = AgregarClienteForm()
    
    context = {
        'form': form,
    }

    return render(request, 'agregar_cliente.html', context)

def lista_vehiculos(req):
    listap_query=Vehiculos.objects.all()
    context={'vehiculos_context':listap_query}
    return render(req, 'lista_vehiculos.html',context)

def lista_clientes(req):
    listap_query=Clientes.objects.all()
    context={'clientes_context':listap_query}
    return render(req, 'lista_clientes.html',context)

def agregar_vehiculos(request):
    if request.method == 'POST':
        form = AgregarVehiculos(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Vehiculos') 
    else:
        form = AgregarVehiculos()
    
    context = {
        'form': form,
    }

    return render(request, 'agregar_vehiculo.html', context)

def formulario_reserva(req: HttpRequest):

    print('method', req.method)
    print('post', req.POST)

    if req.method== 'POST':
        miFormulario2 = ReservarVehiculo(req.POST)
        if miFormulario2.is_valid():
            print(miFormulario2.cleaned_data)
            data = miFormulario2.cleaned_data

            arriendo = Arriendos(fecha_inicio = data["fechaInicio"],
            fecha_termino = data["fechaTermino"],
            idVehiculo = data["idVehiculo"],
            idCliente = data["idCliente"])        
            arriendo.save()
            return redirect('Arriendos')
        else:
            return render(req, "index.html",{"mensaje": "Formulario Invalido"})
    else:

        miFormulario2 = ReservarVehiculo()
        
    return render(req, "arriendos.html", {"miFormulario2": miFormulario2})

def arriendos_realizados(request):
    sql_query = """
    SELECT cl.nombre, cl.apellidos, cl.rut, cl.telefono, cl.email,
           arr.fecha_inicio, arr.fecha_termino,
           vh.marca, vh.modelo
    FROM Clientes cl
    INNER JOIN Arriendos arr ON cl.id = arr.idCliente
    INNER JOIN Vehiculos vh ON pl.id = arr.idVehiculo
    """

    # Ejecuta la consulta SQL
    results = Arriendos.objects.raw(sql_query)

    context = {
        'arriendos_query': results,
    }

    return render(request, 'arriendos_realizados.html', context)
