from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .models import Atencion, AtencionDetalle
from .forms import AtencionForm, AtencionDetalleForm
from empleado.models import Empleado
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.http import  HttpResponseRedirect, HttpResponse
from django_xhtml2pdf.views import PdfMixin

# Create your views here.
class AtencionListView(LoginRequiredMixin,ListView):
    model = Atencion
    template_name = "atencion/atencion_listado.html"

    
class AtencionCreateView(LoginRequiredMixin,CreateView):
    model = Atencion
    form_class = AtencionForm
    template_name = "atencion/atencion_crear.html"
    success_url = reverse_lazy('atencion_listar')

class AtencionDeleteView(LoginRequiredMixin,DeleteView):
    model = Atencion
    template_name = "atencion/atencion_eliminar.html"
    success_url = reverse_lazy('atencion_listar')
   

class AtencionUpdateView(LoginRequiredMixin,UpdateView):
    model = AtencionDetalle
    form_class = AtencionDetalleForm
    second_form__class= AtencionForm
    template_name = "atencion/atencion_editar.html"
    success_url = reverse_lazy('atencion_listar')


    
class AtencionDetailView(LoginRequiredMixin,DetailView):
    model = Atencion
    template_name = "atencion/atencion_detalle.html"
    # additional parameters

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = AtencionDetalle.objects.filter(cabecera=self.object.id)
        return context
####-ATENCION
class ReporteActaEntregaPdfView(LoginRequiredMixin,PdfMixin,DetailView):
    model = Atencion
    template_name = "atencion/acta_entrega_pdf.html"
    # additional parameters

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = AtencionDetalle.objects.filter(cabecera=self.object.id)
        return context

class ReporteAtencionPdfView(LoginRequiredMixin,PdfMixin, DetailView):
    model = Atencion
    template_name = "atencion/atencion_reporte_pdf.html"

####-BIENES
class ReporteBienesPdfView(LoginRequiredMixin,PdfMixin, DetailView):
    model = Atencion
    template_name = "atencion/acta_bienes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bienes'] = Empleado.objects.get(id=4)
        context['items'] = AtencionDetalle.objects.filter(cabecera=self.object.id)

        return context


####ENTREGA
class ReporteEntregaPdfView(LoginRequiredMixin,PdfMixin, DetailView):
    model = Atencion
    template_name = "atencion/acta_entrega.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = AtencionDetalle.objects.filter(cabecera=self.object.id)

        return context

####   RECEPCION
class ReporteRecepcionPdfView(LoginRequiredMixin,PdfMixin, DetailView):
    model = Atencion
    template_name = "atencion/acta_recepcion.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = AtencionDetalle.objects.filter(cabecera=self.object.id)
       
        return context



