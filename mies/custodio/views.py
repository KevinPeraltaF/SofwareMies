from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .models import Custodio
from .forms import CustodioForm
from django.contrib.auth.mixins import PermissionRequiredMixin,LoginRequiredMixin

# Create your views here.
class CustodioListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'custodio.view_custodio'
    model = Custodio
    template_name = "custodio/custodio_listado.html"

    #def get_queryset(self):
     #   return Custodio.objects.exclude(estado = 0)
    

class CustodioCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'custodio.add_custodio'
    model = Custodio
    form_class = CustodioForm
    template_name = "custodio/custodio_crear.html"
    success_url = reverse_lazy('custodio_listar')
   

class CustodioDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'custodio.delete_custodio'
    model = Custodio
    template_name = "custodio/custodio_eliminar.html"
    success_url = reverse_lazy('custodio_listar')
   


class CustodioUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'custodio.change_custodio'
    model = Custodio
    form_class = CustodioForm
    template_name = "custodio/custodio_editar.html"
    success_url = reverse_lazy('custodio_listar')


    
class CustodioDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'custodio.view_custodio'
    model = Custodio
    template_name = "custodio/custodio_detalle.html"

