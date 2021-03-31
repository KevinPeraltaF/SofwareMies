from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .models import Prestamo
from .forms import PrestamoForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class PrestamoListView(ListView):
    model = Prestamo
    template_name = "prestamo/prestamo_listado.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PrestamoListView, self).dispatch(*args, **kwargs)
    
class PrestamoCreateView(CreateView):
    model = Prestamo
    form_class = PrestamoForm
    template_name = "prestamo/prestamo_crear.html"
    success_url = reverse_lazy('prestamo_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PrestamoCreateView, self).dispatch(*args, **kwargs)


class PrestamoDeleteView(DeleteView):
    model = Prestamo
    template_name = "prestamo/prestamo_eliminar.html"
    success_url = reverse_lazy('prestamo_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PrestamoDeleteView, self).dispatch(*args, **kwargs)


class PrestamoUpdateView(UpdateView):
    model = Prestamo
    form_class = PrestamoForm
    template_name = "prestamo/prestamo_editar.html"
    success_url = reverse_lazy('prestamo_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PrestamoUpdateView, self).dispatch(*args, **kwargs)

    
class PrestamoDetailView(DetailView):
    model = Prestamo
    template_name = "prestamo/prestamo_detalle.html"

