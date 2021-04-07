from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import InventarioTics, Marca, Modelo, Condicion, Categoria, CapacidadDisco, CapacidadMemoriaRam, Procesador, InvetarioDistritoCabecera, InventarioDistritoDetalle
from .forms import InvTicsForm, MarcaForm, ModeloForm, CategoriaForm, CondicionForm, CapacidadDiscoForm, CapacidadMemoriaRamForm, ProcesadorForm, InvetarioDistritoCabeceraForm, InventarioDistritoDetalleForm, DetalleForm
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, JsonResponse

from django.forms import model_to_dict
=======

from django.http import HttpResponseRedirect
>>>>>>> 5d444218691a5eb236c856b2c489d44bf899ff0f
# Create your views here.
#------------------MARCA--------------------------------------
class MarcaListView(LoginRequiredMixin,ListView):
    model = Marca
    template_name = "inventario/marca_listado.html"


class MarcaCreateView(LoginRequiredMixin,CreateView):
    model = Marca
    form_class = MarcaForm
    template_name= "inventario/marca_crear.html"
    success_url = reverse_lazy('marca_listar')

class MarcaDeleteView(LoginRequiredMixin,DeleteView):
    model = Marca
    template_name = "inventario/marca_eliminar.html"
    success_url = reverse_lazy('marca_listar')
 

class MarcaUpdateView(LoginRequiredMixin,UpdateView):
    model = Marca
    form_class = MarcaForm
    template_name = "inventario/marca_editar.html"
    success_url = reverse_lazy('marca_listar')
   
class MarcaDetailView(LoginRequiredMixin,DetailView):
    model = Marca
    template_name = "inventario/marca_detalle.html"
#------------------MODELO--------------------------------------
class ModeloListView(LoginRequiredMixin,ListView):
    model = Modelo
    template_name = "inventario/modelo_listado.html"


class ModeloCreateView(LoginRequiredMixin,CreateView):
    model = Modelo
    form_class = ModeloForm
    template_name= "inventario/modelo_crear.html"
    success_url = reverse_lazy('modelo_listar')
 
class ModeloDeleteView(LoginRequiredMixin,DeleteView):
    model = Modelo
    template_name = "inventario/modelo_eliminar.html"
    success_url = reverse_lazy('modelo_listar')
 

class ModeloUpdateView(LoginRequiredMixin, UpdateView):
    model = Modelo
    form_class = ModeloForm
    template_name = "inventario/modelo_editar.html"
    success_url = reverse_lazy('modelo_listar')
 
class ModeloDetailView(LoginRequiredMixin,DetailView):
    model = Modelo
    template_name = "inventario/modelo_detalle.html"
#------------------CATEGORIA--------------------------------------
class CategoriaListView(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = "inventario/categoria_listado.html"

  
class CategoriaCreateView(LoginRequiredMixin,CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name= "inventario/categoria_crear.html"
    success_url = reverse_lazy('categoria_listar')
    
class CategoriaDeleteView(LoginRequiredMixin,DeleteView):
    model = Categoria
    template_name = "inventario/categoria_eliminar.html"
    success_url = reverse_lazy('categoria_listar')
 


class CategoriaUpdateView(LoginRequiredMixin,UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "inventario/categoria_editar.html"
    success_url = reverse_lazy('categoria_listar')

class CategoriaDetailView(LoginRequiredMixin,DetailView):
    model = Categoria
    template_name = "inventario/categoria_detalle.html"
#------------------CONDICION--------------------------------------
class CondicionListView(LoginRequiredMixin,ListView):
    model = Condicion
    template_name = "inventario/condicion_listado.html"

 
class CondicionCreateView(LoginRequiredMixin,CreateView):
    model = Condicion
    form_class = CondicionForm
    template_name= "inventario/condicion_crear.html"
    success_url = reverse_lazy('condicion_listar')

class CondicionDeleteView(LoginRequiredMixin,DeleteView):
    model = Condicion
    template_name = "inventario/condicion_eliminar.html"
    success_url = reverse_lazy('condicion_listar')
  

class CondicionUpdateView(LoginRequiredMixin,UpdateView):
    model = Condicion
    form_class = CondicionForm
    template_name = "inventario/condicion_editar.html"
    success_url = reverse_lazy('condicion_listar')
  
class CondicionDetailView(LoginRequiredMixin,DetailView):
    model = Condicion
    template_name = "inventario/condicion_detalle.html"
#------------------INVENTARIO TICS--------------------------------------
class InvTicsListView(LoginRequiredMixin,ListView):
    model = InventarioTics
    template_name = "inventario/inv_tics_listado.html"

   
    
class InvTicsCreateView(LoginRequiredMixin,CreateView):
    model = InventarioTics
    form_class = InvTicsForm
    template_name= "inventario/inv_tics_crear.html"
    success_url = reverse_lazy('inv_tics_listar')
    

class InvTicsDeleteView(LoginRequiredMixin,DeleteView):
    model = InventarioTics
    template_name = "inventario/inv_tics_eliminar.html"
    success_url = reverse_lazy('inv_tics_listar')
    
    
class InvTicsUpdateView(LoginRequiredMixin,UpdateView):
    model = InventarioTics
    form_class = InvTicsForm
    template_name = "inventario/inv_tics_editar.html"
    success_url = reverse_lazy('inv_tics_listar')
    
        
class InvTicsDetailView(LoginRequiredMixin,DetailView):
    model = InventarioTics
    template_name = "inventario/inv_tics_detalle.html"
#------------------CAPACIDAD DISCO--------------------------------------
class CapacidadDiscoListView(LoginRequiredMixin,ListView):
    model = CapacidadDisco
    template_name = "inventario/capacidad_disco_listado.html"

   
    
class CapacidadDiscoCreateView(LoginRequiredMixin,CreateView):
    model = CapacidadDisco
    form_class = CapacidadDiscoForm
    template_name= "inventario/capacidad_disco_crear.html"
    success_url = reverse_lazy('capacidad_disco_listar')
  

class CapacidadDiscoDeleteView(LoginRequiredMixin,DeleteView):
    model = CapacidadDisco
    template_name = "inventario/capacidad_discos_eliminar.html"
    success_url = reverse_lazy('capacidad_disco_listar')
    
    
class CapacidadDiscoUpdateView(LoginRequiredMixin,UpdateView):
    model = CapacidadDisco
    form_class = CapacidadDiscoForm
    template_name = "inventario/capacidad_disco_editar.html"
    success_url = reverse_lazy('capacidad_disco_listar')
   
        
class CapacidadDiscoDetailView(LoginRequiredMixin,DetailView):
    model = CapacidadDisco
    template_name = "inventario/capacidad_disco_detalle.html"
#------------------CAPACIDAD MEMORIA RAM--------------------------------------
class CapacidadMemoriaRamListView(LoginRequiredMixin,ListView):
    model = CapacidadMemoriaRam
    template_name = "inventario/capacidad_memoria_ram_listado.html"

    
    
class CapacidadMemoriaRamCreateView(LoginRequiredMixin,CreateView):
    model = CapacidadMemoriaRam
    form_class = CapacidadMemoriaRamForm
    template_name= "inventario/capacidad_memoria_ram_crear.html"
    success_url = reverse_lazy('capacidad_memoria_ram_listar')
    

class CapacidadMemoriaRamDeleteView(LoginRequiredMixin,DeleteView):
    model = CapacidadMemoriaRam
    template_name = "inventario/capacidad_memoria_ram_eliminar.html"
    success_url = reverse_lazy('capacidad_memoria_ram_listar')
  
    
class CapacidadMemoriaRamUpdateView(LoginRequiredMixin,UpdateView):
    model = CapacidadMemoriaRam
    form_class = CapacidadMemoriaRamForm
    template_name = "inventario/capacidad_memoria_ram_editar.html"
    success_url = reverse_lazy('capacidad_memoria_ram_listar')
 
        
class CapacidadMemoriaRamDetailView(LoginRequiredMixin,DetailView):
    model = CapacidadMemoriaRam
    template_name = "inventario/capacidad_memoria_ram_detalle.html"
#------------------PROCESADOR--------------------------------------
class ProcesadorListView(LoginRequiredMixin,ListView):
    model = Procesador
    template_name = "inventario/procesador_listado.html"

    
class ProcesadorCreateView(LoginRequiredMixin,CreateView):
    model = Procesador
    form_class = ProcesadorForm
    template_name= "inventario/procesador_crear.html"
    success_url = reverse_lazy('procesador_listar')


class ProcesadorDeleteView(LoginRequiredMixin,DeleteView):
    model = Procesador
    template_name = "inventario/procesador_eliminar.html"
    success_url = reverse_lazy('procesador_listar')
    
    
class ProcesadorUpdateView(LoginRequiredMixin,UpdateView):
    model = Procesador
    form_class = ProcesadorForm
    template_name = "inventario/procesador_editar.html"
    success_url = reverse_lazy('procesador_listar')
    
        
class ProcesadorDetailView(LoginRequiredMixin,DetailView):
    model = Procesador
    template_name = "inventario/procesador_detalle.html"
#------------------CABECERA-DETALLE--------------------------------------
class DetCabListView(LoginRequiredMixin,ListView):
    model = InvetarioDistritoCabecera
    template_name = "inventario/det_cab_listado.html"

   
class DetCabCreateView(LoginRequiredMixin,CreateView):
    model = InvetarioDistritoCabecera
    template_name = "inventario/det_cab_crear.html"
    form_class = InvetarioDistritoCabeceraForm
    success_url = reverse_lazy('det_cab_listar')
    
    def get(self, request,*args,**kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_form = DetalleForm()
        return self.render_to_response(
            self.get_context_data(form=form, detalle_form=detalle_form)
        )
    
    @method_decorator(csrf_exempt,login_required)
    def dispatch(self,request,*args, **kwargs):
        return super().dispatch(request,*args, **kwargs)
    def post(self, request,*args, **kwargs):
        data ={}
        if self.request.POST['action']=='search_periferico':
            try:
                action = self.request.POST['action']
                print(self.request.POST['term'])
                if action =='search_periferico':
                    data = []
                    prods = InventarioDistritoDetalle.objects.get(periferico__icontains=self.request.POST['term'])
                    for i in prods:
                        item = i.toJSON()
                        item['value'] = i.periferico
                        data.append(item)
                else:
                    data['error'] = 'No ha ingresado a ninguna opcion'
            except Exception as e:
                data['error'] = "error"
            return JsonResponse(data, safe=False)
        else:
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

   
class DetCabDeleteView(LoginRequiredMixin,DeleteView):
    model = InvetarioDistritoCabecera
    template_name = "inventario/det_cab_eliminar.html"
    success_url = reverse_lazy('det_cab_listar')
    
  
    
class DetCabUpdateView(LoginRequiredMixin,UpdateView):
    model = InvetarioDistritoCabecera
    form_class = InvetarioDistritoCabeceraForm
    template_name = "inventario/det_cab_editar.html"
    success_url = reverse_lazy('det_cab_listar')
    def get_context_data(self, **kwargs):
        context = super(DetCabUpdateView, self).get_context_data(**kwargs)
        if self.request.POST :
            context['detalle_form'] = DetalleForm(self.request.POST, instance=self.object)
        else:
            context['detalle_form'] = DetalleForm(instance=self.object)
        return context
    def post(self, request,*args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_form = DetalleForm(self.request.POST,instance=self.object)
        if (form.is_valid() and detalle_form.is_valid()):
            return self.form_valid(form, detalle_form)
        else:
            return self.form_invalid(form, detalle_form)

    def form_valid(self, form, detalle_form):
        cabecera =form.save()
        detalle_form.instance = cabecera
        detalle_form.save()    
        return HttpResponseRedirect(self.success_url)
        
    def form_invalid(self, form, detalle_form):
        return self.render_to_response(
            self.get_context_data(form = form, detalle_form=detalle_form)
        )

  

class DetCabDetailView(LoginRequiredMixin,DetailView):
    model = InvetarioDistritoCabecera
    template_name = "inventario/det_cab_detalle.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
     
        context['items'] = InventarioDistritoDetalle.objects.filter(cabeceraDistrito=self.object.id)
        return context

