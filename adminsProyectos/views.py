from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import ClienteForm, ProductoForm, FacturaForm
from adminsProyectos.models import Proyecto, Lista, Trabajador
from django.contrib.auth.decorators import login_required
