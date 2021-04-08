from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .models import Prestamo
from .forms import PrestamoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator

# Create your views here.
class PrestamoListView(LoginRequiredMixin,ListView):
    model = Prestamo
    template_name = "prestamo/prestamo_listado.html"

    
class PrestamoCreateView(LoginRequiredMixin,CreateView):
    model = Prestamo
    form_class = PrestamoForm
    template_name = "prestamo/prestamo_crear.html"
    success_url = reverse_lazy('prestamo_listar')



class PrestamoDeleteView(LoginRequiredMixin,DeleteView):
    model = Prestamo
    template_name = "prestamo/prestamo_eliminar.html"
    success_url = reverse_lazy('prestamo_listar')



class PrestamoUpdateView(LoginRequiredMixin,UpdateView):
    model = Prestamo
    form_class = PrestamoForm
    template_name = "prestamo/prestamo_editar.html"
    success_url = reverse_lazy('prestamo_listar')
 

    
class PrestamoDetailView(LoginRequiredMixin,DetailView):
    model = Prestamo
    template_name = "prestamo/prestamo_detalle.html"

