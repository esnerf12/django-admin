from django.contrib import admin
from .models import Condicion, TipoArticulo, Articulo, TipoAveria, Departamento, Averia, Asignacion, Compra, Sede

# Register your models here.
admin.site.register(Condicion)
admin.site.register(TipoArticulo)
admin.site.register(Articulo)
admin.site.register(TipoAveria)
admin.site.register(Departamento)
admin.site.register(Averia)
admin.site.register(Asignacion)
admin.site.register(Compra)
admin.site.register(Sede)
