from django.shortcuts import render, redirect, get_object_or_404
from .models import Articulo, Averia, Compra, Asignacion
from .forms import ArticuloForm, TecnologiaForm, ConsumibleForm, MobiliarioForm, VehiculoForm, AveriaForm, CompraForm, AsignacionForm
from django.core.paginator import Paginator
from django.views.generic import ListView

# Create your views here.

# Inicio
def inicio(request):
    return render(request, 'inicio.html')

# Tecnologia
def tecnologia(request):
    tecnologia = Articulo.objects.filter(tipo_articulo=1)
    paginator = Paginator(tecnologia, 10)  # Show 10 per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'tecnologia/tecnologia.html', {
        'tecnologia': paginator.page(page_number),
        'page_obj': page_obj
    })

def create_tecnologia(request):
    if request.method == 'GET':
        return render(request, 'tecnologia/create_tecnologia.html', {
            'form': TecnologiaForm
        })
    else:
        try:
            form = TecnologiaForm(request.POST)
            new_tecnologia = form.save(commit=False)
            new_tecnologia.user = request.user
            new_tecnologia.tipo_articulo_id = 1
            new_tecnologia.save()
            return redirect('tecnologia')
        except ValueError:
            return render(request, 'tecnologia/create_tecnologia.html', {
                'form': TecnologiaForm,
                'error': 'Please provide valid data'
            })

def update_tecnologia(request, tecnologia_id):
    if request.method == 'GET':
        tecnologia = get_object_or_404(Articulo, pk=tecnologia_id)
        form = TecnologiaForm(instance=tecnologia)
        return render(request, 'tecnologia/update_tecnologia.html', {
            'tecnologia': tecnologia,
            'form': form
        })
    else:
        try:
            tecnologia = get_object_or_404(Articulo, pk=tecnologia_id)
            form = TecnologiaForm(request.POST, instance=tecnologia)
            form.save()
            return redirect('tecnologia')
        except ValueError:
            return render(request, 'tecnologia/update_tecnologia.html', {
                'tecnologia': tecnologia,
                'form': form,
                'error': 'Error updating tecnologia'
            })

def delete_tecnologia(request, tecnologia_id):
    tecnologia = get_object_or_404(Articulo, pk=tecnologia_id)
    if request.method == 'POST':
        tecnologia.delete()
        return redirect('tecnologia') 

# Consumible    
def consumible(request):
    consumible = Articulo.objects.filter(tipo_articulo=2)
    paginator = Paginator(consumible, 10)  # Show 10 per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'consumible/consumible.html', {
        'consumible': paginator.page(page_number),
        'page_obj': page_obj
    })

def create_consumible(request):
    if request.method == 'GET':
        return render(request, 'consumible/create_consumible.html', {
            'form': ConsumibleForm
        })
    else:
        try:
            form = ConsumibleForm(request.POST)
            new_consumible = form.save(commit=False)
            new_consumible.user = request.user
            new_consumible.tipo_articulo_id = 2
            new_consumible.condicion_id = 1
            new_consumible.save()
            return redirect('consumible')
        except ValueError:
            return render(request, 'consumible/create_consumible.html', {
                'form': ConsumibleForm,
                'error': 'Please provide valid data'
            })
        
def update_consumible(request, consumible_id):
    if request.method == 'GET':
        consumible = get_object_or_404(Articulo, pk=consumible_id, user=request.user)
        form = ConsumibleForm(instance=consumible)
        return render(request, 'consumible/update_consumible.html', {
            'consumible': consumible,
            'form': form
        })
    else:
        try:
            consumible = get_object_or_404(Articulo, pk=consumible_id, user=request.user)
            form = ConsumibleForm(request.POST, instance=consumible)
            form.save()
            return redirect('consumible')
        except ValueError:
            return render(request, 'consumible/update_consumible.html', {
                'consumible': consumible,
                'form': form,
                'error': 'Error updating consumible'
            })
        
def delete_consumible(request, consumible_id):
    consumible = get_object_or_404(Articulo, pk=consumible_id, user=request.user)
    if request.method == 'POST':
        consumible.delete()
        return redirect('consumible')
    
# Mobiliario
def mobiliario(request):
    mobiliario = Articulo.objects.filter(tipo_articulo=3)
    paginator = Paginator(mobiliario, 10)  # Show 10 per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'mobiliario/mobiliario.html', {
        'mobiliario': paginator.page(page_number),
        'page_obj': page_obj
    })

def create_mobiliario(request):
    if request.method == 'GET':
        return render(request, 'mobiliario/create_mobiliario.html', {
            'form': MobiliarioForm
        })
    else:
        try:
            form = MobiliarioForm(request.POST)
            new_mobiliario = form.save(commit=False)
            new_mobiliario.user = request.user
            new_mobiliario.tipo_articulo_id = 3
            new_mobiliario.save()
            return redirect('mobiliario')
        except ValueError:
            return render(request, 'mobiliario/create_mobiliario.html', {
                'form': MobiliarioForm,
                'error': 'Please provide valid data'
            })
        
def update_mobiliario(request, mobiliario_id):
    if request.method == 'GET':
        mobiliario = get_object_or_404(Articulo, pk=mobiliario_id, user=request.user)
        form = MobiliarioForm(instance=mobiliario)
        return render(request, 'mobiliario/update_mobiliario.html', {
            'mobiliario': mobiliario,
            'form': form
        })
    else:
        try:
            mobiliario = get_object_or_404(Articulo, pk=mobiliario_id, user=request.user)
            form = MobiliarioForm(request.POST, instance=mobiliario)
            form.save()
            return redirect('mobiliario')
        except ValueError:
            return render(request, 'mobiliario/update_mobiliario.html', {
                'mobiliario': mobiliario,
                'form': form,
                'error': 'Error updating mobiliario'
            })
        
def delete_mobiliario(request, mobiliario_id):
    mobiliario = get_object_or_404(Articulo, pk=mobiliario_id, user=request.user)
    if request.method == 'POST':
        mobiliario.delete()
        return redirect('mobiliario')
    
# Vehiculo
def vehiculo(request):
    vehiculo = Articulo.objects.filter(tipo_articulo=4)
    paginator = Paginator(vehiculo, 10)  # Show 10 per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'vehiculo/vehiculo.html', {
        'vehiculo': paginator.page(page_number),
        'page_obj': page_obj
    })

def create_vehiculo(request):
    if request.method == 'GET':
        return render(request, 'vehiculo/create_vehiculo.html', {
            'form': VehiculoForm
        })
    else:
        try:
            form = VehiculoForm(request.POST)
            new_vehiculo = form.save(commit=False)
            new_vehiculo.user = request.user
            new_vehiculo.tipo_articulo_id = 4
            new_vehiculo.save()
            return redirect('vehiculo')
        except ValueError:
            return render(request, 'vehiculo/create_vehiculo.html', {
                'form': VehiculoForm,
                'error': 'Please provide valid data'
            })
        
def update_vehiculo(request, vehiculo_id):
    if request.method == 'GET':
        vehiculo = get_object_or_404(Articulo, pk=vehiculo_id, user=request.user)
        form = VehiculoForm(instance=vehiculo)
        return render(request, 'vehiculo/update_vehiculo.html', {
            'vehiculo': vehiculo,
            'form': form
        })
    else:
        try:
            vehiculo = get_object_or_404(Articulo, pk=vehiculo_id, user=request.user)
            form = VehiculoForm(request.POST, instance=vehiculo)
            form.save()
            return redirect('vehiculo')
        except ValueError:
            return render(request, 'vehiculo/update_vehiculo.html', {
                'vehiculo': vehiculo,
                'form': form,
                'error': 'Error updating vehiculo'
            })
        
def delete_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Articulo, pk=vehiculo_id, user=request.user)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('vehiculo')
    
# Reporte de Averia
def averia(request):
    averia = Averia.objects.filter()
    paginator = Paginator(averia, 10)  # Show 10 per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'averia/averia.html', {
        'averia': paginator.page(page_number),
        'page_obj': page_obj
    })

def create_averia(request):
    if request.method == 'GET':
        return render(request, 'averia/create_averia.html', {
            'form': AveriaForm
        })
    else:
        try:
            form = AveriaForm(request.POST)
            new_averia = form.save(commit=False)
            new_averia.user = request.user
            new_averia.save()
            return redirect('averia')
        except ValueError:
            return render(request, 'averia/create_averia.html', {
                'form': AveriaForm,
                'error': 'Please provide valid data'
            })
        
def update_averia(request, averia_id):
    if request.method == 'GET':
        averia = get_object_or_404(Averia, pk=averia_id, user=request.user)
        form = AveriaForm(instance=averia)
        return render(request, 'averia/update_averia.html', {
            'averia': averia,
            'form': form
        })
    else:
        try:
            averia = get_object_or_404(Averia, pk=averia_id, user=request.user)
            form = AveriaForm(request.POST, instance=averia)
            form.save()
            return redirect('averia')
        except ValueError:
            return render(request, 'averia/update_averia.html', {
                'averia': averia,
                'form': form,
                'error': 'Error updating averia'
            })
        
def delete_averia(request, averia_id):
    averia = get_object_or_404(Averia, pk=averia_id, user=request.user)
    if request.method == 'POST':
        averia.delete()
        return redirect('averia')
    
# Compra
def compra(request):
    compra = Compra.objects.filter()
    paginator = Paginator(compra, 10)  # Show 10 per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'compra/compra.html', {
        'compra': paginator.page(page_number),
        'page_obj': page_obj
    })

def create_compra(request):
    if request.method == 'GET':
        return render(request, 'compra/create_compra.html', {
            'form_articulo': ArticuloForm,
            'form_compra': CompraForm,
        })
    else:
        try:
            form_articulo = ArticuloForm(request.POST)
            form_compra = CompraForm(request.POST)
            new_articulo = form_articulo.save(commit=False)
            new_articulo.user = request.user
            new_articulo.save()
            new_compra = form_compra.save(commit=False)
            new_compra.articulo_id = new_articulo.id
            new_compra.user = request.user
            new_compra.save()
            return redirect('compra')
        except ValueError:
            return render(request, 'compra/create_compra.html', {
                'form_articulo': ArticuloForm,
                'form_compra': CompraForm,
                'error': 'Please provide valid data'
            })
        
def update_compra(request, compra_id):
    if request.method == 'GET':
        compra = get_object_or_404(Compra, pk=compra_id, user=request.user)
        form = CompraForm(instance=compra)
        return render(request, 'compra/update_compra.html', {
            'compra': compra,
            'form': form
        })
    else:
        try:
            compra = get_object_or_404(Compra, pk=compra_id, user=request.user)
            form = CompraForm(request.POST, instance=compra)
            form.save()
            return redirect('compra')
        except ValueError:
            return render(request, 'compra/update_compra.html', {
                'compra': compra,
                'form': form,
                'error': 'Error updating compra'
            })
        
def delete_compra(request, compra_id):
    compra = get_object_or_404(Compra, pk=compra_id, user=request.user)
    if request.method == 'POST':
        compra.delete()
        return redirect('compra')

# Asignacion
def asignacion(request):
    asignacion = Asignacion.objects.filter()
    paginator = Paginator(asignacion, 10)  # Show 10 per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'asignacion/asignacion.html', {
        'asignacion': paginator.page(page_number),
        'page_obj': page_obj
    })
    
def create_asignacion(request):
    if request.method == 'GET':
        return render(request, 'asignacion/create_asignacion.html', {
            'form': AsignacionForm,
        })
    else:
        try:
            form_asignacion = AsignacionForm(request.POST)
            new_asignacion = form_asignacion.save(commit=False)
            new_asignacion.user = request.user
            new_asignacion.save()
            articulo = get_object_or_404(Articulo, pk=new_asignacion.articulo_id)
            articulo.asignado = True
            articulo.save()
            return redirect('asignacion')
        except ValueError:
            return render(request, 'asignacion/create_asignacion.html', {
                'form': AsignacionForm,
                'error': 'Please provide valid data'
            })
            
def delete_asignacion(request, asignacion_id):
    asignacion = get_object_or_404(Asignacion, pk=asignacion_id, user=request.user)
    if request.method == 'POST':
        asignacion.delete()
        return redirect('asignacion')

class SearchTecnologia(ListView):
    model = Articulo
    template_name = 'tecnologia/tecnologia.html'
    context_object_name = 'tecnologia'

    def get_queryset(self):
        option = self.request.GET.get('option')
        query = self.request.GET.get('q')
        if option == 'descripcion':
            return Articulo.objects.filter(tipo_articulo=1, descripcion__icontains=query, user=self.request.user)
        if option == 'marca':
            return Articulo.objects.filter(tipo_articulo=1, marca__icontains=query, user=self.request.user)
        if option == 'modelo':
            return Articulo.objects.filter(tipo_articulo=1, modelo__icontains=query, user=self.request.user)
        if option == 'serial':
            return Articulo.objects.filter(tipo_articulo=1, serial__icontains=query, user=self.request.user)
        if option == 'codigo_bn':
            return Articulo.objects.filter(tipo_articulo=1, codigo_bn__icontains=query, user=self.request.user)
        if option == 'cantidad':
            return Articulo.objects.filter(tipo_articulo=1, cantidad__icontains=query, user=self.request.user)
        #if option == 'condicion':
            #return Articulo.objects.filter(tipo_articulo=1, condicion__icontains=query, user=self.request.user)
        if option == 'fecha_adq':
            return Articulo.objects.filter(tipo_articulo=1, fecha_adq__icontains=query, user=self.request.user)
        #if option == 'fecha_adq':
            #return Articulo.objects.filter(tipo_articulo=1, fecha_adq__icontains=query, user=self.request.user)
            
class SearchConsumible(ListView):
    model = Articulo
    template_name = 'consumible/consumible.html'
    context_object_name = 'consumible'

    def get_queryset(self):
        option = self.request.GET.get('option')
        query = self.request.GET.get('q')
        if option == 'descripcion':
            return Articulo.objects.filter(tipo_articulo=2, descripcion__icontains=query, user=self.request.user)
        if option == 'marca':
            return Articulo.objects.filter(tipo_articulo=2, marca__icontains=query, user=self.request.user)
        if option == 'serial':
            return Articulo.objects.filter(tipo_articulo=2, serial__icontains=query, user=self.request.user)
        if option == 'cantidad':
            return Articulo.objects.filter(tipo_articulo=2, cantidad__icontains=query, user=self.request.user)
        #if option == 'condicion':
            #return Articulo.objects.filter(tipo_articulo=2, condicion__icontains=query, user=self.request.user)
        if option == 'fecha_adq':
            return Articulo.objects.filter(tipo_articulo=2, fecha_adq__icontains=query, user=self.request.user)
        #if option == 'fecha_adq':
            #return Articulo.objects.filter(tipo_articulo=2, fecha_adq__icontains=query, user=self.request.user)
            
class SearchMobiliario(ListView):
    model = Articulo
    template_name = 'mobiliario/mobiliario.html'
    context_object_name = 'mobiliario'

    def get_queryset(self):
        option = self.request.GET.get('option')
        query = self.request.GET.get('q')
        if option == 'descripcion':
            return Articulo.objects.filter(tipo_articulo=3, descripcion__icontains=query, user=self.request.user)
        if option == 'serial':
            return Articulo.objects.filter(tipo_articulo=3, serial__icontains=query, user=self.request.user)
        if option == 'codigo_bn':
            return Articulo.objects.filter(tipo_articulo=3, codigo_bn__icontains=query, user=self.request.user)
        if option == 'cantidad':
            return Articulo.objects.filter(tipo_articulo=3, cantidad__icontains=query, user=self.request.user)
        #if option == 'condicion':
            #return Articulo.objects.filter(tipo_articulo=3, condicion__icontains=query, user=self.request.user)
        if option == 'fecha_adq':
            return Articulo.objects.filter(tipo_articulo=3, fecha_adq__icontains=query, user=self.request.user)
        #if option == 'fecha_adq':
            #return Articulo.objects.filter(tipo_articulo=3, fecha_adq__icontains=query, user=self.request.user)
            
class SearchVehiculo(ListView):
    model = Articulo
    template_name = 'vehiculo/vehiculo.html'
    context_object_name = 'vehiculo'

    def get_queryset(self):
        option = self.request.GET.get('option')
        query = self.request.GET.get('q')
        if option == 'descripcion':
            return Articulo.objects.filter(tipo_articulo=4, descripcion__icontains=query, user=self.request.user)
        if option == 'marca':
            return Articulo.objects.filter(tipo_articulo=4, marca__icontains=query, user=self.request.user)
        if option == 'modelo':
            return Articulo.objects.filter(tipo_articulo=4, modelo__icontains=query, user=self.request.user)
        if option == 'codigo_bn':
            return Articulo.objects.filter(tipo_articulo=4, codigo_bn__icontains=query, user=self.request.user)
        if option == 'placa':
            return Articulo.objects.filter(tipo_articulo=4, placa__icontains=query, user=self.request.user)
        if option == 'cantidad':
            return Articulo.objects.filter(tipo_articulo=4, cantidad__icontains=query, user=self.request.user)
        #if option == 'condicion':
            #return Articulo.objects.filter(tipo_articulo=4, condicion__icontains=query, user=self.request.user)
        if option == 'fecha_adq':
            return Articulo.objects.filter(tipo_articulo=4, fecha_adq__icontains=query, user=self.request.user)
        #if option == 'fecha_adq':
            #return Articulo.objects.filter(tipo_articulo=4, fecha_adq__icontains=query, user=self.request.user)