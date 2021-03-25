from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from red.models import AccesoRed

# Create your views here.
class AccesoRedListView(ListView):
    model = AccesoRed
    template_name = "red/acceso_red_listado.html"
    


class AccesoRedCreateView(CreateView):
    model = AccesoRed
    template_name = "red/acceso_red_crear.html"
    fields = ['fecha','usuario','direccion_mac','direccion_ip','observacion','estado']
    success_url = reverse_lazy('accesoRed_listar')
