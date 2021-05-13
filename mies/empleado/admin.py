from django.contrib import admin
from empleado.models import Area,Cargo,UnidadAtencion,Empleado
# Register your models here.

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    '''Admin View for Area'''

    list_display = ('descripcion','distrito',)
    list_filter = ('descripcion',)
    search_fields = ('distrito','descripcion',)


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    '''Admin View for Cargo'''

    list_display = ('descripcion',)
    list_filter = ('descripcion',)
    search_fields = ('descripcion',)


@admin.register(UnidadAtencion)
class UnidadAtencionAdmin(admin.ModelAdmin):
    '''Admin View for UnidadAtencion'''

    list_display = ('descripcion','codigo',)
    list_filter = ('descripcion','codigo',)
    search_fields = ('descripcion','codigo',)

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    '''Admin View for Empleado'''

    list_display = ('area' ,'cargo','unidadAtencion','nombres','apellidos' ,'genero' ,'correo','cedula','telefono','foto','estado',)
    list_editable = ('cargo','unidadAtencion','nombres','apellidos' ,'genero' ,'correo','cedula','telefono','foto','estado',)
    list_filter = ('nombres','apellidos', 'unidadAtencion','correo','cedula',)
    search_fields = ('correo','cedula','nombres','apellidos',)
    fieldsets = (
        ("Información Personal",{
            "fields":(
                'nombres',
                'apellidos',
                'cedula',
                'telefono',
                'correo',
                'genero',
                'foto',
                
            )
        }),
        ("Información Empresarial", {
            "fields": (
                'area',
                'cargo',
                'unidadAtencion',
                'estado',
                
            ),
        })

    )

# Register your models here.
