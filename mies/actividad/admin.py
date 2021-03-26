from django.contrib import admin
from actividad.models import ActividadCabecera ,ActividadDetalle, Prioridad, Asunto
# Register your models here.

@admin.register(Asunto)
class AsuntoAdmin(admin.ModelAdmin):
    '''Admin View for Asunto'''

    list_display = ('descripcion',)
    list_filter = ('descripcion',)
    search_fields = ('descripcion',)


@admin.register(Prioridad)
class PrioridadAdmin(admin.ModelAdmin):
    '''Admin View for Prioridad'''

    list_display = ('descripcion',)
    list_filter = ('descripcion',)
    search_fields = ('descripcion',)

class ActividadDetalleInline(admin.TabularInline):
    '''Tabular Inline View for ActividadDetalle'''
    model = ActividadDetalle
    extra = 1
        
@admin.register(ActividadCabecera)
class ActividadAdmin(admin.ModelAdmin):
    '''Admin View for ActividadCabecera'''
    inlines =(ActividadDetalleInline,)
    list_display = ('fecha','responsable','ubicacion','prioridad')
    list_filter = ('prioridad',)
    search_fields = ('responsable','empleado','ubicacion',)

# Register your models here.
