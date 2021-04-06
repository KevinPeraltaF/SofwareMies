from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .models import Empleado, Area, Cargo, UnidadAtencion
from .forms import EmpleadoForm, AreaForm, CargoForm, UnidadAtencionForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator

# VISTA EMPLEADO.
class EmpleadoListView(LoginRequiredMixin,ListView):
    model = Empleado
    template_name = "empleado/empleado_listado.html"
    
class EmpleadoCreateView(LoginRequiredMixin,CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = "empleado/empleado_crear.html"
    success_url = reverse_lazy('empleado_listar')
  


class EmpleadoDeleteView(LoginRequiredMixin,DeleteView):
    model = Empleado
    template_name = "empleado/empleado_eliminar.html"
    success_url = reverse_lazy('empleado_listar')



class EmpleadoUpdateView(LoginRequiredMixin,UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = "empleado/empleado_editar.html"
    success_url = reverse_lazy('empleado_listar')

    
class EmpleadoDetailView(LoginRequiredMixin,DetailView):
    model = Empleado
    template_name = "empleado/empleado_detalle.html"

# VISTA AREA.
class AreaListView(LoginRequiredMixin,ListView):
    model = Area
    template_name = "empleado/area_listado.html"

class AreaCreateView(LoginRequiredMixin,CreateView):
    model = Area
    form_class = AreaForm
    template_name = "empleado/area_crear.html"
    success_url = reverse_lazy('area_listar')



class AreaDeleteView(LoginRequiredMixin,DeleteView):
    model = Area
    template_name = "empleado/area_eliminar.html"
    success_url = reverse_lazy('area_listar')



class AreaUpdateView(LoginRequiredMixin,UpdateView):
    model = Area
    form_class = AreaForm
    template_name = "empleado/area_editar.html"
    success_url = reverse_lazy('area_listar')


    
class AreaDetailView(LoginRequiredMixin,DetailView):
    model = Area
    template_name = "empleado/area_detalle.html"

# VISTA CARGO.
class CargoListView(LoginRequiredMixin,ListView):
    model = Cargo
    template_name = "empleado/cargo_listado.html"

    
class CargoCreateView(LoginRequiredMixin,CreateView):
    model = Cargo
    form_class = CargoForm
    template_name = "empleado/cargo_crear.html"
    success_url = reverse_lazy('cargo_listar')


class CargoDeleteView(LoginRequiredMixin,DeleteView):
    model = Cargo
    template_name = "empleado/cargo_eliminar.html"
    success_url = reverse_lazy('cargo_listar')


class CargoUpdateView(LoginRequiredMixin,UpdateView):
    model = Cargo
    form_class = CargoForm
    template_name = "empleado/cargo_editar.html"
    success_url = reverse_lazy('cargo_listar')

    
class CargoDetailView(LoginRequiredMixin,DetailView):
    model = Cargo
    template_name = "empleado/cargo_detalle.html"


# VISTA UNIDAD DE ATENCION.
class UnidadListView(LoginRequiredMixin,ListView):
    model = UnidadAtencion
    template_name = "empleado/unidad_listado.html"

    
class UnidadCreateView(LoginRequiredMixin,CreateView):
    model = UnidadAtencion
    form_class = UnidadAtencionForm
    template_name = "empleado/unidad_crear.html"
    success_url = reverse_lazy('unidad_listar')

class UnidadDeleteView(LoginRequiredMixin,DeleteView):
    model = UnidadAtencion
    template_name = "empleado/unidad_eliminar.html"
    success_url = reverse_lazy('unidad_listar')


class UnidadUpdateView(LoginRequiredMixin,UpdateView):
    model = UnidadAtencion
    form_class = UnidadAtencionForm
    template_name = "empleado/unidad_editar.html"
    success_url = reverse_lazy('unidad_listar')

    
class UnidadDetailView(LoginRequiredMixin,DetailView):
    model = UnidadAtencion
    template_name = "empleado/unidad_detalle.html"