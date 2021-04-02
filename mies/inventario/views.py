from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .models import InventarioTics, Marca, Modelo, Condicion, Categoria, CapacidadDisco, CapacidadMemoriaRam, Procesador
from .forms import InvTicsForm, MarcaForm, ModeloForm, CategoriaForm, CondicionForm, CapacidadDiscoForm, CapacidadMemoriaRamForm, ProcesadorForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
#------------------MARCA--------------------------------------
class MarcaListView(ListView):
    model = Marca
    template_name = "inventario/marca_listado.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MarcaListView, self).dispatch(*args, **kwargs)
class MarcaCreateView(CreateView):
    model = Marca
    form_class = MarcaForm
    template_name= "inventario/marca_crear.html"
    success_url = reverse_lazy('marca_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MarcaCreateView, self).dispatch(*args, **kwargs)
class MarcaDeleteView(DeleteView):
    model = Marca
    template_name = "inventario/marca_eliminar.html"
    success_url = reverse_lazy('marca_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MarcaDeleteView, self).dispatch(*args, **kwargs)

class MarcaUpdateView(UpdateView):
    model = Marca
    form_class = MarcaForm
    template_name = "inventario/marca_editar.html"
    success_url = reverse_lazy('marca_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MarcaUpdateView, self).dispatch(*args, **kwargs)
class MarcaDetailView(DetailView):
    model = Marca
    template_name = "inventario/marca_detalle.html"
#------------------MODELO--------------------------------------
class ModeloListView(ListView):
    model = Modelo
    template_name = "inventario/modelo_listado.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ModeloListView, self).dispatch(*args, **kwargs)
class ModeloCreateView(CreateView):
    model = Modelo
    form_class = ModeloForm
    template_name= "inventario/modelo_crear.html"
    success_url = reverse_lazy('modelo_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ModeloCreateView, self).dispatch(*args, **kwargs)
class ModeloDeleteView(DeleteView):
    model = Modelo
    template_name = "inventario/modelo_eliminar.html"
    success_url = reverse_lazy('modelo_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ModeloDeleteView, self).dispatch(*args, **kwargs)

class ModeloUpdateView(UpdateView):
    model = Modelo
    form_class = ModeloForm
    template_name = "inventario/modelo_editar.html"
    success_url = reverse_lazy('modelo_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ModeloUpdateView, self).dispatch(*args, **kwargs)
class ModeloDetailView(DetailView):
    model = Modelo
    template_name = "inventario/modelo_detalle.html"
#------------------CATEGORIA--------------------------------------
class CategoriaListView(ListView):
    model = Categoria
    template_name = "inventario/categoria_listado.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CategoriaListView, self).dispatch(*args, **kwargs)
class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name= "inventario/categoria_crear.html"
    success_url = reverse_lazy('categoria_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CategoriaCreateView, self).dispatch(*args, **kwargs)
class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = "inventario/categoria_eliminar.html"
    success_url = reverse_lazy('categoria_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CategoriaDeleteView, self).dispatch(*args, **kwargs)


class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "inventario/categoria_editar.html"
    success_url = reverse_lazy('categoria_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CategoriaUpdateView, self).dispatch(*args, **kwargs)
class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = "inventario/categoria_detalle.html"
#------------------CONDICION--------------------------------------
class CondicionListView(ListView):
    model = Condicion
    template_name = "inventario/condicion_listado.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CondicionListView, self).dispatch(*args, **kwargs)
class CondicionCreateView(CreateView):
    model = Condicion
    form_class = CondicionForm
    template_name= "inventario/condicion_crear.html"
    success_url = reverse_lazy('condicion_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CondicionCreateView, self).dispatch(*args, **kwargs)
class CondicionDeleteView(DeleteView):
    model = Condicion
    template_name = "inventario/condicion_eliminar.html"
    success_url = reverse_lazy('condicion_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CondicionDeleteView, self).dispatch(*args, **kwargs)

class CondicionUpdateView(UpdateView):
    model = Condicion
    form_class = CondicionForm
    template_name = "inventario/condicion_editar.html"
    success_url = reverse_lazy('condicion_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CondicionUpdateView, self).dispatch(*args, **kwargs)
class CondicionDetailView(DetailView):
    model = Condicion
    template_name = "inventario/condicion_detalle.html"
#------------------INVENTARIO TICS--------------------------------------
class InvTicsListView(ListView):
    model = InventarioTics
    template_name = "inventario/inv_tics_listado.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InvTicsListView, self).dispatch(*args, **kwargs)
    
class InvTicsCreateView(CreateView):
    model = InventarioTics
    form_class = InvTicsForm
    template_name= "inventario/inv_tics_crear.html"
    success_url = reverse_lazy('inv_tics_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InvTicsCreateView, self).dispatch(*args, **kwargs)

class InvTicsDeleteView(DeleteView):
    model = InventarioTics
    template_name = "inventario/inv_tics_eliminar.html"
    success_url = reverse_lazy('inv_tics_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InvTicsDeleteView, self).dispatch(*args, **kwargs)
    
class InvTicsUpdateView(UpdateView):
    model = InventarioTics
    form_class = InvTicsForm
    template_name = "inventario/inv_tics_editar.html"
    success_url = reverse_lazy('inv_tics_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InvTicsUpdateView, self).dispatch(*args, **kwargs)
        
class InvTicsDetailView(DetailView):
    model = InventarioTics
    template_name = "inventario/inv_tics_detalle.html"
#------------------CAPACIDAD DISCO--------------------------------------
class CapacidadDiscoListView(ListView):
    model = CapacidadDisco
    template_name = "inventario/capacidad_disco_listado.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CapacidadDiscoListView, self).dispatch(*args, **kwargs)
    
class CapacidadDiscoCreateView(CreateView):
    model = CapacidadDisco
    form_class = CapacidadDiscoForm
    template_name= "inventario/capacidad_disco_crear.html"
    success_url = reverse_lazy('capacidad_disco_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CapacidadDiscoCreateView, self).dispatch(*args, **kwargs)

class CapacidadDiscoDeleteView(DeleteView):
    model = CapacidadDisco
    template_name = "inventario/capacidad_discos_eliminar.html"
    success_url = reverse_lazy('capacidad_disco_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CapacidadDiscoDeleteView, self).dispatch(*args, **kwargs)
    
class CapacidadDiscoUpdateView(UpdateView):
    model = CapacidadDisco
    form_class = CapacidadDiscoForm
    template_name = "inventario/capacidad_disco_editar.html"
    success_url = reverse_lazy('capacidad_disco_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CapacidadDiscoUpdateView, self).dispatch(*args, **kwargs)
        
class CapacidadDiscoDetailView(DetailView):
    model = CapacidadDisco
    template_name = "inventario/capacidad_disco_detalle.html"
#------------------CAPACIDAD MEMORIA RAM--------------------------------------
class CapacidadMemoriaRamListView(ListView):
    model = CapacidadMemoriaRam
    template_name = "inventario/capacidad_memoria_ram_listado.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CapacidadMemoriaRamListView, self).dispatch(*args, **kwargs)
    
class CapacidadMemoriaRamCreateView(CreateView):
    model = CapacidadMemoriaRam
    form_class = CapacidadMemoriaRamForm
    template_name= "inventario/capacidad_memoria_ram_crear.html"
    success_url = reverse_lazy('capacidad_memoria_ram_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CapacidadMemoriaRamCreateView, self).dispatch(*args, **kwargs)

class CapacidadMemoriaRamDeleteView(DeleteView):
    model = CapacidadMemoriaRam
    template_name = "inventario/capacidad_memoria_ram_eliminar.html"
    success_url = reverse_lazy('capacidad_memoria_ram_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CapacidadMemoriaRamDeleteView, self).dispatch(*args, **kwargs)
    
class CapacidadMemoriaRamUpdateView(UpdateView):
    model = CapacidadMemoriaRam
    form_class = CapacidadMemoriaRamForm
    template_name = "inventario/capacidad_memoria_ram_editar.html"
    success_url = reverse_lazy('capacidad_memoria_ram_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CapacidadMemoriaRamUpdateView, self).dispatch(*args, **kwargs)
        
class CapacidadMemoriaRamDetailView(DetailView):
    model = CapacidadMemoriaRam
    template_name = "inventario/capacidad_memoria_ram_detalle.html"
#------------------PROCESADOR--------------------------------------
class ProcesadorListView(ListView):
    model = Procesador
    template_name = "inventario/procesador_listado.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProcesadorListView, self).dispatch(*args, **kwargs)
    
class ProcesadorCreateView(CreateView):
    model = Procesador
    form_class = ProcesadorForm
    template_name= "inventario/procesador_crear.html"
    success_url = reverse_lazy('procesador_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProcesadorCreateView, self).dispatch(*args, **kwargs)

class ProcesadorDeleteView(DeleteView):
    model = Procesador
    template_name = "inventario/procesador_eliminar.html"
    success_url = reverse_lazy('procesador_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProcesadorDeleteView, self).dispatch(*args, **kwargs)
    
class ProcesadorUpdateView(UpdateView):
    model = Procesador
    form_class = ProcesadorForm
    template_name = "inventario/procesador_editar.html"
    success_url = reverse_lazy('procesador_listar')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProcesadorUpdateView, self).dispatch(*args, **kwargs)
        
class ProcesadorDetailView(DetailView):
    model = Procesador
    template_name = "inventario/procesador_detalle.html"
