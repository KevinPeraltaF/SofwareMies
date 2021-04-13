from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .models import Empleado, Area, Cargo, UnidadAtencion
from .forms import EmpleadoForm, AreaForm, CargoForm, UnidadAtencionForm
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.utils.decorators import method_decorator

# VISTA EMPLEADO.
class EmpleadoListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'empleado.view_empleado'
    model = Empleado
    template_name = "empleado/empleado_listado.html"
    
class EmpleadoCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'empleado.add_empleado'
    model = Empleado
    form_class = EmpleadoForm
    template_name = "empleado/empleado_crear.html"
    success_url = reverse_lazy('empleado_listar')
  


class EmpleadoDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'empleado.delete_empleado'
    model = Empleado
    template_name = "empleado/empleado_eliminar.html"
    success_url = reverse_lazy('empleado_listar')



class EmpleadoUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'empleado.change_empleado'
    model = Empleado
    form_class = EmpleadoForm
    template_name = "empleado/empleado_editar.html"
    success_url = reverse_lazy('empleado_listar')

    
class EmpleadoDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'empleado.view_empleado'
    model = Empleado
    template_name = "empleado/empleado_detalle.html"

# VISTA AREA.
class AreaListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'empleado.view_area'
    model = Area
    template_name = "empleado/area_listado.html"

class AreaCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'empleado.add_area'
    model = Area
    form_class = AreaForm
    template_name = "empleado/area_crear.html"
    success_url = reverse_lazy('area_listar')



class AreaDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'empleado.delete_area'
    model = Area
    template_name = "empleado/area_eliminar.html"
    success_url = reverse_lazy('area_listar')



class AreaUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'empleado.change_area'
    model = Area
    form_class = AreaForm
    template_name = "empleado/area_editar.html"
    success_url = reverse_lazy('area_listar')


    
class AreaDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'empleado.view_area'
    model = Area
    template_name = "empleado/area_detalle.html"

# VISTA CARGO.
class CargoListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'empleado.view_cargo'
    model = Cargo
    template_name = "empleado/cargo_listado.html"

    
class CargoCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'empleado.add_cargo'
    model = Cargo
    form_class = CargoForm
    template_name = "empleado/cargo_crear.html"
    success_url = reverse_lazy('cargo_listar')


class CargoDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'empleado.delete_cargo'
    model = Cargo
    template_name = "empleado/cargo_eliminar.html"
    success_url = reverse_lazy('cargo_listar')


class CargoUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'empleado.change_cargo'
    model = Cargo
    form_class = CargoForm
    template_name = "empleado/cargo_editar.html"
    success_url = reverse_lazy('cargo_listar')

    
class CargoDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'empleado.view_cargo'
    model = Cargo
    template_name = "empleado/cargo_detalle.html"


# VISTA UNIDAD DE ATENCION.
class UnidadListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'empleado.view_unidadatencion'
    model = UnidadAtencion
    template_name = "empleado/unidad_listado.html"

    
class UnidadCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'empleado.add_unidadatencion'
    model = UnidadAtencion
    form_class = UnidadAtencionForm
    template_name = "empleado/unidad_crear.html"
    success_url = reverse_lazy('unidad_listar')

class UnidadDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'empleado.delete_unidadatencion'
    model = UnidadAtencion
    template_name = "empleado/unidad_eliminar.html"
    success_url = reverse_lazy('unidad_listar')


class UnidadUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'empleado.change_unidadatencion'
    model = UnidadAtencion
    form_class = UnidadAtencionForm
    template_name = "empleado/unidad_editar.html"
    success_url = reverse_lazy('unidad_listar')

    
class UnidadDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'empleado.view_unidadatencion'
    model = UnidadAtencion
    template_name = "empleado/unidad_detalle.html"