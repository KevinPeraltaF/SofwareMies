from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .models import  TipoCapacitacion, CapacitacionCabecera, CapacitacionDetalle
from .forms import TipoCapacitacionForm, CapacitacionForm

from django.contrib.auth.mixins import PermissionRequiredMixin,LoginRequiredMixin
from django.http import HttpRequest
from django.utils.decorators import method_decorator
#pdf libreria
from django_xhtml2pdf.views import PdfMixin

# Create your views here.
class TipoCapacitacionListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'capacitacion.view_tipocapacitacion'
    model = TipoCapacitacion
    template_name = "capacitacion/tipo_capacitacion_listado.html"
    

class TipoCapacitacionCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'capacitacion.add_tipocapacitacion'
    model = TipoCapacitacion
    form_class = TipoCapacitacionForm
    template_name = "capacitacion/tipo_capacitacion_crear.html"
    success_url = reverse_lazy('tipo_capacitacion_listar')
   

class TipoCapacitacionDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'capacitacion.delete_tipocapacitacion'
    model = TipoCapacitacion
    template_name = "capacitacion/tipo_capacitacion_eliminar.html"
    success_url = reverse_lazy('tipo_capacitacion_listar')
   


class TipoCapacitacionUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'capacitacion.change_tipocapacitacion'
    model = TipoCapacitacion
    form_class = TipoCapacitacionForm
    template_name = "capacitacion/tipo_capacitacion_editar.html"
    success_url = reverse_lazy('tipo_capacitacion_listar')


    
class TipoCapacitacionDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'capacitacion.view_tipocapacitacion'
    model = TipoCapacitacion
    template_name = "capacitacion/tipo_capacitacion_detalle.html"




# Create your views here.
class CapacitacionListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'capacitacion.view_capacitacion'
    model = CapacitacionCabecera
    template_name = "capacitacion/capacitacion_listado.html"
    

class CapacitacionCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'capacitacion.add_capacitacion'
    model = CapacitacionCabecera
    form_class = CapacitacionForm
    template_name = "capacitacion/capacitacion_crear.html"
    success_url = reverse_lazy('capacitacion_listar')
   

class CapacitacionDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'capacitacion.delete_capacitacion'
    model = CapacitacionCabecera
    template_name = "capacitacion/_capacitacion_eliminar.html"
    success_url = reverse_lazy('capacitacion_listar')
   


class CapacitacionUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'capacitacion.change_capacitacion'
    model = CapacitacionCabecera
    form_class = CapacitacionForm
    template_name = "capacitacion/capacitacion_editar.html"
    success_url = reverse_lazy('capacitacion_listar')


    
class CapacitacionDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'capacitacion.view_capacitacion'
    model = CapacitacionCabecera
    template_name = "capacitacion/capacitacion_detalle.html"


####   REPORTE CAPACITACION PDF
class CapacitacionReportePdfDetailView(LoginRequiredMixin,PdfMixin, DetailView):
    model = CapacitacionCabecera
    template_name = "capacitacion/capacitacion_reporte_pdf.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = CapacitacionDetalle.objects.filter(capacitacionCabecera=self.object.id)
       
        return context

