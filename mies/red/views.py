from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .models import AccesoRed
from .forms import AccesoRedForm

from django.contrib.auth.mixins import PermissionRequiredMixin,LoginRequiredMixin
from django.http import HttpRequest
from django.utils.decorators import method_decorator

# Create your views here.
class AccesoRedListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'red.view_accesored'
    model = AccesoRed
    template_name = "red/acceso_red_listado.html"
    

class AccesoRedCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'red.add_accesored'
    model = AccesoRed
    form_class = AccesoRedForm
    template_name = "red/acceso_red_crear.html"
    success_url = reverse_lazy('accesoRed_listar')
   

class AccesoRedDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'red.delete_accesored'
    model = AccesoRed
    template_name = "red/acceso_red_eliminar.html"
    success_url = reverse_lazy('accesoRed_listar')
   


class AccesoRedUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'red.change_accesored'
    model = AccesoRed
    form_class = AccesoRedForm
    template_name = "red/acceso_red_editar.html"
    success_url = reverse_lazy('accesoRed_listar')


    
class AccesoRedDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'red.view_accesored'
    model = AccesoRed
    template_name = "red/acceso_red_detalle.html"

