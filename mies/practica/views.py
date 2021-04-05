from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .models import Pasante, Carrera, Universidad
from .forms import PasanteForm, CarreraForm, UniversidadForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# VISTA PASANTE.
class PasanteListView(ListView):
    model = Pasante
    template_name = "practica/pasante_listado.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PasanteListView, self).dispatch(*args, **kwargs)
    
class PasanteCreateView(CreateView):
    model = Pasante
    form_class = PasanteForm
    template_name = "practica/pasante_crear.html"
    success_url = reverse_lazy('pasante_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PasanteCreateView, self).dispatch(*args, **kwargs)


class PasanteDeleteView(DeleteView):
    model = Pasante
    template_name = "practica/pasante_eliminar.html"
    success_url = reverse_lazy('pasante_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PasanteDeleteView, self).dispatch(*args, **kwargs)


class PasanteUpdateView(UpdateView):
    model = Pasante
    form_class = PasanteForm
    template_name = "practica/pasante_editar.html"
    success_url = reverse_lazy('pasante_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PasanteUpdateView, self).dispatch(*args, **kwargs)

    
class PasanteDetailView(DetailView):
    model = Pasante
    template_name = "practica/pasante_detalle.html"

# VISTA CARRERA.
class CarreraListView(ListView):
    model = Carrera
    template_name = "practica/carrera_listado.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CarreraListView, self).dispatch(*args, **kwargs)
    
class CarreraCreateView(CreateView):
    model = Carrera
    form_class = CarreraForm
    template_name = "practica/carrera_crear.html"
    success_url = reverse_lazy('carrera_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CarreraCreateView, self).dispatch(*args, **kwargs)


class CarreraDeleteView(DeleteView):
    model = Carrera
    template_name = "practica/carrera_eliminar.html"
    success_url = reverse_lazy('carrera_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CarreraDeleteView, self).dispatch(*args, **kwargs)


class CarreraUpdateView(UpdateView):
    model = Carrera
    form_class = CarreraForm
    template_name = "practica/carrera_editar.html"
    success_url = reverse_lazy('carrera_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CarreraUpdateView, self).dispatch(*args, **kwargs)

    
class CarreraDetailView(DetailView):
    model = Carrera
    template_name = "practica/carrera_detalle.html"

# VISTA UNIVERSIDAD.
class UniversidadListView(ListView):
    model = Universidad
    template_name = "practica/universidad_listado.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UniversidadListView, self).dispatch(*args, **kwargs)
    
class UniversidadCreateView(CreateView):
    model = Universidad
    form_class = UniversidadForm
    template_name = "practica/universidad_crear.html"
    success_url = reverse_lazy('universidad_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UniversidadCreateView, self).dispatch(*args, **kwargs)

class UniversidadDeleteView(DeleteView):
    model = Universidad
    template_name = "practica/universidad_eliminar.html"
    success_url = reverse_lazy('universidad_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UniversidadDeleteView, self).dispatch(*args, **kwargs)

class UniversidadUpdateView(UpdateView):
    model = Universidad
    form_class = UniversidadForm
    template_name = "practica/universidad_editar.html"
    success_url = reverse_lazy('universidad_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UniversidadUpdateView, self).dispatch(*args, **kwargs)
    
class UniversidadDetailView(DetailView):
    model = Universidad
    template_name = "practica/universidad_detalle.html"


