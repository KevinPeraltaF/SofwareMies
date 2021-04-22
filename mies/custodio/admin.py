from django.contrib import admin

# Register your models here.
from custodio.models import Custodio
# Register your models here.
@admin.register(Custodio)
class CustodioAdmin(admin.ModelAdmin):
    '''Admin View for AccesoRed'''
    list_display = ('fecha','custodio','equipo','estado')
    list_editable =('custodio','equipo','estado')
    list_filter = ('fecha','custodio','equipo','estado')
    search_fields = ('usuario','custodio','equipo','estado',)
    fieldsets = (
        ("Asignación  del equipo al custodio" , {
            "fields": (
                'fecha',
                'custodio',
                'equipo',
                'estado',
                
            ),
        }),
      
    )
    
