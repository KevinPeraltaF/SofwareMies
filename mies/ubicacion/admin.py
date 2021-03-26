from django.contrib import admin
from ubicacion.models import Zona,Provincia,Distrito
# Register your models here.

@admin.register(Zona)
class ZonaAdmin(admin.ModelAdmin):
    '''Admin View for Zona'''

    list_display = ('descripcion',)
    list_filter = ('descripcion',)
    search_fields = ('descripcion',)

@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    '''Admin View for Provincia'''

    list_display = ('descripcion','zona',)
    list_filter = ('zona','descripcion',)
    search_fields = ('zona','descripcion',)
   


@admin.register(Distrito)
class DistritoAdmin(admin.ModelAdmin):
    '''Admin View for Distrito'''

    list_display = ('descripcion','provincia',)
    list_filter = ('provincia','descripcion',)
    search_fields = ('provincia','descripcion',)




