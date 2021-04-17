from django.contrib import admin
from atencion.models import TipoDocumento, Atencion, AtencionDetalle
# Register your models here.
@admin.register(TipoDocumento)
class TipoDocumentoAdmin(admin.ModelAdmin):
    '''Admin View for TipoDocumento'''
    list_display = ('descripcion',)
    list_filter = ('descripcion',)
    search_fields = ('descripcion',)


class ListadoDetalleAtencion(admin.TabularInline):
    model=AtencionDetalle
    extra =1


@admin.register(Atencion)
class AtencionAdmin(admin.ModelAdmin):
    '''Admin View for Atencion'''
    inlines=(ListadoDetalleAtencion,)
    list_display = ('equipo','responsable','tipoDocumento','fecha_salida','hora_salida','instalacion','configuracion','prueba','capacitacion','hardware','software')
    list_filter = ('equipo','fechaIncidente','tipoDocumento',)
    search_fields = ('equipo','fechaIncidente','tipoDocumento',)
    exclude=("contadorDocumento ",)
    readonly_fields=('contadorDocumento',)