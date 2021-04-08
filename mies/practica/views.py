from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .models import Pasante, Carrera, Universidad
from .forms import PasanteForm, CarreraForm, UniversidadForm
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.utils.decorators import method_decorator

# VISTA PASANTE.
class PasanteListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'practica.view_pasante'
    model = Pasante
    template_name = "practica/pasante_listado.html"


    
class PasanteCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'practica.add_pasante'
    model = Pasante
    form_class = PasanteForm
    template_name = "practica/pasante_crear.html"
    success_url = reverse_lazy('pasante_listar')
 


class PasanteDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'practica.delete_pasante'
    model = Pasante
    template_name = "practica/pasante_eliminar.html"
    success_url = reverse_lazy('pasante_listar')
   


class PasanteUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'practica.change_pasante'
    model = Pasante
    form_class = PasanteForm
    template_name = "practica/pasante_editar.html"
    success_url = reverse_lazy('pasante_listar')
 

    
class PasanteDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'practica.view_pasante'
    model = Pasante
    template_name = "practica/pasante_detalle.html"

# VISTA CARRERA.
class CarreraListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'practica.view_carrera'
    model = Carrera
    template_name = "practica/carrera_listado.html"


    
class CarreraCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'practica.add_carrera'
    model = Carrera
    form_class = CarreraForm
    template_name = "practica/carrera_crear.html"
    success_url = reverse_lazy('carrera_listar')
    


class CarreraDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'practica.delete_carrera'
    model = Carrera
    template_name = "practica/carrera_eliminar.html"
    success_url = reverse_lazy('carrera_listar')
   


class CarreraUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'practica.change_carrera'
    model = Carrera
    form_class = CarreraForm
    template_name = "practica/carrera_editar.html"
    success_url = reverse_lazy('carrera_listar')
 

    
class CarreraDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'practica.view_carrera'
    model = Carrera
    template_name = "practica/carrera_detalle.html"

# VISTA UNIVERSIDAD.
class UniversidadListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'practica.view_universidad'
    model = Universidad
    template_name = "practica/universidad_listado.html"

 
    
class UniversidadCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'practica.add_universidad'
    model = Universidad
    form_class = UniversidadForm
    template_name = "practica/universidad_crear.html"
    success_url = reverse_lazy('universidad_listar')
 

class UniversidadDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'practica.delete_universidad'
    model = Universidad
    template_name = "practica/universidad_eliminar.html"
    success_url = reverse_lazy('universidad_listar')
  

class UniversidadUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'practica.change_universidad'
    model = Universidad
    form_class = UniversidadForm
    template_name = "practica/universidad_editar.html"
    success_url = reverse_lazy('universidad_listar')
  
    
class UniversidadDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'practica.view_universidad'
    model = Universidad
    template_name = "practica/universidad_detalle.html"


