from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .models import Pasante, Carrera, Universidad
from .forms import PasanteForm, CarreraForm, UniversidadForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator

# VISTA PASANTE.
class PasanteListView(LoginRequiredMixin,ListView):
    model = Pasante
    template_name = "practica/pasante_listado.html"


    
class PasanteCreateView(LoginRequiredMixin,CreateView):
    model = Pasante
    form_class = PasanteForm
    template_name = "practica/pasante_crear.html"
    success_url = reverse_lazy('pasante_listar')
 


class PasanteDeleteView(LoginRequiredMixin,DeleteView):
    model = Pasante
    template_name = "practica/pasante_eliminar.html"
    success_url = reverse_lazy('pasante_listar')
   


class PasanteUpdateView(LoginRequiredMixin,UpdateView):
    model = Pasante
    form_class = PasanteForm
    template_name = "practica/pasante_editar.html"
    success_url = reverse_lazy('pasante_listar')
 

    
class PasanteDetailView(LoginRequiredMixin,DetailView):
    model = Pasante
    template_name = "practica/pasante_detalle.html"

# VISTA CARRERA.
class CarreraListView(LoginRequiredMixin,ListView):
    model = Carrera
    template_name = "practica/carrera_listado.html"


    
class CarreraCreateView(LoginRequiredMixin,CreateView):
    model = Carrera
    form_class = CarreraForm
    template_name = "practica/carrera_crear.html"
    success_url = reverse_lazy('carrera_listar')
    


class CarreraDeleteView(LoginRequiredMixin,DeleteView):
    model = Carrera
    template_name = "practica/carrera_eliminar.html"
    success_url = reverse_lazy('carrera_listar')
   


class CarreraUpdateView(LoginRequiredMixin,UpdateView):
    model = Carrera
    form_class = CarreraForm
    template_name = "practica/carrera_editar.html"
    success_url = reverse_lazy('carrera_listar')
 

    
class CarreraDetailView(LoginRequiredMixin,DetailView):
    model = Carrera
    template_name = "practica/carrera_detalle.html"

# VISTA UNIVERSIDAD.
class UniversidadListView(LoginRequiredMixin,ListView):
    model = Universidad
    template_name = "practica/universidad_listado.html"

 
    
class UniversidadCreateView(LoginRequiredMixin,CreateView):
    model = Universidad
    form_class = UniversidadForm
    template_name = "practica/universidad_crear.html"
    success_url = reverse_lazy('universidad_listar')
 

class UniversidadDeleteView(LoginRequiredMixin,DeleteView):
    model = Universidad
    template_name = "practica/universidad_eliminar.html"
    success_url = reverse_lazy('universidad_listar')
  

class UniversidadUpdateView(LoginRequiredMixin,UpdateView):
    model = Universidad
    form_class = UniversidadForm
    template_name = "practica/universidad_editar.html"
    success_url = reverse_lazy('universidad_listar')
  
    
class UniversidadDetailView(LoginRequiredMixin,DetailView):
    model = Universidad
    template_name = "practica/universidad_detalle.html"


