from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Usuario, Productos
import datetime

# Create your views here.
def index(request):
    if request.method == 'POST':
        nombreUsername = request.POST.get('nombreUsername')
        contraUsuario = request.POST.get('contraUsuario')

        #print(nombreUsername)
        #print(contraUsuario)

        usuarioInfo = authenticate(request, username=nombreUsername, password=contraUsuario)

        if usuarioInfo is not None:
            login(request, usuarioInfo)
            if usuarioInfo.usuario.tipoUsuario == 'ADMINISTRADOR':
                return HttpResponseRedirect(reverse('gestion_tienda:consolaAdministrador'))
            else:
                return HttpResponseRedirect(reverse('gestion_tienda:verProductos', kwargs={'ind':usuarioInfo.id}))
        else:
            return HttpResponseRedirect(reverse('gestion_tienda:index'))
        
    return render(request,'ingresoUsuario.html')

@login_required(login_url='http://127.0.0.1:8000/')
def cerrarSesion(request):
    logout(request)
    return HttpResponseRedirect(reverse('gestion_tienda:index'))

@login_required(login_url='http://127.0.0.1:8000/')
def consolaAdministrador(request):
    
    if request.user.usuario.tipoUsuario == 'ADMINISTRADOR':

        if request.method == 'POST':
            nombreUsername = request.POST.get('nombreUsername')
            contraUsuario = request.POST.get('contraUsuario')
            nombreUsuario = request.POST.get('nombreUsuario')
            apellidoUsuario = request.POST.get('apellidoUsuario')
            emailUsuario = request.POST.get('emailUsuario')
            tipoUsuario = request.POST.get('tipoUsuario')
            nroCelular = request.POST.get('nroCelular')
            fechaIngreso = request.POST.get('fechaIngreso')

            fechaSeparada = fechaIngreso.split('-')
            ini_dia = int(fechaSeparada[2])
            ini_mes = int(fechaSeparada[1])
            ini_anho = int(fechaSeparada[0])

            fechaIngresoRegistro = datetime.datetime(ini_anho, ini_mes, ini_dia)

            usuarioNuevo = User.objects.create(
                username=nombreUsername,
                email=emailUsuario,
            )

            usuarioNuevo.set_password(contraUsuario)
            usuarioNuevo.first_name = nombreUsuario
            usuarioNuevo.last_name = apellidoUsuario
            usuarioNuevo.is_staff = True
            usuarioNuevo.save()

            Usuario.objects.create(
                user = usuarioNuevo,
                tipoUsuario = tipoUsuario,
                nroCelular = nroCelular,
                fechaIngreso = fechaIngresoRegistro, 
            )

            return HttpResponseRedirect(reverse('gestion_tienda:consolaAdministrador'))
        
        return render(request, 'consolaAdministrador.html', {
            'usuariosTotales':User.objects.all().order_by('id')
        })
    
    else:
        return HttpResponseRedirect(reverse('gestion_tienda:verProductos', kwargs={'ind':request.user.id}))

@login_required(login_url='http://127.0.0.1:8000/')
def eliminarUsuario(request, ind):
    usuarioEliminar = User.objects.get(id=ind)
    print(usuarioEliminar)
    Usuario.objects.get(user=usuarioEliminar).delete
    usuarioEliminar.delete()

    return HttpResponseRedirect(reverse('gestion_tienda:consolaAdministrador'))

@login_required(login_url='http://127.0.0.1:8000/')
def verProductos(request, ind):
    usuarioInformacion = User.objects.get(id=ind)
    productosUsuario = Productos.objects.filter(usuarioRelacionado = usuarioInformacion).order_by('id')

    return render(request, 'informacionUsuario.html', {
        'usuarioInfo': usuarioInformacion,
        'productosUsuario': productosUsuario,
    })

@login_required(login_url='http://127.0.0.1:8000/')
def nuevoProducto(request, ind):

    if request.method == 'POST':
        usuarioRelacionado = User.objects.get(id=ind)
        nombreProducto = request.POST.get('nombreProducto')
        codigoProducto = request.POST.get('codigoProducto')
        precioCompra = request.POST.get('precioCompra')
        precioVenta = request.POST.get('precioVenta')

        Productos.objects.create(
            nombreProducto = nombreProducto,
            codigoProducto = codigoProducto,
            precioCompra = precioCompra,
            precioVenta = precioVenta,
            usuarioRelacionado = usuarioRelacionado,
        )

        return HttpResponseRedirect(reverse('gestion_tienda:verProductos', kwargs={'ind': ind}))

@login_required(login_url='http://127.0.0.1:8000/') 
def eliminarProducto(request, ind, pind):
    
    productoEliminar = Productos.objects.filter(usuarioRelacionado = ind, id = pind).delete()
    del(productoEliminar)

    return HttpResponseRedirect(reverse('gestion_tienda:verProductos', kwargs={'ind': ind}))