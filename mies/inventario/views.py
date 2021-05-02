from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .models import InventarioTics, Marca, Modelo, Condicion, Categoria, CapacidadDisco, CapacidadMemoriaRam, Procesador,\
    EquipoCabecera, EquipoDetalle
from .forms import InvTicsForm, MarcaForm, ModeloForm, CategoriaForm, CondicionForm, CapacidadDiscoForm, CapacidadMemoriaRamForm, ProcesadorForm,\
    EquipoCabeceraForm, EquipoDetalleForm,EquipoCabDetalleForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, JsonResponse
import json
from django.db import transaction
from django.forms import model_to_dict
# Create your views here.
#------------------MARCA--------------------------------------
class MarcaListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'inventario.view_marca'
    model = Marca
    template_name = "inventario/marca_listado.html"


class MarcaCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'inventario.add_marca'
    model = Marca
    form_class = MarcaForm
    template_name= "inventario/marca_crear.html"
    success_url = reverse_lazy('marca_listar')

class MarcaDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'inventario.delete_marca'
    model = Marca
    template_name = "inventario/marca_eliminar.html"
    success_url = reverse_lazy('marca_listar')
 

class MarcaUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'inventario.change_marca'
    model = Marca
    form_class = MarcaForm
    template_name = "inventario/marca_editar.html"
    success_url = reverse_lazy('marca_listar')
   
class MarcaDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'inventario.view_marca'
    model = Marca
    template_name = "inventario/marca_detalle.html"
#------------------MODELO--------------------------------------
class ModeloListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'inventario.view_modelo'
    model = Modelo
    template_name = "inventario/modelo_listado.html"


class ModeloCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'inventario.add_modelo'
    model = Modelo
    form_class = ModeloForm
    template_name= "inventario/modelo_crear.html"
    success_url = reverse_lazy('modelo_listar')
 
class ModeloDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'inventario.delete_modelo'
    model = Modelo
    template_name = "inventario/modelo_eliminar.html"
    success_url = reverse_lazy('modelo_listar')
 

class ModeloUpdateView(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    permission_required = 'inventario.change_modelo'
    model = Modelo
    form_class = ModeloForm
    template_name = "inventario/modelo_editar.html"
    success_url = reverse_lazy('modelo_listar')
 
class ModeloDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'inventario.view_modelo'
    model = Modelo
    template_name = "inventario/modelo_detalle.html"
#------------------CATEGORIA--------------------------------------
class CategoriaListView(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    permission_required = 'inventario.view_categoria'
    model = Categoria
    template_name = "inventario/categoria_listado.html"

  
class CategoriaCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'inventario.add_categoria'
    model = Categoria
    form_class = CategoriaForm
    template_name= "inventario/categoria_crear.html"
    success_url = reverse_lazy('categoria_listar')
    
class CategoriaDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'inventario.delete_categoria'
    model = Categoria
    template_name = "inventario/categoria_eliminar.html"
    success_url = reverse_lazy('categoria_listar')
 


class CategoriaUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'inventario.change_categoria'
    model = Categoria
    form_class = CategoriaForm
    template_name = "inventario/categoria_editar.html"
    success_url = reverse_lazy('categoria_listar')

class CategoriaDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'inventario.view_categoria'
    model = Categoria
    template_name = "inventario/categoria_detalle.html"
#------------------CONDICION--------------------------------------
class CondicionListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'inventario.view_condicion'
    model = Condicion
    template_name = "inventario/condicion_listado.html"

 
class CondicionCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'inventario.add_condicion'
    model = Condicion
    form_class = CondicionForm
    template_name= "inventario/condicion_crear.html"
    success_url = reverse_lazy('condicion_listar')

class CondicionDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'inventario.delete_condicion'
    model = Condicion
    template_name = "inventario/condicion_eliminar.html"
    success_url = reverse_lazy('condicion_listar')
  

class CondicionUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'inventario.change_condicion'
    model = Condicion
    form_class = CondicionForm
    template_name = "inventario/condicion_editar.html"
    success_url = reverse_lazy('condicion_listar')
  
class CondicionDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'inventario.view_condicion'
    model = Condicion
    template_name = "inventario/condicion_detalle.html"
#------------------INVENTARIO TICS--------------------------------------
class InvTicsListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'inventario.view_inventariotics'
    model = InventarioTics
    template_name = "inventario/inv_tics_listado.html"

   
    
class InvTicsCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'inventario.add_inventariotics'
    model = InventarioTics
    form_class = InvTicsForm
    template_name= "inventario/inv_tics_crear.html"
    success_url = reverse_lazy('inv_tics_listar')
    

class InvTicsDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'inventario.delete_inventariotics'
    model = InventarioTics
    template_name = "inventario/inv_tics_eliminar.html"
    success_url = reverse_lazy('inv_tics_listar')
    
    
class InvTicsUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'inventario.change_inventariotics'
    model = InventarioTics
    form_class = InvTicsForm
    template_name = "inventario/inv_tics_editar.html"
    success_url = reverse_lazy('inv_tics_listar')
    
        
class InvTicsDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'inventario.view_inventariotics'
    model = InventarioTics
    template_name = "inventario/inv_tics_detalle.html"
#------------------CAPACIDAD DISCO--------------------------------------
class CapacidadDiscoListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'inventario.view_capacidaddisco'
    model = CapacidadDisco
    template_name = "inventario/capacidad_disco_listado.html"

   
    
class CapacidadDiscoCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'inventario.add_capacidaddisco'
    model = CapacidadDisco
    form_class = CapacidadDiscoForm
    template_name= "inventario/capacidad_disco_crear.html"
    success_url = reverse_lazy('capacidad_disco_listar')
  

class CapacidadDiscoDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'inventario.delete_capacidaddisco'
    model = CapacidadDisco
    template_name = "inventario/capacidad_discos_eliminar.html"
    success_url = reverse_lazy('capacidad_disco_listar')
    
    
class CapacidadDiscoUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'inventario.change_capacidaddisco'
    model = CapacidadDisco
    form_class = CapacidadDiscoForm
    template_name = "inventario/capacidad_disco_editar.html"
    success_url = reverse_lazy('capacidad_disco_listar')
   
        
class CapacidadDiscoDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'inventario.view_capacidaddisco'
    model = CapacidadDisco
    template_name = "inventario/capacidad_disco_detalle.html"
#------------------CAPACIDAD MEMORIA RAM--------------------------------------
class CapacidadMemoriaRamListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'inventario.view_capacidadmemoriaram'
    model = CapacidadMemoriaRam
    template_name = "inventario/capacidad_memoria_ram_listado.html"

    
    
class CapacidadMemoriaRamCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'inventario.add_capacidadmemoriaram'
    model = CapacidadMemoriaRam
    form_class = CapacidadMemoriaRamForm
    template_name= "inventario/capacidad_memoria_ram_crear.html"
    success_url = reverse_lazy('capacidad_memoria_ram_listar')
    

class CapacidadMemoriaRamDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'inventario.delete_capacidadmemoriaram'
    model = CapacidadMemoriaRam
    template_name = "inventario/capacidad_memoria_ram_eliminar.html"
    success_url = reverse_lazy('capacidad_memoria_ram_listar')
  
    
class CapacidadMemoriaRamUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'inventario.change_capacidadmemoriaram'
    model = CapacidadMemoriaRam
    form_class = CapacidadMemoriaRamForm
    template_name = "inventario/capacidad_memoria_ram_editar.html"
    success_url = reverse_lazy('capacidad_memoria_ram_listar')
 
        
class CapacidadMemoriaRamDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'inventario.view_capacidadmemoriaram'
    model = CapacidadMemoriaRam
    template_name = "inventario/capacidad_memoria_ram_detalle.html"
#------------------PROCESADOR--------------------------------------
class ProcesadorListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'inventario.view_procesador'
    model = Procesador
    template_name = "inventario/procesador_listado.html"

    
class ProcesadorCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'inventario.add_procesador'
    model = Procesador
    form_class = ProcesadorForm
    template_name= "inventario/procesador_crear.html"
    success_url = reverse_lazy('procesador_listar')


class ProcesadorDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'inventario.delete_procesador'
    model = Procesador
    template_name = "inventario/procesador_eliminar.html"
    success_url = reverse_lazy('procesador_listar')
    
    
class ProcesadorUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'inventario.change_procesador'
    model = Procesador
    form_class = ProcesadorForm
    template_name = "inventario/procesador_editar.html"
    success_url = reverse_lazy('procesador_listar')
    
        
class ProcesadorDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'inventario.view_procesador'
    model = Procesador
    template_name = "inventario/procesador_detalle.html"
#------------------CABECERA-DETALLE-EQUIPO--------------------------------------

class EquipoListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'inventario.view_Equipocabecera'
    model = EquipoCabecera
    template_name = "inventario/equipo_listado.html"
    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args, **kwargs):
        return super().dispatch(request,*args, **kwargs)
class EquipoCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'inventario.add_Equipocabecera'
    model = EquipoCabecera
    form_class = EquipoCabeceraForm
    template_name= "inventario/equipo_crear.html"
    success_url = reverse_lazy('equipo_listar')
    def get(self, request,*args,**kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_form = EquipoCabDetalleForm()
        return self.render_to_response(
            self.get_context_data(form=form, detalle_form=detalle_form)
        )
    
    def post(self, request,*args, **kwargs):
<<<<<<< HEAD
        data ={}
        try:
            action = request.POST['action']
            if action =='search_periferico':
                data = []
                prods = InventarioTics.objects.filter(descripcion__icontains=request.POST['term'])[0:10]
                for i in prods:
                    item = i.toJSON()
                    item['text'] = i.descripcion
                    item['foto'] = ""
                    data.append(item)
            elif action =='add':
                vents = json.loads(request.POST['vents'])
                print(vents['foto'])
                invCab = InvetarioDistritoCabecera()
                invCab.fechaIngreso = vents['fechaIngreso']
                invCab.responsable_id = vents['responsable']
                invCab.categoria_id = vents['categoria']
                invCab.descripcion = vents['descripcion']
                invCab.marca_id = vents['marca']
                invCab.modelo_id = vents['modelo']
                invCab.condicion_id = vents['condicion']
                invCab.serie = vents['serie']
                invCab.codigoMies = vents['codigoMies']
                invCab.direccionIp = vents['direccionIp']
                invCab.direccionMac = vents['direccionMac']
                invCab.capacidadDisco_id = vents['capacidadDisco']
                invCab.capacidadMemoria_id = vents['capacidadMemoria']
                invCab.capacidadProcesador_id = vents['capacidadProcesador']
                invCab.foto = vents['foto']
                invCab.save()
                for i in vents['detalle']:
                    det = InventarioDistritoDetalle()
                    det.cabeceraDistrito_id = invCab.id
                    det.periferico_id = i['id']
                    det.cantidad = int(i['cant'])
                    det.save()
=======
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_form = EquipoCabDetalleForm(self.request.POST)
        if (form.is_valid() and detalle_form.is_valid()):
            return self.form_valid(form, detalle_form)
        else:
            return self.form_invalid(form, detalle_form)
>>>>>>> a6bb34eff834a94a8898d054ae68c283b9b7de5f

    def form_valid(self, form, detalle_form):
        cabecera = form.save()
        detalle_form.instance = cabecera
        detalle_form.save()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form, detalle_form):
        return self.render_to_response(
            self.get_context_data(form = form, detalle_form=detalle_form)
        )
class EquipoUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'inventario.change_Equipocabecera'
    model = EquipoCabecera
    form_class = EquipoCabeceraForm
    template_name= "inventario/equipo_editar.html"
    success_url = reverse_lazy('equipo_listar')
    def get(self, request,*args,**kwargs):
        self.object = self.get_object()
        print(self.object)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_form = EquipoCabDetalleForm(instance = self.object)
        return self.render_to_response(
            self.get_context_data(form=form, detalle_form=detalle_form)
        )
    
    def post(self, request,*args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_form = EquipoCabDetalleForm(self.request.POST,instance=self.get_object())
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
class EquipoDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'inventario.view_Equipocabecera'
    model = EquipoCabecera
    template_name = "inventario/equipo_detalle.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
     
        context['items'] = EquipoDetalle.objects.filter(cabeceraDistrito=self.object.id)
        return context
class EquipoDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'inventario.delete_Equipocabecera'
    model = EquipoCabecera
    template_name = "inventario/equipo_eliminar.html"
    success_url = reverse_lazy('equipo_listar')
    