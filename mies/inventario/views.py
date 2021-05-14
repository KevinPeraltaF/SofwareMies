from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .models import Dispositivo, Marca, Modelo,  CapacidadDisco, CapacidadMemoriaRam, Procesador, TipoDispositivo, TipoImpresora,ImpresoraTecnologia ,SoftwareAntivirus , SoftwareOfimatica,SistemaOperativo,TipoEquipo
from .forms import  MarcaForm, ModeloForm,  CapacidadDiscoForm, CapacidadMemoriaRamForm, ProcesadorForm,DispositivoForm,TipoDispositivoForm,TipoImpresoraForm,ImpresoraTecnologiaForm,SoftwareAntivirusForm,SoftwareOfimaticaForm,SistemaOperativoForm,TipoEquipoForm







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


#DISPOSITIVO
class DispositivoListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'inventario.view_dispositivo'
    model = Dispositivo
    template_name = "inventario/dispositivo_listado.html"

class DispositivoCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'inventario.add_dispositivo'
    model = Dispositivo
    form_class = DispositivoForm
    template_name= "inventario/dispositivo_crear.html"
    success_url = reverse_lazy('dispositivo_listar')
    

class DispositivoDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'inventario.delete_dispositivo'
    model = Dispositivo
    template_name = "inventario/dispositivo_eliminar.html"
    success_url = reverse_lazy('dispositivo_listar')
    
    
class DispositivoUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'inventario.change_dispositivo'
    model = Dispositivo
    form_class = DispositivoForm
    template_name = "inventario/dispositivo_editar.html"
    success_url = reverse_lazy('dispositivo_listar')
    
        
class DispositivoDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'inventario.view_dispositivo'
    model = Dispositivo
    template_name = "inventario/dispositivo_detalle.html"


####
#------------------TIPO DISPOSITIVO--------------------------------------
class TipoDispositivoListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'inventario.view_tipodispositivo'
    model = TipoDispositivo
    template_name = "inventario/tipo_dispositivo_listado.html"

    
class TipoDispositivoCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'inventario.add_tipodispositivo'
    model = TipoDispositivo
    form_class = TipoDispositivoForm
    template_name= "inventario/tipo_dispositivo_crear.html"
    success_url = reverse_lazy('tipo_dispositivo_listar')


class TipoDispositivoDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'inventario.delete_tipodispositivo'
    model = TipoDispositivo
    template_name = "inventario/tipo_dispositivo_eliminar.html"
    success_url = reverse_lazy('tipo_dispositivo_listar')
    
    
class TipoDispositivoUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'inventario.change_tipodispositivo'
    model = TipoDispositivo
    form_class = TipoDispositivoForm
    template_name = "inventario/tipo_dispositivo_editar.html"
    success_url = reverse_lazy('tipo_dispositivo_listar')
    
        
class TipoDispositivoDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'inventario.view_tipodispositivo'
    model = TipoDispositivo
    template_name = "inventario/tipo_dispositivo_detalle.html"

#------------------TIPO TipoImpresora--------------------------------------
class TipoImpresoraListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'inventario.view_tipoimpresora'
    model = TipoImpresora
    template_name = "inventario/tipo_impresora_listado.html"

    
class TipoImpresoraCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'inventario.add_tipoimpresora'
    model = TipoImpresora
    form_class = TipoImpresoraForm
    template_name= "inventario/tipo_impresora_crear.html"
    success_url = reverse_lazy('tipo_impresora_listar')


class TipoImpresoraDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'inventario.delete_tipoimpresora'
    model = TipoImpresora
    template_name = "inventario/tipo_impresora_eliminar.html"
    success_url = reverse_lazy('tipo_impresora_listar')
    
    
class TipoImpresoraUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'inventario.change_tipoimpresora'
    model = TipoImpresora
    form_class = TipoImpresoraForm
    template_name = "inventario/tipo_impresora_editar.html"
    success_url = reverse_lazy('tipo_impresora_listar')
    
        
class TipoImpresoraDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'inventario.view_tipoimpresora'
    model = TipoImpresora
    template_name = "inventario/tipo_impresora_detalle.html"


#------------------TIPO TipoEquipo--------------------------------------
class TipoEquipoListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'inventario.view_tipoequipo'
    model = TipoEquipo
    template_name = "inventario/tipo_equipo_listado.html"

    
class TipoEquipoCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'inventario.add_tipoequipo'
    model = TipoEquipo
    form_class = TipoEquipoForm
    template_name= "inventario/tipo_equipo_crear.html"
    success_url = reverse_lazy('tipo_equipo_listar')


class TipoEquipoDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'inventario.delete_tipoequipo'
    model = TipoEquipo
    template_name = "inventario/tipo_equipo_eliminar.html"
    success_url = reverse_lazy('tipo_equipo_listar')
    
    
class TipoEquipoUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'inventario.change_tipoequipo'
    model = TipoEquipo
    form_class = TipoEquipoForm
    template_name = "inventario/tipo_equipo_editar.html"
    success_url = reverse_lazy('tipo_equipo_listar')
    
        
class TipoEquipoDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'inventario.view_tipoequipo'
    model = TipoEquipo
    template_name = "inventario/tipo_equipo_detalle.html"
