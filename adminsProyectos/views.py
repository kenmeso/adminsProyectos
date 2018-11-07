from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import TrabajadorForm, ProyectoForm, ListaForm
from adminsProyectos.models import Proyecto, Lista, Trabajador
from django.contrib.auth.decorators import login_required

@login_required
def lista_nueva(request):
    if request.method == "POST":
        formulario = TrabajadorForm(request.POST)
        if formulario.is_valid():
            trabajador = Trabajador.objects.create(
            nit = formulario.cleaned_data['nit'],
            nombre = formulario.cleaned_data['nombre'],
            apellido = formulario.cleaned_data['apellido'],
            direccion = formulario.cleaned_data['direccion'],
            email = formulario.cleaned_data['email'],
            telefono = formulario.cleaned_data['telefono'])
            for proyecto_id in request.POST.getlist('proyectos'):
                factura = Factura(proyecto_id=proyecto_id, trabajador_id = trabajador.id)
                factura.save()
            messages.add_message(request, messages.SUCCESS, 'Listado creado con éxito.')
            return redirect('lista_lista')
    else:
        formulario = TrabajadorForm()
    return render(request, 'lista/lista_nueva.html', {'formulario': formulario})

@login_required
def lista_lista(request):
    trabajador = Trabajador.objects.all()
    return render(request, 'lista/lista_lista.html', {'trabajador': trabajador})

@login_required
def lista_detalle(request, pk):
     trabajador = get_object_or_404(Trabajador,pk=pk)
     lista = Lista.objects.filter(trabajador__id=pk)
     return render(request,"lista/lista_detalle.html",{'trabajador':trabajador, 'lista':lista})

@login_required
def lista_editar(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)
    if request.method == 'POST':
        formulario = ListaForm(request.POST, request.FILES, instance=trabajador)
        if formulario.is_valid():
            trabajador = formulario.save()
            trabajador.save()
            return redirect('listaa_lista')
    else:
        formulario = TrabajadorForm(instance=trabajador)
    return render(request, 'lista/lista_editar.html', {'formulario': formulario})

@login_required
def lista_remove(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)
    trabajador.delete()
    return redirect('lista_lista')

@login_required
def proyecto_lista(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyectos/proyecto_lista.html', {'proyectos': proyectos})

@login_required
def proyecto_nuevo(request):
    if request.method == "POST":
        formulario = ProyectoForm(request.POST)
        if formulario.is_valid():
            proyecto = Proyecto.objects.create(
            nombre = formulario.cleaned_data['nombre'],
            precio = formulario.cleaned_data['precio'],
            stock = formulario.cleaned_data['stock'])
            messages.add_message(request, messages.SUCCESS, 'Proyecto creado con éxito.')
            return redirect('proyecto_lista')
    else:
        formulario = ProyectoForm()
    return render(request, 'proyectos/proyecto_crear.html', {'formulario': formulario})

@login_required
def proyecto_editar(request, pk):
    proyecto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES, instance=proyecto)
        if formulario.is_valid():
            proyecto = formulario.save()
            proyecto.save()
            return redirect('proyecto_lista')
    else:
        formulario = ProyectoForm(instance=proyecto)
    return render(request, 'proyectos/proyecto_editar.html', {'formulario': formulario})

@login_required
def proyecto_remove(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    proyecto.delete()
return redirect('proyecto_lista')
