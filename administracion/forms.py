from django import forms
from .models import Articulo, Averia, Asignacion, Compra

class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['descripcion', 'marca', 'modelo', 'serial', 'codigo_bn', 'cantidad', 'condicion', 'fecha_adq']
        widgets = {}
        
class ConsumibleForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['descripcion', 'marca', 'serial', 'cantidad', 'fecha_adq']
        widgets = {}
        
class MobiliarioForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['descripcion', 'serial', 'codigo_bn', 'cantidad', 'condicion', 'fecha_adq']
        widgets = {}
        
class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['descripcion', 'marca', 'modelo', 'placa', 'codigo_bn', 'cantidad', 'condicion', 'fecha_adq']
        widgets = {}
        
class AveriaForm(forms.ModelForm):
    class Meta:
        model = Averia
        fields = ['problema', 'tipo_averia', 'departamento', 'ubicacion', 'serial', 'codigo_bn']
        widgets = {}
        
class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['descripcion', 'marca', 'modelo', 'serial', 'placa', 'codigo_bn', 'n_orden', 'valor_bs', 'cantidad', 'fecha_adq', 'tipo_articulo']
        widgets = {}
        
class AsignacionForm(forms.ModelForm):
    class Meta:
        model = Asignacion
        fields = ['articulo', 'departamento', 'cantidad', 'descripcion', 'observaciones']
        widgets = {}
