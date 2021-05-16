from django.contrib import admin

# Register your models here.
from custodia.models import Custodia
# Register your models here.
@admin.register(Custodia)
class CustodiaAdmin(admin.ModelAdmin):
    '''Admin View for AccesoRed'''
    list_display = ('fecha','custodio','custodioAnterior','equipo','estado')
    list_editable =('custodio','custodioAnterior','equipo','estado')
    list_filter = ('fecha','custodio','equipo','estado')
    search_fields = ('usuario','custodio','equipo','estado',)
    fieldsets = (
        ("Asignación  del equipo al custodio" , {
            "fields": (
                'fecha',
                'custodio',
                'custodioAnterior',
                'equipo',
                'estado',
                
            ),
        }),
      
    )
    
