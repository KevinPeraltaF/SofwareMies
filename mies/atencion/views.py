from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .models import Atencion, AtencionDetalle
from .forms import AtencionForm, AtencionDetalleForm, DetalleForm
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
    
    def get(self, request,*args,**kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_form = DetalleForm()
        return self.render_to_response(
            self.get_context_data(form=form, detalle_form=detalle_form)
        )
    
    def post(self, request,*args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_form = DetalleForm(self.request.POST)
        if (form.is_valid() and detalle_form.is_valid()):
            return self.form_valid(form, detalle_form)
        else:
            return self.form_invalid(form, detalle_form)

    def form_valid(self, form, detalle_form):
        cabecera = form.save()
        detalle_form.instance = cabecera
        detalle_form.save()
        cabecera.save()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form, detalle_form):
        return self.render_to_response(
            self.get_context_data(form = form, detalle_form=detalle_form)
        )



class AtencionDeleteView(LoginRequiredMixin,DeleteView):
    model = AtencionDetalle
    template_name = "atencion/atencion_eliminar.html"
    success_url = reverse_lazy('Atencion_listar')
   

class AtencionUpdateView(LoginRequiredMixin,UpdateView):
    model = AtencionDetalle
    form_class = AtencionDetalleForm
    second_form__class= AtencionForm
    template_name = "atencion/atencion_editar.html"
    success_url = reverse_lazy('Atencion_listar')


    
class AtencionDetailView(LoginRequiredMixin,DetailView):
    model = Atencion
    template_name = "atencion/atencion_detalle.html"
    # additional parameters

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = AtencionDetalle.objects.filter(cabecera=self.object.id)
        return context


class ReporteAtencionPdfView(LoginRequiredMixin,PdfMixin, DetailView):
    model = Atencion
    template_name = "atencion/atencion_reporte_pdf.html"


class ReporteActaEntregaPdfView(LoginRequiredMixin,PdfMixin,DetailView):
    model = Atencion
    template_name = "atencion/acta_entrega_pdf.html"
    # additional parameters

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = AtencionDetalle.objects.filter(cabecera=self.object.id)
        return context