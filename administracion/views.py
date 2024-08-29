from django.shortcuts import render, redirect, get_object_or_404
from .models import Articulo, Averia, Asignacion, Compra
from .forms import TecnologiaForm, ConsumibleForm, MobiliarioForm, VehiculoForm, AveriaForm, CompraForm, AsignacionForm
from django.core.paginator import Paginator

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def tecnologia(request):
    tecnologia = Articulo.objects.filter(tipo_articulo=1)
    paginator = Paginator(tecnologia, 10)  # Show 20 emergencies per page.

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
                'error': 'Error updating emergency'
            })

def delete_tecnologia(request, tecnologia_id):
    tecnologia = get_object_or_404(Articulo, pk=tecnologia_id, user=request.user)
    if request.method == 'POST':
        tecnologia.delete()
        return redirect('tecnologia')