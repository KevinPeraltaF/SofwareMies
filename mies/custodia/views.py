from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin,LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .models import Custodia
from .forms import CustodiaForm
from inventario.models import Dispositivo
#excel
#Vista genérica para mostrar resultados
from django.views.generic.base import TemplateView
#Workbook nos permite crear libros en excel
from openpyxl import Workbook
#Nos devuelve un objeto resultado, en este caso un archivo de excel
from django.http.response import HttpResponse
import csv
from csv import reader
from openpyxl.utils import get_column_letter

# Create your views here.
class CustodiaListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'custodia.view_custodia'
    model = Custodia
    template_name = "custodia/custodia_listado.html"

    #def get_queryset(self):
     #   return Custodio.objects.exclude(estado = 0) CustodioReporteExcelView
    
# excel


class CustodiaCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'custodia.add_custodia'
    model = Custodia
    form_class = CustodiaForm
    template_name = "custodia/custodia_crear.html"
    success_url = reverse_lazy('custodia_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #obtengo los equipos que ya han sido asignado a un equipo y estan vigentes
        conCustodia = Custodia.objects.all().exclude( estado=0).values_list('equipo')
        #excluyo los dispositivos que esten con estado malo
        dispositivo = Dispositivo.objects.exclude(estado=3).values_list('id')
        #obtengo los id de los dispositivos que no tienen custodio
        diferente  =dispositivo.difference(conCustodia).order_by('id')
        #filtro para mostrar solo los dispositivos sin custodio
        context["equipos"] = Dispositivo.objects.filter(id__in=diferente)
      
        return context  
    
   
class CustodiaReasignarView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'custodia.add_custodia'
    model = Custodia
    form_class = CustodiaForm
    template_name = "custodia/custodiaReasignar.html"
    success_url = reverse_lazy('custodia_listar')

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #obtengo los equipos que ya han sido asignado a un equipo y estan vigentes
        conCustodia = Custodia.objects.all().exclude( estado=0).values_list('equipo')
        print (conCustodia)
        #excluyo los dispositivos que esten con estado malo
        dispositivo = Dispositivo.objects.exclude(estado=3).values_list('id')
        print (dispositivo)
        #obtengo los id de los dispositivos que no tienen custodio
        interseccion  =dispositivo.intersection(conCustodia).order_by('id')
        print (interseccion)
        #filtro para mostrar solo los dispositivos sin custodio
        context["equipos"] = Dispositivo.objects.filter(id__in=interseccion)
        #obtener todos los custodios para saber quien es el custodio anterior
        context["custodioAnterior"] = Custodia.objects.exclude( estado=0)
      
        return context  

 

class CustodiaDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'custodia.delete_custodia'
    model = Custodia
    template_name = "custodia/custodia_eliminar.html"
    success_url = reverse_lazy('custodia_listar')
   


class CustodiaUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'custodia.change_custodia'
    model = Custodia
    form_class = CustodiaForm
    template_name = "custodia/custodia_editar.html"
    success_url = reverse_lazy('custodia_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["equipo"] = Dispositivo.objects.all()
        context["custodioAnterior"] = Custodia.objects.all()
        context["dispositivos"] = Dispositivo.objects.all()
        context["update_dispositivos"] = self.object.equipo.id
        context["update_dispositivos"] = self.object.carrera.universidad.id
      
        return context
    
    
class CustodiaDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'custodia.view_custodia'
    model = Custodia
    template_name = "custodia/custodia_detalle.html"

    