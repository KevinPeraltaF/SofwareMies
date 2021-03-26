from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .models import AccesoRed
from .forms import AccesoRedForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

class AccesoRedListView(ListView):
    model = AccesoRed
    template_name = "red/acceso_red_listado.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AccesoRedListView, self).dispatch(*args, **kwargs)
    


class AccesoRedCreateView(CreateView):
    model = AccesoRed
    form_class = AccesoRedForm
    template_name = "red/acceso_red_crear.html"
    success_url = reverse_lazy('accesoRed_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AccesoRedCreateView, self).dispatch(*args, **kwargs)


class AccesoRedDeleteView(DeleteView):
    model = AccesoRed
    success_url = reverse_lazy('accesoRed_listar')


class AccesoRedUpdateView(UpdateView):
    model = AccesoRed
    form_class = AccesoRedForm
    template_name = "red/acceso_red_editar.html"
    success_url = reverse_lazy('accesoRed_listar')

    

