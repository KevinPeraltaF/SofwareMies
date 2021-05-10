from django.contrib import admin
from inventario.models import Marca, Modelo, Categoria,Condicion,InventarioTics,CapacidadDisco,CapacidadMemoriaRam,Procesador,\
    EquipoCabecera, EquipoDetalle
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

    list_display = ('fechaIngreso','responsable','categoria','descripcion','marca',
    'modelo','condicion','serie' ,'codigoMies' ,'cantidad' ,'foto',)
    list_filter = ('categoria','descripcion','marca',
    'modelo','condicion','serie' ,'codigoMies' ,)
    search_fields = ('descripcion','serie' ,'codigoMies',)

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


class EquipoDetalleTab(admin.TabularInline):
    model=EquipoDetalle
    fk_name ="cabeceraDistrito"
    extra = 4
@admin.register(EquipoCabecera)
class EquipoAdmin(admin.ModelAdmin):
    '''Admin View for Procesador'''
    inlines = (EquipoDetalleTab,)
    list_display = ('descripcion',)
    list_filter = ('descripcion',)
    search_fields = ('descripcion',)


# Register your models here.
