from django.contrib import admin
from prestamo.models import Prestamo


@admin.register(Prestamo)
class Admin(admin.ModelAdmin):
    list_display = ('item','condicion','cantidad','usuario','estado','fecha_entrega','fecha_devolucion','observacion')
    list_filter = ('usuario','item')
    search_fields = ('usuario',)
    fieldsets = (
        ("Información de Préstamo", {
            "fields": (
                'fecha_entrega',
                'fecha_devolucion',
                'usuario',
                
                
                
            ),
        }),
        ("Detalle Préstamo", {
            "fields": (
                'item',
                'cantidad',
                'condicion',
                'observacion',
                'estado',
            ),
        }),
    )