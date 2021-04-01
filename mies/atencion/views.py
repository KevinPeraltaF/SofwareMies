from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .models import Atencion, AtencionDetalle
from .forms import AtencionForm, AtencionDetalleForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class AtencionListView(ListView):
    model = Atencion
    template_name = "atencion/atencion_listado.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AtencionListView, self).dispatch(*args, **kwargs)
    
class AtencionCreateView(CreateView):
    model = Atencion
    form_class = AtencionForm
    template_name = "atencion/atencion_crear.html"
    success_url = reverse_lazy('Atencion_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AtencionCreateView, self).dispatch(*args, **kwargs)


class AtencionDeleteView(DeleteView):
    model = Atencion
    template_name = "atencion/atencion_eliminar.html"
    success_url = reverse_lazy('Atencion_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AtencionDeleteView, self).dispatch(*args, **kwargs)


class AtencionUpdateView(UpdateView):
    model = Atencion
    form_class = AtencionForm
    template_name = "atencion/atencion_editar.html"
    success_url = reverse_lazy('Atencion_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AtencionUpdateView, self).dispatch(*args, **kwargs)

    
class AtencionDetailView(DetailView):
    model = Atencion
    template_name = "atencion/atencion_detalle.html"

