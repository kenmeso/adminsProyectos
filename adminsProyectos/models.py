from django.db import models
from django.contrib import admin


class Proyecto(models.Model):
    nombre    = models.CharField(max_length=60)
    descripcion    = models.CharField(max_length=120)
    importancia     = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Trabajador(models.Model):
    dpi = models.CharField(max_length=15)
    nombre  =   models.CharField(max_length=50)
    apellido =  models.CharField(max_length=50)
    direccion = models.TextField()
    telefono = models.CharField(max_length=8)
    email = models.EmailField()
    proyectos = models.ManyToManyField(Proyecto, through='Listado')

    def __str__(self):
        return self.nombre

class Listado(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    extra = 1

class ListadoInLine(admin.TabularInline):
    model = Listado
#muestra un campo extra al momento de insertar, como indicación que se pueden ingresar N actores.
    extra = 1

class ProyectoAdmin(admin.ModelAdmin):
    inlines = (ListadoInLine,)

class TrabajadorAdmin (admin.ModelAdmin):
    inlines = (ListadoInLine,)
