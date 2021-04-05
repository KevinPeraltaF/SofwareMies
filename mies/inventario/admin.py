from django.contrib import admin
from inventario.models import Marca, Modelo, Categoria,Condicion,InventarioTics,InvetarioDistritoCabecera,CapacidadDisco,CapacidadMemoriaRam,Procesador, InventarioDistritoDetalle
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

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    '''Admin View for Categoria'''

    list_display = ('descripcion',)
    list_filter = ('descripcion',)
    search_fields = ('descripcion',)

@admin.register(Condicion)
class CondicionAdmin(admin.ModelAdmin):
    '''Admin View for Condicion'''
    list_display = ('descripcion',)
    list_filter = ('descripcion',)
    search_fields = ('descripcion',)


@admin.register(InventarioTics)
class InventarioTicsAdmin(admin.ModelAdmin):
    '''Admin View for InventarioTics'''

    list_display = ('fechaIngreso','responsable','ubicacion','categoria','descripcion','marca',
    'modelo','condicion','serie' ,'codigoMies' ,'cantidad' ,'foto',)
    list_filter = ('ubicacion','categoria','descripcion','marca',
    'modelo','condicion','serie' ,'codigoMies' ,)
    search_fields = ('ubicacion','categoria','descripcion','marca',
    'modelo','condicion','serie' ,'codigoMies',)

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






class ListadoDetalleInventarioDistrital(admin.TabularInline):
    model=InventarioDistritoDetalle
    fk_name ="cabeceraDistrito"
    extra = 4


@admin.register(InvetarioDistritoCabecera)
class InventarioDistritalAdmin(admin.ModelAdmin ):
    '''Admin View for InventarioDistrital'''
    inlines = (ListadoDetalleInventarioDistrital,)
    list_display = ('fechaIngreso','descripcion','direccionIp' ,'direccionMac','responsable','ubicacion','categoria','marca',
    'modelo','condicion','serie' ,'codigoMies' ,'foto')
    list_filter = ('ubicacion','categoria','descripcion','marca',
    'modelo','condicion','serie' ,'codigoMies','direccionIp' ,'direccionMac',)
    search_fields = ('ubicacion','categoria','descripcion','marca',
    'modelo','condicion','serie' ,'codigoMies','direccionIp' ,'direccionMac',)

# Register your models here.
