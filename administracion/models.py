from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Condicion(models.Model):
    nombre = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
    
class TipoArticulo(models.Model):
    nombre = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    descripcion = models.TextField(max_length=255)
    marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    serial = models.CharField(max_length=255)
    placa = models.CharField(max_length=255)
    codigo_bn = models.CharField(max_length=255)
    cantidad = models.IntegerField()
    tipo_articulo = models.ForeignKey(TipoArticulo, on_delete=models.CASCADE)
    condicion = models.ForeignKey(Condicion, on_delete=models.CASCADE)
    fecha_adq = models.DateField()
    asignado = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.descripcion
    
class TipoAveria(models.Model):
    nombre = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
    
class Departamento(models.Model):
    nombre = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
    
class Averia(models.Model):
    problema = models.TextField(max_length=255)
    tipo_averia = models.ForeignKey(TipoAveria, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    ubicacion = models.TextField(max_length=255)
    serial = models.CharField(max_length=255)
    codigo_bn = models.CharField(max_length=255)

    def __str__(self):
        return self.problema
    
class Asignacion(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    descripcion = models.TextField(max_length=255)
    observaciones = models.TextField(max_length=255)

class Compra(models.Model):
    descripcion = models.TextField(max_length=255)
    marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    serial = models.CharField(max_length=255)
    placa = models.CharField(max_length=255)
    codigo_bn = models.CharField(max_length=255)
    n_orden = models.IntegerField()
    valor_bs = models.IntegerField()
    cantidad = models.IntegerField()
    fecha_adq = models.DateField()
    tipo_articulo = models.ForeignKey(TipoArticulo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
