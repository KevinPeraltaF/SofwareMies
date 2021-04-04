from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .models import Atencion, AtencionDetalle
from .forms import AtencionForm, AtencionDetalleForm, DetalleForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import  HttpResponseRedirect

# Create your views here.
class AtencionListView(ListView):
    model = AtencionDetalle 
    template_name = "atencion/atencion_listado.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AtencionListView, self).dispatch(*args, **kwargs)
    
class AtencionCreateView(CreateView):
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
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AtencionCreateView, self).dispatch(*args, **kwargs)


class AtencionDeleteView(DeleteView):
    model = AtencionDetalle
    template_name = "atencion/atencion_eliminar.html"
    success_url = reverse_lazy('Atencion_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AtencionDeleteView, self).dispatch(*args, **kwargs)


class AtencionUpdateView(UpdateView):
    model = AtencionDetalle
    form_class = AtencionDetalleForm
    second_form__class= AtencionForm
    template_name = "atencion/atencion_editar.html"
    success_url = reverse_lazy('Atencion_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AtencionUpdateView, self).dispatch(*args, **kwargs)

    
class AtencionDetailView(DetailView):
    model = AtencionDetalle
    template_name = "atencion/atencion_detalle.html"
    
