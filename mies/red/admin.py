from django.contrib import admin
from red.models import AccesoRed
# Register your models here.
@admin.register(AccesoRed)
class AccesoRedAdmin(admin.ModelAdmin):
    '''Admin View for AccesoRed'''
    list_display = ('usuario','direccion_mac','direccion_ip','observacion','estado')
    list_display_links = ('usuario',)
    list_editable =('direccion_mac','direccion_ip','estado')
    list_filter = ('usuario','direccion_mac','direccion_ip',)
    search_fields = ('usuario','direccion_mac','direccion_ip',)
    fieldsets = (
        ("Información del equipo", {
            "fields": (
              
                'usuario',
                'direccion_mac',
                'direccion_ip',
                'estado',
                
            ),
        }),
        ("Información Extra",{
            "fields":(
                'observacion',
                
            )
        })
    )
    
