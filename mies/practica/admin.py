from django.contrib import admin
from practica.models import Universidad,Carrera,Pasante
# Register your models here.
@admin.register(Universidad)
class UniversidadAdmin(admin.ModelAdmin):
    '''Admin View for Universidad'''

    list_display = ('descripcion',)
    list_filter = ('descripcion',)
    search_fields = ('descripcion',)


@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    '''Admin View for Carrera'''

    list_display = ('descripcion','universidad')
    list_filter = ('descripcion','universidad',)
    search_fields = ('descripcion','universidad',)

@admin.register(Pasante)
class PasanteAdmin(admin.ModelAdmin):
    '''Admin View for Pasante'''

    list_display = ('apellidos','nombres','cedula','telefono','tutor_profesional','fecha_inicio','fecha_fin','carrera','horas_diarias','estado',)
    list_filter = ('tutor_profesional','carrera',)
    search_fields = ('cedula','apellidos','nombres','telefono',)

# Register your models here.
