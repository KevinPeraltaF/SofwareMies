"""mies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from usuario import views as usuario_views
from red import views as red_views
from empleado import views as empleado_views
from ubicacion import views as ubicacion_views
from practica import views as practica_views
from actividad import views as actividad_views
from capacitacion import views as capacitacion_views
from inventario import views as inventario_views
from django.conf import settings
from django.conf.urls.static import static
#400
from django.conf.urls import (
handler400, handler403, handler404, handler500
)

urlpatterns = [

    path('admin/', admin.site.urls),
    #MENU PARA LOS USUARIOS
    path('', usuario_views.dashboard_view.as_view(), name="dashboard") ,
   
    #MODULO OTROS
    # ACCESO A REDES  
    path('AccesoRed', red_views.AccesoRedListView.as_view(), name="accesoRed_listar") ,
    path('AccesoRed/Crear', red_views.AccesoRedCreateView.as_view(), name="accesoRed_crear") ,
    path('AccesoRed/Excel', red_views.AccesoRedExcelListView.as_view(), name="accesoRedExcel_crear") ,
    path('AccesoRed/Editar/<int:pk>', red_views.AccesoRedUpdateView.as_view(), name="accesoRed_editar") ,
    path('AccesoRed/Eliminar/<int:pk>', red_views.AccesoRedDeleteView.as_view(), name="accesoRed_eliminar") ,
    path('AccesoRed/Detalle/<int:pk>', red_views.AccesoRedDetailView.as_view(), name="accesoRed_detalle") ,
    #MODULO DE EMPLEADO
    #-- empleado
    path('Empleado', empleado_views.EmpleadoListView.as_view(), name="empleado_listar") ,
    path('Empleado/Crear', empleado_views.EmpleadoCreateView.as_view(), name="empleado_crear") ,
    path('Empleado/Excel', empleado_views.EmpleadoExcelListView.as_view(), name="empleadoExcel_crear") ,
    path('Empleado/Editar/<int:pk>', empleado_views.EmpleadoUpdateView.as_view(), name="empleado_editar") ,
    path('Empleado/Eliminar/<int:pk>', empleado_views.EmpleadoDeleteView.as_view(), name="empleado_eliminar") ,
    path('Empleado/Detalle/<int:pk>', empleado_views.EmpleadoDetailView.as_view(), name="empleado_detalle") ,
    #--area
    path('Area', empleado_views.AreaListView.as_view(), name="area_listar") ,
    path('Area/Crear', empleado_views.AreaCreateView.as_view(), name="area_crear") ,
    path('Area/Editar/<int:pk>', empleado_views.AreaUpdateView.as_view(), name="area_editar") ,
    path('Area/Eliminar/<int:pk>', empleado_views.AreaDeleteView.as_view(), name="area_eliminar") ,
    path('Area/Detalle/<int:pk>', empleado_views.AreaDetailView.as_view(), name="area_detalle") ,
    #--cargo
    path('Cargo', empleado_views.CargoListView.as_view(), name="cargo_listar") ,
    path('Cargo/Crear', empleado_views.CargoCreateView.as_view(), name="cargo_crear") ,
    path('Cargo/Editar/<int:pk>', empleado_views.CargoUpdateView.as_view(), name="cargo_editar") ,
    path('Cargo/Eliminar/<int:pk>', empleado_views.CargoDeleteView.as_view(), name="cargo_eliminar") ,
    path('Cargo/Detalle/<int:pk>', empleado_views.CargoDetailView.as_view(), name="cargo_detalle") ,
    #--unidad de atencion
    path('UnidadAtencion', empleado_views.UnidadListView.as_view(), name="unidad_listar") ,
    path('UnidadAtencion/Crear', empleado_views.UnidadCreateView.as_view(), name="unidad_crear") ,
    path('UnidadAtencion/Editar/<int:pk>', empleado_views.UnidadUpdateView.as_view(), name="unidad_editar") ,
    path('UnidadAtencion/Eliminar/<int:pk>', empleado_views.UnidadDeleteView.as_view(), name="unidad_eliminar") ,
    path('UnidadAtencion/Detalle/<int:pk>', empleado_views.UnidadDetailView.as_view(), name="unidad_detalle") ,
    #MODULO UBICACION DISTRITAL
    #--zona
    path('Zona', ubicacion_views.ZonaListView.as_view(), name="zona_listar") ,
    path('Zona/Crear', ubicacion_views.ZonaCreateView.as_view(), name="zona_crear") ,
    path('Zona/Editar/<int:pk>', ubicacion_views.ZonaUpdateView.as_view(), name="zona_editar") ,
    path('Zona/Eliminar/<int:pk>', ubicacion_views.ZonaDeleteView.as_view(), name="zona_eliminar") ,
    path('Zona/Detalle/<int:pk>', ubicacion_views.ZonaDetailView.as_view(), name="zona_detalle") ,
    #--provincia
    path('Provincia', ubicacion_views.ProvinciaListView.as_view(), name="provincia_listar") ,
    path('Provincia/Crear', ubicacion_views.ProvinciaCreateView.as_view(), name="provincia_crear") ,
    path('Provincia/Editar/<int:pk>', ubicacion_views.ProvinciaUpdateView.as_view(), name="provincia_editar") ,
    path('Provincia/Eliminar/<int:pk>', ubicacion_views.ProvinciaDeleteView.as_view(), name="provincia_eliminar") ,
    path('Provincia/Detalle/<int:pk>', ubicacion_views.ProvinciaDetailView.as_view(), name="provincia_detalle") ,
    #--distrito
    path('Distrito', ubicacion_views.DistritoListView.as_view(), name="distrito_listar") ,
    path('Distrito/Crear', ubicacion_views.DistritoCreateView.as_view(), name="distrito_crear") ,
    path('Distrito/Editar/<int:pk>', ubicacion_views.DistritoUpdateView.as_view(), name="distrito_editar") ,
    path('Distrito/Eliminar/<int:pk>', ubicacion_views.DistritoDeleteView.as_view(), name="distrito_eliminar") ,
    path('Distrito/Detalle/<int:pk>', ubicacion_views.DistritoDetailView.as_view(), name="distrito_detalle") ,
    #MODULO PRACTICAS PROFESIONALIZANTES
    #--Pasante
    path('Pasante', practica_views.PasanteListView.as_view(), name="pasante_listar") ,
    path('Pasante/Crear', practica_views.PasanteCreateView.as_view(), name="pasante_crear") ,
    path('Pasante/Excel', practica_views.PasanteExcelListView.as_view(), name="pasanteExcel_crear") ,
    path('Pasante/Editar/<int:pk>', practica_views.PasanteUpdateView.as_view(), name="pasante_editar") ,
    path('Pasante/Eliminar/<int:pk>', practica_views.PasanteDeleteView.as_view(), name="pasante_eliminar") ,
    path('Pasante/Detalle/<int:pk>', practica_views.PasanteDetailView.as_view(), name="pasante_detalle") ,
    #--Carrera
    path('Carrera', practica_views.CarreraListView.as_view(), name="carrera_listar") ,
    path('Carrera/Crear', practica_views.CarreraCreateView.as_view(), name="carrera_crear") ,
    path('Carrera/Editar/<int:pk>', practica_views.CarreraUpdateView.as_view(), name="carrera_editar") ,
    path('Carrera/Eliminar/<int:pk>', practica_views.CarreraDeleteView.as_view(), name="carrera_eliminar") ,
    path('Carrera/Detalle/<int:pk>', practica_views.CarreraDetailView.as_view(), name="carrera_detalle") ,
    #--Universidad
    path('Universidad', practica_views.UniversidadListView.as_view(), name="universidad_listar") ,
    path('Universidad/Crear', practica_views.UniversidadCreateView.as_view(), name="universidad_crear") ,
    path('Universidad/Editar/<int:pk>', practica_views.UniversidadUpdateView.as_view(), name="universidad_editar") ,
    path('Universidad/Eliminar/<int:pk>', practica_views.UniversidadDeleteView.as_view(), name="universidad_eliminar") ,
    path('Universidad/Detalle/<int:pk>', practica_views.UniversidadDetailView.as_view(), name="universidad_detalle") ,
    

    #MODULO ACTIVIDAD
    #--Actividad
    path('Actividad', actividad_views.ActividadListView.as_view(), name="actividad_listar"),
    path('Actividad/Crear',actividad_views.ActividadCreateView.as_view(),name ="actividad_crear"),
    path('Actividad/pdf/<int:pk>', actividad_views.ActividadReportePdfDetailView.as_view(), name="actividad_reporte_pdf") ,
    path('Actividad/Editar/<int:pk>',actividad_views.ActividadUpdateView.as_view(),name ="actividad_editar"),
    path('Actividad/Eliminar/<int:pk>',actividad_views.ActividadDeleteView.as_view(),name ="actividad_eliminar"),
    path('Actividad/Detalle/<int:pk>',actividad_views.ActividadDetailView.as_view(),name ="actividad_detalle"),
   
    #--Asunto
    path('Asunto', actividad_views.AsuntoListView.as_view(), name="asunto_listar"),
    path('Asunto/Crear',actividad_views.AsuntoCreateView.as_view(),name ="asunto_crear"),
    path('Asunto/Editar/<int:pk>',actividad_views.AsuntoUpdateView.as_view(),name ="asunto_editar"),
    path('Asunto/Eliminar/<int:pk>',actividad_views.AsuntoDeleteView.as_view(),name ="asunto_eliminar"),
    path('Asunto/Detalle/<int:pk>',actividad_views.AsuntoDetailView.as_view(),name ="asunto_detalle"),

     #--Capacitacion
    path('Capacitacion', capacitacion_views.CapacitacionListView.as_view(), name="capacitacion_listar") ,
    path('Capacitacion/Crear', capacitacion_views.CapacitacionCreateView.as_view(), name="capacitacion_crear") ,
    path('Capacitacion/Editar/<int:pk>', capacitacion_views.CapacitacionUpdateView.as_view(), name="capacitacion_editar") ,
    path('Capacitacion/Eliminar/<int:pk>', capacitacion_views.CapacitacionDeleteView.as_view(), name="capacitacion_eliminar") ,
    path('Capacitacion/Detalle/<int:pk>', capacitacion_views.CapacitacionDetailView.as_view(), name="capacitacion_detalle") ,
    path('Capacitacion/pdf/<int:pk>', capacitacion_views.CapacitacionReportePdfDetailView.as_view(), name="capacitacion_reporte_pdf") ,


    #Modulo Inventario 
    #--Marca
    path('Marca', inventario_views.MarcaListView.as_view(), name="marca_listar"),
    path('Marca/Crear',inventario_views.MarcaCreateView.as_view(),name ="marca_crear"),
    path('Marca/Editar/<int:pk>',inventario_views.MarcaUpdateView.as_view(),name ="marca_editar"),
    path('Marca/Eliminar/<int:pk>',inventario_views.MarcaDeleteView.as_view(),name ="marca_eliminar"),
    path('Marca/Detalle/<int:pk>',inventario_views.MarcaDetailView.as_view(),name ="marca_detalle"),
    #--Modelo
    path('Modelo', inventario_views.ModeloListView.as_view(), name="modelo_listar"),
    path('Modelo/Crear',inventario_views.ModeloCreateView.as_view(),name ="modelo_crear"),
    path('Modelo/Editar/<int:pk>',inventario_views.ModeloUpdateView.as_view(),name ="modelo_editar"),
    path('Modelo/Eliminar/<int:pk>',inventario_views.ModeloDeleteView.as_view(),name ="modelo_eliminar"),
    path('Modelo/Detalle/<int:pk>',inventario_views.ModeloDetailView.as_view(),name ="modelo_detalle"),
    #--CAPACIDAD DISCO
    path('CapacidadDisco', inventario_views.CapacidadDiscoListView.as_view(), name="capacidad_disco_listar"),
    path('CapacidadDisco/Crear',inventario_views.CapacidadDiscoCreateView.as_view(),name ="capacidad_disco_crear"),
    path('CapacidadDisco/Editar/<int:pk>',inventario_views.CapacidadDiscoUpdateView.as_view(),name ="capacidad_disco_editar"),
    path('CapacidadDisco/Eliminar/<int:pk>',inventario_views.CapacidadDiscoDeleteView.as_view(),name ="capacidad_disco_eliminar"),
    path('CapacidadDisco/Detalle/<int:pk>',inventario_views.CapacidadDiscoDetailView.as_view(),name ="capacidad_disco_detalle"),
    #--CAPACIDAD MEMORIA
    path('CapacidadMemoriaRam', inventario_views.CapacidadMemoriaRamListView.as_view(), name="capacidad_memoria_ram_listar"),
    path('CapacidadMemoriaRam/Crear',inventario_views.CapacidadMemoriaRamCreateView.as_view(),name ="capacidad_memoria_ram_crear"),
    path('CapacidadMemoriaRam/Editar/<int:pk>',inventario_views.CapacidadMemoriaRamUpdateView.as_view(),name ="capacidad_memoria_ram_editar"),
    path('CapacidadMemoriaRam/Eliminar/<int:pk>',inventario_views.CapacidadMemoriaRamDeleteView.as_view(),name ="capacidad_memoria_ram_eliminar"),
    path('CapacidadMemoriaRam/Detalle/<int:pk>',inventario_views.CapacidadMemoriaRamDetailView.as_view(),name ="capacidad_memoria_ram_detalle"),
    #--Procesador
    path('Procesador', inventario_views.ProcesadorListView.as_view(), name="procesador_listar"),
    path('Procesador/Crear',inventario_views.ProcesadorCreateView.as_view(),name ="procesador_crear"),
    path('Procesador/Editar/<int:pk>',inventario_views.ProcesadorUpdateView.as_view(),name ="procesador_editar"),
    path('Procesador/Eliminar/<int:pk>',inventario_views.ProcesadorDeleteView.as_view(),name ="procesador_eliminar"),
    path('Procesador/Detalle/<int:pk>',inventario_views.ProcesadorDetailView.as_view(),name ="procesador_detalle"),
    #dispositivo
    path('dispositivo', inventario_views.DispositivoListView.as_view(), name="dispositivo_listar"),
    path('dispositivo/Crear',inventario_views.DispositivoCreateView.as_view(),name ="dispositivo_crear"),
    path('dispositivo/Editar/<int:pk>',inventario_views.DispositivoUpdateView.as_view(),name ="dispositivo_editar"),
    path('dispositivo/Eliminar/<int:pk>',inventario_views.DispositivoDeleteView.as_view(),name ="dispositivo_eliminar"),
    path('dispositivo/Detalle/<int:pk>',inventario_views.DispositivoDetailView.as_view(),name ="dispositivo_detalle"),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]



