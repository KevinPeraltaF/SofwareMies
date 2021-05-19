from django.contrib import admin
from .models import Configuracion

# Register your models here.
@admin.register(Configuracion)
class CargoAdmin(admin.ModelAdmin):
    '''Admin View for Configuracion'''
    list_display = ('encargadoTics','encargadoBienes','logoIzquierdo','logocentro','logoDerecho',)
    list_filter = ('encargadoTics','encargadoBienes',)
    search_fields = ('encargadoTics','encargadoBienes')
