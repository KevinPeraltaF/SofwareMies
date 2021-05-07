from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .models import Atencion, AtencionDetalle, AtencionSecundaria , AtencionSecundariaDetalle
from .forms import AtencionForm, AtencionDetalleForm,AtencionCabDetalleForm, AtencionSecundariaForm,AtencionDetalleSecundariaForm,AtencionCabDetalleSecundariaForm
from empleado.models import Empleado
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.http import  HttpResponseRedirect, HttpResponse
from django_xhtml2pdf.views import PdfMixin
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
class AtencionListView(LoginRequiredMixin,ListView):
    model = Atencion
    template_name = "atencion/atencion_listado.html"
    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args, **kwargs):
        return super().dispatch(request,*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['atencionSecundaria'] = AtencionSecundaria.objects.all()
        return context

    
class AtencionCreateView(LoginRequiredMixin,CreateView):
    model = Atencion
    form_class = AtencionForm
    template_name = "atencion/atencion_crear.html"
    success_url = reverse_lazy('atencion_listar')

    def get(self, request,*args,**kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_form = AtencionCabDetalleForm()
        return self.render_to_response(
            self.get_context_data(form=form, detalle_form=detalle_form)
        )
    
    def post(self, request,*args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_form = AtencionCabDetalleForm(self.request.POST)
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
   

class AtencionDeleteView(LoginRequiredMixin,DeleteView):
    model = Atencion
    template_name = "atencion/atencion_eliminar.html"
    success_url = reverse_lazy('atencion_listar')
   

class AtencionUpdateView(LoginRequiredMixin,UpdateView):
    permission_required = 'atencion.change_atencion'
    model = Atencion
    form_class =  AtencionForm 
    template_name = "atencion/atencion_editar.html"
    success_url = reverse_lazy('atencion_listar')

    def get(self, request,*args,**kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_form = AtencionCabDetalleForm(instance = self.object)
        return self.render_to_response(
            self.get_context_data(form=form, detalle_form=detalle_form)
        )
    
    def post(self, request,*args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_form = AtencionCabDetalleForm(self.request.POST,instance=self.get_object())
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
        #context['bienes'] = Empleado.objects.get(id=4)
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





#atencion secundaria

class AtencionSecundariaListView(LoginRequiredMixin,ListView):
    model = AtencionSecundaria
    template_name = "atencion/atencion_listado.html"
    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args, **kwargs):
        return super().dispatch(request,*args, **kwargs)
    
class AtencionSecundariaCreateView(LoginRequiredMixin,CreateView):
    model = AtencionSecundaria
    form_class = AtencionSecundariaForm
    template_name = "atencion/atencion_crear.html"
    success_url = reverse_lazy('atencion_listar')

    def get(self, request,*args,**kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_form = AtencionCabDetalleForm()
        return self.render_to_response(
            self.get_context_data(form=form, detalle_form=detalle_form)
        )
    
    def post(self, request,*args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_form = AtencionCabDetalleForm(self.request.POST)
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
   

class AtencionSecundariaDeleteView(LoginRequiredMixin,DeleteView):
    model = AtencionSecundaria
    template_name = "atencion/atencion_eliminar.html"
    success_url = reverse_lazy('atencion_listar')
   

class AtencionSecundariaUpdateView(LoginRequiredMixin,UpdateView):
    permission_required = 'atencion.change_atencionsecundaria'
    model = AtencionSecundaria
    form_class =  AtencionSecundariaForm 
    template_name = "atencion/atencion_editar.html"
    success_url = reverse_lazy('atencion_listar')

    def get(self, request,*args,**kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_form = AtencionCabDetalleForm(instance = self.object)
        return self.render_to_response(
            self.get_context_data(form=form, detalle_form=detalle_form)
        )
    
    def post(self, request,*args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_form = AtencionCabDetalleForm(self.request.POST,instance=self.get_object())
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



    
class AtencionSecundariaDetailView(LoginRequiredMixin,DetailView):
    model = AtencionSecundaria
    template_name = "atencion/atencion_detalle.html"
    # additional parameters

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = AtencionSecundariaDetalle.objects.filter(cabecera=self.object.id)
        return context


