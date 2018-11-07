from django.contrib import admin
from adminsProyectos.models import Proyecto, ProyectoAdmin, Trabajador, TrabajadorAdmin


admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Trabajador, TrabajadorAdmin)
