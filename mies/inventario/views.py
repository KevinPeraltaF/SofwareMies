from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .models import Dispositivo, Marca, Modelo,  CapacidadDisco, CapacidadMemoriaRam, Procesador, TipoDispositivo, TipoImpresora,ImpresoraTecnologia ,SoftwareAntivirus , SoftwareOfimatica,SistemaOperativo,TipoEquipo,InventarioTics
from .forms import  MarcaForm, ModeloForm,  CapacidadDiscoForm, CapacidadMemoriaRamForm, ProcesadorForm,DispositivoForm,TipoDispositivoForm,TipoImpresoraForm,ImpresoraTecnologiaForm,SoftwareAntivirusForm,SoftwareOfimaticaForm,SistemaOperativoForm,TipoEquipoForm,InvTicsForm
from django.http import HttpResponseRedirect, JsonResponse
# excel
#Vista genérica para mostrar resultados
from django.views.generic.base import TemplateView
#Workbook nos permite crear libros en excel
from openpyxl import Workbook
#Nos devuelve un objeto resultado, en este caso un archivo de excel
from django.http.response import HttpResponse
import csv
from csv import reader

from openpyxl.utils import get_column_letter
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

#############################################33
#
#
#
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

#------------------ ImpresoraTecnologia--------------------------------------
class ImpresoraTecnologiaListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'inventario.view_impresoratecnologia'
    model = ImpresoraTecnologia
    template_name = "inventario/tecnologia_impresora_listado.html"

    
class ImpresoraTecnologiaCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'inventario.add_impresoratecnologia'
    model = ImpresoraTecnologia
    form_class = ImpresoraTecnologiaForm
    template_name= "inventario/tecnologia_impresora_crear.html"
    success_url = reverse_lazy('tecnologia_impresora_listar')


class ImpresoraTecnologiaDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'inventario.delete_impresoratecnologia'
    model = ImpresoraTecnologia
    template_name = "inventario/tecnologia_impresora_eliminar.html"
    success_url = reverse_lazy('tecnologia_impresora_listar')
    
    
class ImpresoraTecnologiaUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'inventario.change_impresoratecnologia'
    model = ImpresoraTecnologia
    form_class = ImpresoraTecnologiaForm
    template_name = "inventario/tecnologia_impresora_editar.html"
    success_url = reverse_lazy('tecnologia_impresora_listar')
    
        
class ImpresoraTecnologiaDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'inventario.view_impresoratecnologia'
    model = ImpresoraTecnologia
    template_name = "inventario/tecnologia_impresora_detalle.html"


#------------------ SoftwareAntivirus--------------------------------------
class SoftwareAntivirusListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'inventario.view_softwareantivirus'
    model = SoftwareAntivirus
    template_name = "inventario/software_antivirus_listado.html"

    
class SoftwareAntivirusCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'inventario.add_softwareantivirus'
    model = SoftwareAntivirus
    form_class = SoftwareAntivirusForm
    template_name= "inventario/software_antivirus_crear.html"
    success_url = reverse_lazy('software_antivirus_listar')


class SoftwareAntivirusDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'inventario.delete_softwareantivirus'
    model = SoftwareAntivirus
    template_name = "inventario/software_antivirus_eliminar.html"
    success_url = reverse_lazy('software_antivirus_listar')
    
    
class SoftwareAntivirusUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'inventario.change_softwareantivirus'
    model = SoftwareAntivirus
    form_class = SoftwareAntivirusForm
    template_name = "inventario/software_antivirus_editar.html"
    success_url = reverse_lazy('software_antivirus_listar')
    
        
class SoftwareAntivirusDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'inventario.view_softwareantivirus'
    model = SoftwareAntivirus
    template_name = "inventario/software_antivirus_detalle.html"



#------------------ SoftwareOfimatica--------------------------------------
class SoftwareOfimaticaListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'inventario.view_softwareofimatica'
    model = SoftwareOfimatica
    template_name = "inventario/software_ofimatica_listado.html"

    
class SoftwareOfimaticaCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'inventario.add_softwareofimatica'
    model = SoftwareOfimatica
    form_class = SoftwareOfimaticaForm
    template_name= "inventario/software_ofimatica_crear.html"
    success_url = reverse_lazy('software_ofimatica_listar')


class SoftwareOfimaticaDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'inventario.delete_softwareofimatica'
    model = SoftwareOfimatica
    template_name = "inventario/software_ofimatica_eliminar.html"
    success_url = reverse_lazy('software_ofimatica_listar')
    
    
class SoftwareOfimaticaUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'inventario.change_softwareofimatica'
    model = SoftwareOfimatica
    form_class = SoftwareOfimaticaForm
    template_name = "inventario/software_ofimatica_editar.html"
    success_url = reverse_lazy('software_ofimatica_listar')
    
        
class SoftwareOfimaticaDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'inventario.view_softwareofimatica'
    model = SoftwareOfimatica
    template_name = "inventario/software_ofimatica_detalle.html"



#------------------ SistemaOperativo--------------------------------------
class SistemaOperativoListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'inventario.view_sistemaoperativo'
    model = SistemaOperativo
    template_name = "inventario/sistema_operativo_listado.html"

    
class SistemaOperativoCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'inventario.add_sistemaoperativo'
    model = SistemaOperativo
    form_class = SistemaOperativoForm
    template_name= "inventario/sistema_operativo_crear.html"
    success_url = reverse_lazy('sistema_operativo_listar')


class SistemaOperativoDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'inventario.delete_sistemaoperativo'
    model = SistemaOperativo
    template_name = "inventario/sistema_operativo_eliminar.html"
    success_url = reverse_lazy('sistema_operativo_listar')
    
    
class SistemaOperativoUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'inventario.change_sistemaoperativo'
    model = SistemaOperativo
    form_class = SistemaOperativoForm
    template_name = "inventario/sistema_operativo_editar.html"
    success_url = reverse_lazy('sistema_operativo_listar')
    
class SistemaOperativoDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'inventario.view_sistemaoperativo'
    model = SistemaOperativo
    template_name = "inventario/sistema_operativo_detalle.html"

##mantenimientos para inventario tics hice duplicados
    
class TipoDispositivoInvCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'inventario.add_tipodispositivo'
    model = TipoDispositivo
    form_class = TipoDispositivoForm
    template_name= "inventario/tipo_dispositivoInv_crear.html"
    success_url = reverse_lazy('tipo_dispositivo_listar')

class ModeloInvCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'inventario.add_modelo'
    model = Modelo
    form_class = ModeloForm
    template_name= "inventario/modeloInv_crear.html"
    success_url = reverse_lazy('modelo_listar')

class MarcaInvCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'inventario.add_marca'
    model = Marca
    form_class = MarcaForm
    template_name= "inventario/marcaInv_crear.html"
    success_url = reverse_lazy('marca_listar')



###
###
##

#------------------INVENTARIO TICS--------------------------------------
class InvTicsListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'inventario.view_inventariotics'
    model = InventarioTics
    template_name = "inventario/inv_tics_listado.html"

 #excel 


#Nuestra clase hereda de la vista genérica TemplateView
class InvTicsExcelListView(TemplateView):
     
    #Usamos el método get para generar el archivo excel 
    def get(self, request, *args, **kwargs):
        #Obtenemos todas las lista de nuestra base de listas
        lista = InventarioTics.objects.all()
        #Creamos el libro de trabajo
        wb = Workbook()
        #Definimos como nuestra hoja de trabajo, la hoja activa, por defecto la primera del libro
        ws = wb.active
        #En la celda B1 ponemos el texto 'REPORTE DE lista'
        ws['B1'] = 'INVENTARIO OFICINA TICS'
        #Juntamos las celdas desde la B1 hasta la E1, formando una sola celda
        ws.merge_cells('B1:I1')
        #Creamos los encabezados desde la celda B3 hasta la E3
    
        ws['B3'] = 'TIPO'
        ws['C3'] = 'MARCA'
        ws['D3'] = 'MODELO'
        ws['E3'] = 'SERIE'
        ws['F3'] = 'CODIGO MIES'
        ws['G3'] = 'CANTIDAD'
        ws['H3'] = 'CONDICIÓN'


        #ancho de columna
        ws.column_dimensions['B'].width = 40.0
        ws.column_dimensions['C'].width = 30.0
        ws.column_dimensions['D'].width = 25.0
        ws.column_dimensions['E'].width = 25.0
        ws.column_dimensions['F'].width = 25.0
        ws.column_dimensions['G'].width = 25.0
        ws.column_dimensions['H'].width = 15.0
       
        cont=4
        
        #Recorremos el conjunto de lista y vamos escribiendo cada uno de los listas en las celdas
        for dato in lista:

            if dato.codigoMies is None:
                DatoCodigoMies = 'N/A'
            else:
                DatoCodigoMies = dato.codigoMies
               

            if dato.serie is None:
                DatoSerie = 'N/A'
            else:
                DatoSerie = dato.serie
               
            if dato.marca is None:
                DatoMarca = 'N/A'
            else:
                DatoMarca = dato.marca.descripcion
               
            if dato.modelo is None:
                DatoModelo = 'N/A'
            else:
                 DatoModelo = dato.marca.descripcion

            if dato.condicion == "1":
                DatoCondicion = 'BUENO'
                
            if dato.condicion == "2":
                 DatoCondicion = 'REGULAR'
            if dato.condicion == "3":
                 DatoCondicion = 'DAÑADO'
            
            ws.cell(row=cont,column=2).value = str(dato.tipo)
            ws.cell(row=cont,column=3).value = DatoMarca 
            ws.cell(row=cont,column=4).value =  DatoModelo
            ws.cell(row=cont,column=5).value = DatoSerie
            ws.cell(row=cont,column=6).value = DatoCodigoMies
            ws.cell(row=cont,column=7).value =  dato.cantidad
            ws.cell(row=cont,column=8).value = DatoCondicion
         
            cont = cont + 1
    

        #Establecemos el nombre del archivo
        nombre_archivo ="InventarioTics.xlsx"
        #Definimos que el tipo de respuesta a devolver es un archivo de microsoft excel
        response = HttpResponse(content_type="application/ms-excel") 
        contenido = "attachment; filename={0}".format(nombre_archivo)
        response["Content-Disposition"] = contenido
        wb.save(response)
        return response
 

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



