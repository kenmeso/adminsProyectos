from django import forms
from .models import Producto, Cliente

class TrabajadorForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Trabajador
        fields = ('dpi', 'nombre', 'apellido', 'direccion', 'telefono', 'email', 'proyectos')

def __init__ (self, *args, **kwargs):
        super(TrabajadorForm, self).__init__(*args, **kwargs)
        self.fields["proyectos"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["proyectos"].help_text = "Seleccione Proyectos"
        self.fields["proyectos"].queryset = Proyecto.objects.all()

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
fields = ('nombre', 'descripcion', 'importancia')
