from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .models import Prioridad, Asunto, Actividad, ActividadDetalle
from .forms import Prioridad, Asunto, ActividadForm, ActividadDetalleForm, DetalleForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.http import  HttpResponseRedirect

# VISTAS DEL MODULO ACTIVIDAD.
#VISTA ACTIVIDAD
class ActividadListView(LoginRequiredMixin,ListView):
    model = Actividad
    template_name = "actividad/actividad_listado.html"

    
class ActividadCreateView(LoginRequiredMixin,CreateView):
    model = Actividad
    
    form_class = ActividadForm
    template_name = "actividad/actividad_crear.html"
    success_url = reverse_lazy('actividad_listar')
    
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



class ActividadDeleteView(LoginRequiredMixin,DeleteView):
    model = ActividadDetalle
    template_name = "actividad/actividad_eliminar.html"
    success_url = reverse_lazy('actividad_listar')
   

class ActividadUpdateView(LoginRequiredMixin,UpdateView):
    model = ActividadDetalle
    form_class = ActividadDetalleForm
    second_form__class= ActividadForm
    template_name = "actividad/actividad_editar.html"
    success_url = reverse_lazy('actividad_listar')


    
class ActividadDetailView(LoginRequiredMixin,DetailView):
    model = Actividad
    template_name = "actividad/actividad_detalle.html"
    # additional parameters

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = ActividadDetalle.objects.filter(cabecera=self.object.id)
        return context

#VISTA PRIORIDAD
#VISTA ASUNTO