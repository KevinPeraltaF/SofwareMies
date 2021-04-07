from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .models import Zona, Provincia, Distrito
from .forms import DistritoForm, ProvinciaForm,ZonaForm
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
# ------------------------------ZONA
class ZonaListView(LoginRequiredMixin,ListView):
    model = Zona
    template_name = "ubicacion/ubicacion_zona_listado.html"

 
    
class ZonaCreateView(LoginRequiredMixin,CreateView):
    model = Zona
    form_class = ZonaForm
    template_name = "ubicacion/ubicacion_zona_crear.html"
    success_url = reverse_lazy('zona_listar')
   

class ZonaDeleteView(LoginRequiredMixin,DeleteView):
    model = Zona
    template_name = "ubicacion/ubicacion_zona_eliminar.html"
    success_url = reverse_lazy('zona_listar')
   


class ZonaUpdateView(LoginRequiredMixin,UpdateView):
    model = Zona
    form_class = ZonaForm
    template_name = "ubicacion/ubicacion_zona_editar.html"
    success_url = reverse_lazy('zona_listar')
   

    
class ZonaDetailView(LoginRequiredMixin,DetailView):
    model = Zona
    template_name = "ubicacion/ubicacion_zona_detalle.html"

#----------------------------------- provincia
class ProvinciaListView(LoginRequiredMixin,ListView):
    model = Provincia
    template_name = "ubicacion/ubicacion_provincia_listado.html"

   
class ProvinciaCreateView(LoginRequiredMixin,CreateView):
    model = Provincia
    form_class = ProvinciaForm
    template_name = "ubicacion/ubicacion_provincia_crear.html"
    success_url = reverse_lazy('provincia_listar')
 


class ProvinciaDeleteView(LoginRequiredMixin,DeleteView):
    model = Provincia
    template_name = "ubicacion/ubicacion_provincia_eliminar.html"
    success_url = reverse_lazy('provincia_listar')
 


class ProvinciaUpdateView(LoginRequiredMixin,UpdateView):
    model = Provincia
    form_class = ProvinciaForm
    template_name = "ubicacion/ubicacion_provincia_editar.html"
    success_url = reverse_lazy('provincia_listar')
   

    
class ProvinciaDetailView(LoginRequiredMixin,DetailView):
    model = Provincia
    template_name = "ubicacion/ubicacion_provincia_detalle.html"



# ------------------------------DISTRITO
class DistritoListView(LoginRequiredMixin,ListView):
    model = Distrito
    template_name = "ubicacion/ubicacion_distrito_listado.html"


    
class DistritoCreateView(LoginRequiredMixin,CreateView):
    model = Distrito
    form_class = DistritoForm
    template_name = "ubicacion/ubicacion_distrito_crear.html"
    success_url = reverse_lazy('distrito_listar')
    

class DistritoDeleteView(LoginRequiredMixin,DeleteView):
    model = Distrito
    template_name = "ubicacion/ubicacion_distrito_eliminar.html"
    success_url = reverse_lazy('distrito_listar')
  


class DistritoUpdateView(LoginRequiredMixin,UpdateView):
    model = Distrito
    form_class = DistritoForm
    template_name = "ubicacion/ubicacion_distrito_editar.html"
    success_url = reverse_lazy('distrito_listar')
 
    
class DistritoDetailView(LoginRequiredMixin,DetailView):
    model = Distrito
    template_name = "ubicacion/ubicacion_distrito_detalle.html"

