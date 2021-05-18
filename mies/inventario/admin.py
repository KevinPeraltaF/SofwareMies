from django.contrib import admin
from inventario.models import Marca, Modelo,Dispositivo,CapacidadDisco,CapacidadMemoriaRam,Procesador , TipoDispositivo, TipoImpresora,ImpresoraTecnologia ,SoftwareAntivirus , SoftwareOfimatica,SistemaOperativo,TipoEquipo,InventarioTics
# Register your models here.

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    '''Admin View for Marca'''

    list_display = ('descripcion',)
    list_filter = ('descripcion',)
    search_fields = ('descripcion',)

@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    '''Admin View for Modelo'''

    list_display = ('descripcion',)
    list_filter = ('descripcion',)
    search_fields = ('descripcion',)

@admin.register(CapacidadDisco)
class CapacidadDiscoAdmin(admin.ModelAdmin):
    '''Admin View for CapacidadDisco'''

    list_display = ('descripcion',)
    list_filter = ('descripcion',)
    search_fields = ('descripcion',)

@admin.register(CapacidadMemoriaRam)
class CapacidadMemoriaRamAdmin(admin.ModelAdmin):
    '''Admin View for CapacidadMemoriaRam'''

    list_display = ('descripcion',)
    list_filter = ('descripcion',)
    search_fields = ('descripcion',)

@admin.register(Procesador)
class ProcesadorAdmin(admin.ModelAdmin):
    '''Admin View for Procesador'''

    list_display = ('descripcion',)
    list_filter = ('descripcion',)
    search_fields = ('descripcion',)
#######333
@admin.register(TipoEquipo)
class TipoEquipoAdmin(admin.ModelAdmin):
    '''Admin View for TipoEquipo'''

    list_display = ('descripcion',)
    list_filter = ('descripcion',)
    search_fields = ('descripcion',)


@admin.register(SistemaOperativo)
class SistemaOperativoAdmin(admin.ModelAdmin):
    '''Admin View for SistemaOperativo'''

    list_display = ('descripcion',)
    list_filter = ('descripcion',)
    search_fields = ('descripcion',)


@admin.register(SoftwareOfimatica)
class SoftwareOfimaticaAdmin(admin.ModelAdmin):
    '''Admin View for SoftwareOfimatica'''

    list_display = ('descripcion',)
    list_filter = ('descripcion',)
    search_fields = ('descripcion',)



@admin.register(SoftwareAntivirus)
class SoftwareAntivirusAdmin(admin.ModelAdmin):
    '''Admin View for SoftwareAntivirus'''

    list_display = ('descripcion',)
    list_filter = ('descripcion',)
    search_fields = ('descripcion',)

@admin.register(ImpresoraTecnologia)
class ImpresoraTecnologiaAdmin(admin.ModelAdmin):
    '''Admin View for ImpresoraTecnologia'''

    list_display = ('descripcion',)
    list_filter = ('descripcion',)
    search_fields = ('descripcion',)

@admin.register(TipoImpresora)
class TipoImpresoraAdmin(admin.ModelAdmin):
    '''Admin View for TipoImpresora'''

    list_display = ('descripcion',)
    list_filter = ('descripcion',)
    search_fields = ('descripcion',)

@admin.register(TipoDispositivo)
class TipoDispositivoAdmin(admin.ModelAdmin):
    '''Admin View for TipoDispositivo'''

    list_display = ('descripcion',)
    list_filter = ('descripcion',)
    search_fields = ('descripcion',)




@admin.register(Dispositivo)
class DispositivoAdmin(admin.ModelAdmin):
    '''Admin View for Dispositivo'''

    list_display = ('categoria','nombreEquipo','tipoEquipo','marca',
    'modelo','serie' ,'codigoMies' ,'capacidadProcesador','capacidadDisco','capacidadMemoriaRam' ,'sistemaOperativo','direccionIp','direccionMac','ofimatica','antivirus','softwareAdicional','tecnologia','tipoImpresora','tipoDispositivo','estado','observacion','foto',)
    list_filter = ('categoria','tipoEquipo','tipoImpresora',
    'tipoDispositivo','sistemaOperativo' ,'tecnologia' ,)
    search_fields = ('nombreEquipo','serie' ,'codigoMies',)


####
##
##
##3
@admin.register(InventarioTics)
class InventarioTicsAdmin(admin.ModelAdmin):
    '''Admin View for InventarioTics'''
    list_display = ('descripcion','marca',
    'modelo','condicion','serie' ,'codigoMies' ,'cantidad' ,'foto',)
    list_filter = ('marca','modelo','condicion',)
    search_fields = ('descripcion','serie' ,'codigoMies','marca','modelo',)