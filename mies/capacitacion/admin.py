from django.contrib import admin
from capacitacion.models import TipoCapacitacion, CapacitacionCabecera, CapacitacionDetalle
# Register your models here.
@admin.register(TipoCapacitacion)
class TipoCapacitacionAdmin(admin.ModelAdmin):
    '''Admin View for TipoCapacitacion'''

    list_display = ('descripcion',)
    list_filter = ('descripcion',)
    search_fields = ('descripcion',)


class CapacitacionInline(admin.TabularInline):
    '''Tabular Inline View for Capacitacion'''
    model = CapacitacionDetalle
    extra = 1

@admin.register(CapacitacionCabecera)
class CapacitacionCabeceraAdmin(admin.ModelAdmin):
    '''Admin View for CapacitacionCabecera'''
    inlines = (CapacitacionInline,)
    list_display = ('tema','lugar','fecha','hora_inicio','hora_fin')
    list_filter = ('tema','lugar',)
    search_fields = ('tema','lugar',)


# Register your models here.
