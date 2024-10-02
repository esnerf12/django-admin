"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from administracion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('bienes/tecnologia', views.tecnologia, name='tecnologia'),
    path('bienes/tecnologia/create/', views.create_tecnologia, name='create_tecnologia'),
    path('bienes/tecnologia/<int:tecnologia_id>/', views.update_tecnologia, name='update_tecnologia'),
    path('bienes/tecnologia/<int:tecnologia_id>/delete', views.delete_tecnologia, name='delete_tecnologia'),
    path('bienes/tecnologia/search', views.SearchTecnologia.as_view(), name='search_tecnologia'),
    path('bienes/consumible', views.consumible, name='consumible'),
    path('bienes/consumible/create/', views.create_consumible, name='create_consumible'),
    path('bienes/consumible/<int:consumible_id>/', views.update_consumible, name='update_consumible'),
    path('bienes/consumible/<int:consumible_id>/delete', views.delete_consumible, name='delete_consumible'),
    path('bienes/consumible/search', views.SearchConsumible.as_view(), name='search_consumible'),
    path('bienes/mobiliario', views.mobiliario, name='mobiliario'),
    path('bienes/mobiliario/create/', views.create_mobiliario, name='create_mobiliario'),
    path('bienes/mobiliario/<int:mobiliario_id>/', views.update_mobiliario, name='update_mobiliario'),
    path('bienes/mobiliario/<int:mobiliario_id>/delete', views.delete_mobiliario, name='delete_mobiliario'),
    path('bienes/mobiliario/search', views.SearchMobiliario.as_view(), name='search_mobiliario'),
    path('bienes/vehiculo', views.vehiculo, name='vehiculo'),
    path('bienes/vehiculo/create/', views.create_vehiculo, name='create_vehiculo'),
    path('bienes/vehiculo/<int:vehiculo_id>/', views.update_vehiculo, name='update_vehiculo'),
    path('bienes/vehiculo/<int:vehiculo_id>/delete', views.delete_vehiculo, name='delete_vehiculo'),
    path('bienes/vehiculo/search', views.SearchVehiculo.as_view(), name='search_vehiculo'),
    path('bienes/averia', views.averia, name='averia'),
    path('bienes/averia/create/', views.create_averia, name='create_averia'),
    path('bienes/averia/<int:averia_id>/', views.update_averia, name='update_averia'),
    path('bienes/averia/<int:averia_id>/delete', views.delete_averia, name='delete_averia'),
    path('bienes/averia/search', views.SearchAveria.as_view(), name='search_averia'),
    path('bienes/compra', views.compra, name='compra'),
    path('bienes/compra/create/', views.create_compra, name='create_compra'),
    path('bienes/compra/<int:compra_id>/', views.update_compra, name='update_compra'),
    path('bienes/compra/<int:compra_id>/delete', views.delete_compra, name='delete_compra'),
    path('bienes/compra/search', views.SearchCompra.as_view(), name='search_compra'),
    path('bienes/asignacion', views.asignacion, name='asignacion'),
    path('bienes/asignacion/create/', views.create_asignacion, name='create_asignacion'),
    path('bienes/asignacion/<int:asignacion_id>/', views.update_asignacion, name='update_asignacion'),
    path('bienes/asignacion/<int:asignacion_id>/delete', views.delete_asignacion, name='delete_asignacion'),
    path('bienes/asignacion/search', views.SearchAsignacion.as_view(), name='search_asignacion'),
]
