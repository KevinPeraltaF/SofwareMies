from django.contrib import admin
from inventario.models import Marca, Modelo,Dispositivo,CapacidadDisco,CapacidadMemoriaRam,Procesador
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



@admin.register(Dispositivo)
class DispositivoAdmin(admin.ModelAdmin):
    '''Admin View for Dispositivo'''

    list_display = ('categoria','nombreEquipo','tipoEquipo','marca',
    'modelo','serie' ,'codigoMies' ,'capacidadProcesador','capacidadDisco','capacidadMemoriaRam' ,'sistemaOperativo','direccionIp','direccionMac','ofimatica','antivirus','softwareAdicional','tecnologia','tipoImpresora','tipoDispositivo','estado','observacion','foto',)
    list_filter = ('categoria','tipoEquipo','tipoImpresora',
    'tipoDispositivo','sistemaOperativo' ,'tecnologia' ,)
    search_fields = ('nombreEquipo','serie' ,'codigoMies',)