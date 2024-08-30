from django.shortcuts import render, redirect, get_object_or_404
from .models import Articulo, Averia, Compra, Asignacion
from .forms import TecnologiaForm, ConsumibleForm, MobiliarioForm, VehiculoForm, AveriaForm, CompraForm, AsignacionForm
from django.core.paginator import Paginator

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
    return render(request, 'tecnologia.html', {
        'tecnologia': paginator.page(page_number),
        'page_obj': page_obj
    })

def create_tecnologia(request):
    if request.method == 'GET':
        return render(request, 'create_tecnologia.html', {
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
            return render(request, 'create_tecnologia.html', {
                'form': TecnologiaForm,
                'error': 'Please provide valid data'
            })

def update_tecnologia(request, tecnologia_id):
    if request.method == 'GET':
        tecnologia = get_object_or_404(Articulo, pk=tecnologia_id, user=request.user)
        form = TecnologiaForm(instance=tecnologia)
        return render(request, 'update_tecnologia.html', {
            'tecnologia': tecnologia,
            'form': form
        })
    else:
        try:
            tecnologia = get_object_or_404(Articulo, pk=tecnologia_id, user=request.user)
            form = TecnologiaForm(request.POST, instance=tecnologia)
            form.save()
            return redirect('tecnologia')
        except ValueError:
            return render(request, 'update_tecnologia.html', {
                'tecnologia': tecnologia,
                'form': form,
                'error': 'Error updating tecnologia'
            })

def delete_tecnologia(request, tecnologia_id):
    tecnologia = get_object_or_404(Articulo, pk=tecnologia_id, user=request.user)
    if request.method == 'POST':
        tecnologia.delete()
        return redirect('tecnologia') 

# Consumible    
def consumible(request):
    consumible = Articulo.objects.filter(tipo_articulo=2)
    paginator = Paginator(consumible, 10)  # Show 10 per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'consumible.html', {
        'consumible': paginator.page(page_number),
        'page_obj': page_obj
    })

def create_consumible(request):
    if request.method == 'GET':
        return render(request, 'create_consumible.html', {
            'form': ConsumibleForm
        })
    else:
        try:
            form = ConsumibleForm(request.POST)
            new_consumible = form.save(commit=False)
            new_consumible.user = request.user
            new_consumible.tipo_articulo_id = 2
            new_consumible.save()
            return redirect('consumible')
        except ValueError:
            return render(request, 'create_consumible.html', {
                'form': ConsumibleForm,
                'error': 'Please provide valid data'
            })
        
def update_consumible(request, consumible_id):
    if request.method == 'GET':
        consumible = get_object_or_404(Articulo, pk=consumible_id, user=request.user)
        form = ConsumibleForm(instance=consumible)
        return render(request, 'update_consumible.html', {
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
            return render(request, 'update_consumible.html', {
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
    return render(request, 'mobiliario.html', {
        'mobiliario': paginator.page(page_number),
        'page_obj': page_obj
    })

def create_mobiliario(request):
    if request.method == 'GET':
        return render(request, 'create_mobiliario.html', {
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
            return render(request, 'create_mobiliario.html', {
                'form': MobiliarioForm,
                'error': 'Please provide valid data'
            })
        
def update_mobiliario(request, mobiliario_id):
    if request.method == 'GET':
        mobiliario = get_object_or_404(Articulo, pk=mobiliario_id, user=request.user)
        form = MobiliarioForm(instance=mobiliario)
        return render(request, 'update_mobiliario.html', {
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
            return render(request, 'update_mobiliario.html', {
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
    return render(request, 'vehiculo.html', {
        'vehiculo': paginator.page(page_number),
        'page_obj': page_obj
    })

def create_vehiculo(request):
    if request.method == 'GET':
        return render(request, 'create_vehiculo.html', {
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
            return render(request, 'create_vehiculo.html', {
                'form': VehiculoForm,
                'error': 'Please provide valid data'
            })
        
def update_vehiculo(request, vehiculo_id):
    if request.method == 'GET':
        vehiculo = get_object_or_404(Articulo, pk=vehiculo_id, user=request.user)
        form = VehiculoForm(instance=vehiculo)
        return render(request, 'update_vehiculo.html', {
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
            return render(request, 'update_vehiculo.html', {
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
