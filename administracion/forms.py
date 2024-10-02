from django import forms
from .models import Articulo, Averia, Asignacion, Compra

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['descripcion', 'marca', 'modelo', 'serial', 'placa', 'cantidad_combustible', 'codigo_bn', 'cantidad', 'condicion', 'fecha_adq', 'tipo_articulo']
        labels = {
                    'descripcion': 'Descripción',
                    'marca': 'Marca',
                    'modelo': 'Modelo',
                    'serial': 'Serial',
                    'placa': 'Placa',
                    'cantidad_combustible': 'Cantidad de combustible máx. En litros',
                    'codigo_bn': 'Código BN',
                    'cantidad': 'Cantidad',
                    'condicion': 'Condición',
                    'fecha_adq': 'Fecha de adquisición',
                    'tipo_articulo': 'Tipo de artículo',
        }
        widgets = {
            'fecha_adq': forms.DateInput(format=('%Y-%m-%d'), attrs={'placeholder': 'Selecciona una fecha', 'type': 'date'}),
        }

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
        widgets = {
            'fecha_adq': forms.DateInput(format=('%Y-%m-%d'), attrs={'placeholder': 'Selecciona una fecha', 'type': 'date'}),
        }
        
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
        widgets = {
            'fecha_adq': forms.DateInput(format=('%Y-%m-%d'), attrs={'placeholder': 'Selecciona una fecha', 'type': 'date'}),
        }
        
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
        widgets = {
            'fecha_adq': forms.DateInput(format=('%Y-%m-%d'), attrs={'placeholder': 'Selecciona una fecha', 'type': 'date'}),
        }
        
class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['descripcion', 'marca', 'modelo', 'placa', 'cantidad_combustible', 'codigo_bn', 'cantidad', 'condicion', 'fecha_adq']
        labels = {
                    'descripcion': 'Descripción',
                    'marca': 'Marca',
                    'modelo': 'Modelo',
                    'placa': 'Placa',
                    'cantidad_combustible': 'Cantidad de combustible máx. En litros',
                    'codigo_bn': 'Código BN',
                    'cantidad': 'Cantidad',
                    'condicion': 'Condición',
                    'fecha_adq': 'Fecha de adquisición',
        }
        widgets = {
            'fecha_adq': forms.DateInput(format=('%Y-%m-%d'), attrs={'placeholder': 'Selecciona una fecha', 'type': 'date'}),
        }
        
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
        fields = ['articulo', 'sede', 'departamento', 'cantidad', 'descripcion', 'observaciones']
        labels = {
                    'articulo': 'Artículo',
                    'sede': 'Sede',
                    'departamento': 'Departamento',
                    'cantidad': 'Cantidad',
                    'descripcion': 'Descripción',
                    'observaciones': 'Observaciones',
        }
        widgets = {
            'articulo': forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        super(AsignacionForm, self).__init__(*args, **kwargs)
        self.fields['articulo'].queryset = Articulo.objects.filter(asignado=False)

class AsignacionUpdateForm(forms.ModelForm):
    class Meta:
        model = Asignacion
        fields = ['articulo', 'sede', 'departamento', 'cantidad', 'descripcion', 'observaciones']
        labels = {
                    'articulo': 'Artículo (Solo lectura)',
                    'sede': 'Sede',
                    'departamento': 'Departamento',
                    'cantidad': 'Cantidad',
                    'descripcion': 'Descripción',
                    'observaciones': 'Observaciones',
        }
        widgets = {
            'articulo': forms.Select(attrs={'style': 'pointer-events: none;', 'readonly' : 'readonly'}),
        }
