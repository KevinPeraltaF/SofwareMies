from django.shortcuts import render
from configuracion.models import Configuracion
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import PermissionRequiredMixin,LoginRequiredMixin
# Create your views here.
from django.urls import reverse_lazy
from configuracion.forms import ConfiguracionForm

class ConfiguracionListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'configuracion.view_configuracion'
    model = Configuracion
    template_name = "configuracion/configuracion_listado.html"
    success_url = reverse_lazy('configuracion_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["validador"] = Configuracion.objects.count()
        return context
    


class ConfiguracionUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'configuracion.change_configuracion'
    model = Configuracion
    form_class = ConfiguracionForm
    template_name = "configuracion/configuracion_editar.html"
    success_url = reverse_lazy('configuracion_listar')



class ConfiguracionCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'configuracion.add_configuracion'
    model = Configuracion
    form_class = ConfiguracionForm
    template_name = "configuracion/configuracion_crear.html"
    success_url = reverse_lazy('configuracion_listar')