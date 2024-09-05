from django import forms
from .models import Articulo, Averia, Asignacion, Compra

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['descripcion', 'marca', 'modelo', 'serial', 'codigo_bn', 'cantidad', 'condicion', 'fecha_adq', 'tipo_articulo']
        labels = {
                    'descripcion': 'Descripción',
                    'marca': 'Marca',
                    'modelo': 'Modelo',
                    'serial': 'Serial',
                    'codigo_bn': 'Código BN',
                    'cantidad': 'Cantidad',
                    'condicion': 'Condición',
                    'fecha_adq': 'Fecha de adquisición',
                    'tipo_articulo': 'Tipo de artículo',
        }
        widgets = {}

class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['descripcion', 'marca', 'modelo', 'serial', 'codigo_bn', 'cantidad', 'condicion', 'fecha_adq']
        labels = {
                    'descripcion': 'Descripción',
                    'marca': 'Marca',
                    'modelo': 'Modelo',
                    'serial': 'Serial',
                    'codigo_bn': 'Código BN',
                    'cantidad': 'Cantidad',
                    'condicion': 'Condición',
                    'fecha_adq': 'Fecha de adquisición',
        }
        widgets = {}
        
class ConsumibleForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['descripcion', 'marca', 'serial', 'cantidad', 'fecha_adq']
        labels = {
                    'descripcion': 'Descripción',
                    'marca': 'Marca',
                    'serial': 'Serial',
                    'cantidad': 'Cantidad',
                    'fecha_adq': 'Fecha de adquisición',
        }
        widgets = {}
        
class MobiliarioForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['descripcion', 'serial', 'codigo_bn', 'cantidad', 'condicion', 'fecha_adq']
        labels = {
                    'descripcion': 'Descripción',
                    'serial': 'Serial',
                    'codigo_bn': 'Código BN',
                    'cantidad': 'Cantidad',
                    'condicion': 'Condición',
                    'fecha_adq': 'Fecha de adquisición',
        }
        widgets = {}
        
class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['descripcion', 'marca', 'modelo', 'placa', 'codigo_bn', 'cantidad', 'condicion', 'fecha_adq']
        labels = {
                    'descripcion': 'Descripción',
                    'marca': 'Marca',
                    'modelo': 'Modelo',
                    'placa': 'Placa',
                    'codigo_bn': 'Código BN',
                    'cantidad': 'Cantidad',
                    'condicion': 'Condición',
                    'fecha_adq': 'Fecha de adquisición',
        }
        widgets = {}
        
class AveriaForm(forms.ModelForm):
    class Meta:
        model = Averia
        fields = ['problema', 'tipo_averia', 'departamento', 'ubicacion', 'serial', 'codigo_bn']
        labels = {
                    'problema': 'Problema',
                    'tipo_averia': 'Tipo de avería',
                    'departamento': 'Departamento',
                    'ubicacion': 'Ubicación',
                    'serial': 'Serial',
                    'codigo_bn': 'Código BN'
        }
        widgets = {}
        
class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['n_orden', 'valor_bs']
        labels = {
                    'n_orden': 'N° de orden',
                    'valor_bs': 'Valor en BS',
        }
        widgets = {}
        
class AsignacionForm(forms.ModelForm):
    class Meta:
        model = Asignacion
        fields = ['articulo', 'departamento', 'cantidad', 'descripcion', 'observaciones']
        labels = {
                    'articulo': 'Artículo',
                    'departamento': 'Departamento',
                    'cantidad': 'Cantidad',
                    'descripcion': 'Descripción',
                    'observaciones': 'Observaciones',
        }
        widgets = {}
