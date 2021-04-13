from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .models import Prestamo
from .forms import PrestamoForm
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.utils.decorators import method_decorator

# Create your views here.
class PrestamoListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'prestamo.view_prestamo'
    model = Prestamo
    template_name = "prestamo/prestamo_listado.html"

    
class PrestamoCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'prestamo.add_prestamo'
    model = Prestamo
    form_class = PrestamoForm
    template_name = "prestamo/prestamo_crear.html"
    success_url = reverse_lazy('prestamo_listar')



class PrestamoDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'prestamo.delete_prestamo'
    model = Prestamo
    template_name = "prestamo/prestamo_eliminar.html"
    success_url = reverse_lazy('prestamo_listar')



class PrestamoUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'prestamo.change_prestamo'
    model = Prestamo
    form_class = PrestamoForm
    template_name = "prestamo/prestamo_editar.html"
    success_url = reverse_lazy('prestamo_listar')
 

    
class PrestamoDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'prestamo.view_prestamo'
    model = Prestamo
    template_name = "prestamo/prestamo_detalle.html"

