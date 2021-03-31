from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .models import Zona, Provincia, Distrito
from .forms import DistritoForm, ProvinciaForm,ZonaForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# ------------------------------ZONA
class ZonaListView(ListView):
    model = Zona
    template_name = "ubicacion/ubicacion_zona_listado.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ZonaListView, self).dispatch(*args, **kwargs)
    
class ZonaCreateView(CreateView):
    model = Zona
    form_class = ZonaForm
    template_name = "ubicacion/ubicacion_zona_crear.html"
    success_url = reverse_lazy('zona_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ZonaCreateView, self).dispatch(*args, **kwargs)


class ZonaDeleteView(DeleteView):
    model = Zona
    template_name = "ubicacion/ubicacion_zona_eliminar.html"
    success_url = reverse_lazy('zona_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ZonaDeleteView, self).dispatch(*args, **kwargs)


class ZonaUpdateView(UpdateView):
    model = Zona
    form_class = ZonaForm
    template_name = "ubicacion/ubicacion_zona_editar.html"
    success_url = reverse_lazy('zona_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ZonaUpdateView, self).dispatch(*args, **kwargs)

    
class ZonaDetailView(DetailView):
    model = Zona
    template_name = "ubicacion/ubicacion_zona_detalle.html"

#----------------------------------- provincia
class ProvinciaListView(ListView):
    model = Provincia
    template_name = "ubicacion/ubicacion_provincia_listado.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProvinciaListView, self).dispatch(*args, **kwargs)
    
class ProvinciaCreateView(CreateView):
    model = Provincia
    form_class = ProvinciaForm
    template_name = "ubicacion/ubicacion_provincia_crear.html"
    success_url = reverse_lazy('provincia_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProvinciaCreateView, self).dispatch(*args, **kwargs)


class ProvinciaDeleteView(DeleteView):
    model = Provincia
    template_name = "ubicacion/ubicacion_provincia_eliminar.html"
    success_url = reverse_lazy('provincia_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProvinciaDeleteView, self).dispatch(*args, **kwargs)


class ProvinciaUpdateView(UpdateView):
    model = Provincia
    form_class = ProvinciaForm
    template_name = "ubicacion/ubicacion_provincia_editar.html"
    success_url = reverse_lazy('provincia_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProvinciaUpdateView, self).dispatch(*args, **kwargs)

    
class ProvinciaDetailView(DetailView):
    model = Provincia
    template_name = "ubicacion/ubicacion_provincia_detalle.html"



# ------------------------------DISTRITO
class DistritoListView(ListView):
    model = Distrito
    template_name = "ubicacion/ubicacion_distrito_listado.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DistritoListView, self).dispatch(*args, **kwargs)
    
class DistritoCreateView(CreateView):
    model = Distrito
    form_class = DistritoForm
    template_name = "ubicacion/ubicacion_distrito_crear.html"
    success_url = reverse_lazy('distrito_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DistritoCreateView, self).dispatch(*args, **kwargs)


class DistritoDeleteView(DeleteView):
    model = Distrito
    template_name = "ubicacion/ubicacion_distrito_eliminar.html"
    success_url = reverse_lazy('distrito_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DistritoDeleteView, self).dispatch(*args, **kwargs)


class DistritoUpdateView(UpdateView):
    model = Distrito
    form_class = DistritoForm
    template_name = "ubicacion/ubicacion_distrito_editar.html"
    success_url = reverse_lazy('distrito_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DistritoUpdateView, self).dispatch(*args, **kwargs)

    
class DistritoDetailView(DetailView):
    model = Distrito
    template_name = "ubicacion/ubicacion_distrito_detalle.html"

