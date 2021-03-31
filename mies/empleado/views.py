from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .models import Empleado, Area, Cargo, UnidadAtencion
from .forms import EmpleadoForm, AreaForm, Cargo, UnidadAtencionForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# VISTA EMPLEADO.
class EmpleadoListView(ListView):
    model = Empleado
    template_name = "empleado/empleado_listado.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EmpleadoListView, self).dispatch(*args, **kwargs)
    
class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = "empleado/empleado_crear.html"
    success_url = reverse_lazy('empleado_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EmpleadoCreateView, self).dispatch(*args, **kwargs)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleado/empleado_eliminar.html"
    success_url = reverse_lazy('empleado_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EmpleadoDeleteView, self).dispatch(*args, **kwargs)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = "empleado/empleado_editar.html"
    success_url = reverse_lazy('empleado_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EmpleadoUpdateView, self).dispatch(*args, **kwargs)

    
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleado/empleado_detalle.html"

# VISTA AREA.
class AreaListView(ListView):
    model = Area
    template_name = "empleado/area_listado.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AreaListView, self).dispatch(*args, **kwargs)
    
class AreaCreateView(CreateView):
    model = Area
    form_class = AreaForm
    template_name = "empleado/area_crear.html"
    success_url = reverse_lazy('area_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AreaCreateView, self).dispatch(*args, **kwargs)


class AreaDeleteView(DeleteView):
    model = Area
    template_name = "empleado/area_eliminar.html"
    success_url = reverse_lazy('area_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AreaDeleteView, self).dispatch(*args, **kwargs)


class AreaUpdateView(UpdateView):
    model = Area
    form_class = AreaForm
    template_name = "empleado/area_editar.html"
    success_url = reverse_lazy('area_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AreaUpdateView, self).dispatch(*args, **kwargs)

    
class AreaDetailView(DetailView):
    model = Area
    template_name = "empleado/area_detalle.html"

# VISTA CARGO.
class CargoListView(ListView):
    model = Cargo
    template_name = "empleado/cargo_listado.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CargoListView, self).dispatch(*args, **kwargs)
    
class CargoCreateView(CreateView):
    model = Cargo
    form_class = CargoForm
    template_name = "empleado/cargo_crear.html"
    success_url = reverse_lazy('cargo_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CargoCreateView, self).dispatch(*args, **kwargs)

class CargoDeleteView(DeleteView):
    model = Cargo
    template_name = "empleado/cargo_eliminar.html"
    success_url = reverse_lazy('cargo_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CargoDeleteView, self).dispatch(*args, **kwargs)

class CargoUpdateView(UpdateView):
    model = Cargo
    form_class = CargoForm
    template_name = "empleado/cargo_editar.html"
    success_url = reverse_lazy('cargo_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CargoUpdateView, self).dispatch(*args, **kwargs)
    
class CargoDetailView(DetailView):
    model = Cargo
    template_name = "empleado/cargo_detalle.html"