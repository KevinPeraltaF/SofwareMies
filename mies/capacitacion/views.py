from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .models import  CapacitacionCabecera, CapacitacionDetalle
from .forms import  CapacitacionCabeceraForm, CapacitacionCabDetalleForm, CapacitacionDetalleForm

from django.contrib.auth.mixins import PermissionRequiredMixin,LoginRequiredMixin
from django.http import HttpRequest
from django.utils.decorators import method_decorator
#pdf libreria
from django_xhtml2pdf.views import PdfMixin
#
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, JsonResponse
# Create your views here.
class CapacitacionListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'capacitacion.view_capacitacion'
    model = CapacitacionCabecera
    template_name = "capacitacion/capacitacion_listado.html"
    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args, **kwargs):
        return super().dispatch(request,*args, **kwargs)

class CapacitacionCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'capacitacion.add_capacitacion'
    model = CapacitacionCabecera
    form_class = CapacitacionCabeceraForm
    template_name = "capacitacion/capacitacion_crear.html"
    success_url = reverse_lazy('capacitacion_listar')

    def get(self, request,*args,**kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_form = CapacitacionCabDetalleForm()
        return self.render_to_response(
            self.get_context_data(form=form, detalle_form=detalle_form)
        )
    
    def post(self, request,*args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_form = CapacitacionCabDetalleForm(self.request.POST)
        if (form.is_valid() and detalle_form.is_valid()):
            return self.form_valid(form, detalle_form)
        else:
            return self.form_invalid(form, detalle_form)

    def form_valid(self, form, detalle_form):
        cabecera = form.save()
        detalle_form.instance = cabecera
        detalle_form.save()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form, detalle_form):
        return self.render_to_response(
            self.get_context_data(form = form, detalle_form=detalle_form)
        )
   

class CapacitacionDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'capacitacion.delete_capacitacion'
    model = CapacitacionCabecera
    template_name = "capacitacion/capacitacion_eliminar.html"
    success_url = reverse_lazy('capacitacion_listar')
   


class CapacitacionUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'capacitacion.change_capacitacion'
    model = CapacitacionCabecera
    form_class = CapacitacionCabeceraForm
    template_name = "capacitacion/capacitacion_editar.html"
    success_url = reverse_lazy('capacitacion_listar')

    def get(self, request,*args,**kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_form = CapacitacionCabDetalleForm(instance = self.object)
        return self.render_to_response(
            self.get_context_data(form=form, detalle_form=detalle_form)
        )
    
    def post(self, request,*args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_form = CapacitacionCabDetalleForm(self.request.POST,instance=self.get_object())
        if (form.is_valid() and detalle_form.is_valid()):
            return self.form_valid(form, detalle_form)
        else:
            return self.form_invalid(form, detalle_form)

    def form_valid(self, form, detalle_form):
        cabecera = form.save()
        detalle_form.instance = cabecera
        detalle_form.save()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form, detalle_form):
        return self.render_to_response(
            self.get_context_data(form = form, detalle_form=detalle_form)
        )   


    
class CapacitacionDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'capacitacion.view_capacitacion'
    model = CapacitacionCabecera
    template_name = "capacitacion/capacitacion_detalle.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = CapacitacionDetalle.objects.filter(capacitacionCabecera=self.object.id)
        return context

####   REPORTE CAPACITACION PDF
class CapacitacionReportePdfDetailView(LoginRequiredMixin,PdfMixin, DetailView):
    model = CapacitacionCabecera
    template_name = "capacitacion/capacitacion_reporte_pdf.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = CapacitacionDetalle.objects.filter(capacitacionCabecera=self.object.id)
        return context

