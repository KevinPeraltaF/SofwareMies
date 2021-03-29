from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .models import Empleado
from .forms import EmpleadoForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
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
# Create your views here.
