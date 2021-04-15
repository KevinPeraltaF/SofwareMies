from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .models import Zona, Provincia, Distrito
from .forms import DistritoForm, ProvinciaForm,ZonaForm
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
# ------------------------------ZONA
class ZonaListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'ubicacion.view_zona'
    model = Zona
    template_name = "ubicacion/ubicacion_zona_listado.html"

 
    
class ZonaCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'ubicacion.add_zona'
    model = Zona
    form_class = ZonaForm
    template_name = "ubicacion/ubicacion_zona_crear.html"
    success_url = reverse_lazy('zona_listar')
   

class ZonaDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'ubicacion.delete_zona'
    model = Zona
    template_name = "ubicacion/ubicacion_zona_eliminar.html"
    success_url = reverse_lazy('zona_listar')
   


class ZonaUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'ubicacion.change_zona'
    model = Zona
    form_class = ZonaForm
    template_name = "ubicacion/ubicacion_zona_editar.html"
    success_url = reverse_lazy('zona_listar')
   

    
class ZonaDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'ubicacion.view_zona'
    model = Zona
    template_name = "ubicacion/ubicacion_zona_detalle.html"

#----------------------------------- provincia
class ProvinciaListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'ubicacion.view_provincia'
    model = Provincia
    template_name = "ubicacion/ubicacion_provincia_listado.html"

   
class ProvinciaCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'ubicacion.add_provincia'
    model = Provincia
    form_class = ProvinciaForm
    template_name = "ubicacion/ubicacion_provincia_crear.html"
    success_url = reverse_lazy('provincia_listar')
 


class ProvinciaDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'ubicacion.delete_provincia'
    model = Provincia
    template_name = "ubicacion/ubicacion_provincia_eliminar.html"
    success_url = reverse_lazy('provincia_listar')
 


class ProvinciaUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'ubicacion.change_provincia'
    model = Provincia
    form_class = ProvinciaForm
    template_name = "ubicacion/ubicacion_provincia_editar.html"
    success_url = reverse_lazy('provincia_listar')
   

    
class ProvinciaDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'ubicacion.view_provincia'
    model = Provincia
    template_name = "ubicacion/ubicacion_provincia_detalle.html"



# ------------------------------DISTRITO
class DistritoListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'ubicacion.view_distrito'
    model = Distrito
    template_name = "ubicacion/ubicacion_distrito_listado.html"


    
class DistritoCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'ubicacion.add_distrito'
    model = Distrito
    form_class = DistritoForm
    template_name = "ubicacion/ubicacion_distrito_crear.html"
    success_url = reverse_lazy('distrito_listar')
    

class DistritoDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'ubicacion.delete_distrito'
    model = Distrito
    template_name = "ubicacion/ubicacion_distrito_eliminar.html"
    success_url = reverse_lazy('distrito_listar')
  


class DistritoUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'ubicacion.change_distrito'
    model = Distrito
    form_class = DistritoForm
    template_name = "ubicacion/ubicacion_distrito_editar.html"
    success_url = reverse_lazy('distrito_listar')
 
    
class DistritoDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'ubicacion.view_distrito'
    model = Distrito
    template_name = "ubicacion/ubicacion_distrito_detalle.html"

