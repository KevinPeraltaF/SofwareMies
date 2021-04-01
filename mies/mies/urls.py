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
from inventario import views as inventaio_views
from prestamo import views as prestamo_views
from practica import views as practica_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    #MENU PARA LOS USUARIOS
    path('', usuario_views.dashboardUsuario_view, name="dashboard") ,
    #MODULO OTROS
    # ACCESO A REDES
    path('AccesoRed', red_views.AccesoRedListView.as_view(), name="accesoRed_listar") ,
    path('AccesoRed/Crear', red_views.AccesoRedCreateView.as_view(), name="accesoRed_crear") ,
    path('AccesoRed/Editar/<pk>', red_views.AccesoRedUpdateView.as_view(), name="accesoRed_editar") ,
    path('AccesoRed/Eliminar/<pk>', red_views.AccesoRedDeleteView.as_view(), name="accesoRed_eliminar") ,
    path('AccesoRed/Detalle/<pk>', red_views.AccesoRedDetailView.as_view(), name="accesoRed_detalle") ,
    #MODULO DE EMPLEADO
    #-- empleado
    path('Empleado', empleado_views.EmpleadoListView.as_view(), name="empleado_listar") ,
    path('Empleado/Crear', empleado_views.EmpleadoCreateView.as_view(), name="empleado_crear") ,
    path('Empleado/Editar/<pk>', empleado_views.EmpleadoUpdateView.as_view(), name="empleado_editar") ,
    path('Empleado/Eliminar/<pk>', empleado_views.EmpleadoDeleteView.as_view(), name="empleado_eliminar") ,
    path('Empleado/Detalle/<pk>', empleado_views.EmpleadoDetailView.as_view(), name="empleado_detalle") ,
    #--area
    path('Area', empleado_views.AreaListView.as_view(), name="area_listar") ,
    path('Area/Crear', empleado_views.AreaCreateView.as_view(), name="area_crear") ,
    path('Area/Editar/<pk>', empleado_views.AreaUpdateView.as_view(), name="area_editar") ,
    path('Area/Eliminar/<pk>', empleado_views.AreaDeleteView.as_view(), name="area_eliminar") ,
    path('Area/Detalle/<pk>', empleado_views.AreaDetailView.as_view(), name="area_detalle") ,
    #--cargo
    path('Cargo', empleado_views.CargoListView.as_view(), name="cargo_listar") ,
    path('Cargo/Crear', empleado_views.CargoCreateView.as_view(), name="cargo_crear") ,
    path('Cargo/Editar/<pk>', empleado_views.CargoUpdateView.as_view(), name="cargo_editar") ,
    path('Cargo/Eliminar/<pk>', empleado_views.CargoDeleteView.as_view(), name="cargo_eliminar") ,
    path('Cargo/Detalle/<pk>', empleado_views.CargoDetailView.as_view(), name="cargo_detalle") ,
    #--unidad de atencion
    path('UnidadAtencion', empleado_views.UnidadListView.as_view(), name="unidad_listar") ,
    path('UnidadAtencion/Crear', empleado_views.UnidadCreateView.as_view(), name="unidad_crear") ,
    path('UnidadAtencion/Editar/<pk>', empleado_views.UnidadUpdateView.as_view(), name="unidad_editar") ,
    path('UnidadAtencion/Eliminar/<pk>', empleado_views.UnidadDeleteView.as_view(), name="unidad_eliminar") ,
    path('UnidadAtencion/Detalle/<pk>', empleado_views.UnidadDetailView.as_view(), name="unidad_detalle") ,
    #MODULO UBICACION DISTRITAL
    #--zona
    path('Zona', ubicacion_views.ZonaListView.as_view(), name="zona_listar") ,
    path('Zona/Crear', ubicacion_views.ZonaCreateView.as_view(), name="zona_crear") ,
    path('Zona/Editar/<pk>', ubicacion_views.ZonaUpdateView.as_view(), name="zona_editar") ,
    path('Zona/Eliminar/<pk>', ubicacion_views.ZonaDeleteView.as_view(), name="zona_eliminar") ,
    path('Zona/Detalle/<pk>', ubicacion_views.ZonaDetailView.as_view(), name="zona_detalle") ,
    #--provincia
    path('Provincia', ubicacion_views.ProvinciaListView.as_view(), name="provincia_listar") ,
    path('Provincia/Crear', ubicacion_views.ProvinciaCreateView.as_view(), name="provincia_crear") ,
    path('Provincia/Editar/<pk>', ubicacion_views.ProvinciaUpdateView.as_view(), name="provincia_editar") ,
    path('Provincia/Eliminar/<pk>', ubicacion_views.ProvinciaDeleteView.as_view(), name="provincia_eliminar") ,
    path('Provincia/Detalle/<pk>', ubicacion_views.ProvinciaDetailView.as_view(), name="provincia_detalle") ,
    #--distrito
    path('Distrito', ubicacion_views.DistritoListView.as_view(), name="distrito_listar") ,
    path('Distrito/Crear', ubicacion_views.DistritoCreateView.as_view(), name="distrito_crear") ,
    path('Distrito/Editar/<pk>', ubicacion_views.DistritoUpdateView.as_view(), name="distrito_editar") ,
    path('Distrito/Eliminar/<pk>', ubicacion_views.DistritoDeleteView.as_view(), name="distrito_eliminar") ,
    path('Distrito/Detalle/<pk>', ubicacion_views.DistritoDetailView.as_view(), name="distrito_detalle") ,
    #Modulo Inventario Tics
    #--Marca
    path('Marca', inventaio_views.MarcaListView.as_view(), name="marca_listar"),
    path('Marca/Crear',inventaio_views.MarcaCreateView.as_view(),name ="marca_crear"),
    path('Marca/Editar/<pk>',inventaio_views.MarcaUpdateView.as_view(),name ="marca_editar"),
    path('Marca/Eliminar/<pk>',inventaio_views.MarcaDeleteView.as_view(),name ="marca_eliminar"),
    path('Marca/Detalle/<pk>',inventaio_views.MarcaDetailView.as_view(),name ="marca_detalle"),
    #--Modelo
    path('Modelo', inventaio_views.ModeloListView.as_view(), name="modelo_listar"),
    path('Modelo/Crear',inventaio_views.ModeloCreateView.as_view(),name ="modelo_crear"),
    path('Modelo/Editar/<pk>',inventaio_views.ModeloUpdateView.as_view(),name ="modelo_editar"),
    path('Modelo/Eliminar/<pk>',inventaio_views.ModeloDeleteView.as_view(),name ="modelo_eliminar"),
    path('Modelo/Detalle/<pk>',inventaio_views.ModeloDetailView.as_view(),name ="modelo_detalle"),
    #--Categoria
    path('Categoria', inventaio_views.CategoriaListView.as_view(), name="categoria_listar"),
    path('Categoria/Crear',inventaio_views.CategoriaCreateView.as_view(),name ="categoria_crear"),
    path('Categoria/Editar/<pk>',inventaio_views.CategoriaUpdateView.as_view(),name ="categoria_editar"),
    path('Categoria/Eliminar/<pk>',inventaio_views.CategoriaDeleteView.as_view(),name ="categoria_eliminar"),
    path('Categoria/Detalle/<pk>',inventaio_views.CategoriaDetailView.as_view(),name ="categoria_detalle"),
    #--Condicion
    path('Condicion', inventaio_views.CondicionListView.as_view(), name="condicion_listar"),
    path('Condicion/Crear',inventaio_views.CondicionCreateView.as_view(),name ="condicion_crear"),
    path('Condicion/Editar/<pk>',inventaio_views.CondicionUpdateView.as_view(),name ="condicion_editar"),
    path('Condicion/Eliminar/<pk>',inventaio_views.CondicionDeleteView.as_view(),name ="condicion_eliminar"),
    path('Condicion/Detalle/<pk>',inventaio_views.CondicionDetailView.as_view(),name ="condicion_detalle"),
    #--INVENTARIO TICS
    path('InvTics', inventaio_views.InvTicsListView.as_view(), name="inv_tics_listar"),
    path('InvTics/Crear',inventaio_views.InvTicsCreateView.as_view(),name ="inv_tics_crear"),
    path('InvTics/Editar/<pk>',inventaio_views.InvTicsUpdateView.as_view(),name ="inv_tics_editar"),
    path('InvTics/Eliminar/<pk>',inventaio_views.InvTicsDeleteView.as_view(),name ="inv_tics_eliminar"),
    path('InvTics/Detalle/<pk>',inventaio_views.InvTicsDetailView.as_view(),name ="inv_tics_detalle"),
    #MODULO OTRO
    # --PRESTAMO
    path('Prestamo', prestamo_views.PrestamoListView.as_view(), name="prestamo_listar"),
    path('Prestamo/Crear',prestamo_views.PrestamoCreateView.as_view(),name ="prestamo_crear"),
    path('Prestamo/Editar/<pk>',prestamo_views.PrestamoUpdateView.as_view(),name ="prestamo_editar"),
    path('Prestamo/Eliminar/<pk>',prestamo_views.PrestamoDeleteView.as_view(),name ="prestamo_eliminar"),
    path('Prestamo/Detalle/<pk>',prestamo_views.PrestamoDetailView.as_view(),name ="prestamo_detalle"),
    #MODULO PRACTICAS PROFESIONALIZANTES
    #--Pasante
    path('Pasante', practica_views.PasanteListView.as_view(), name="pasante_listar") ,
    path('Pasante/Crear', practica_views.PasanteCreateView.as_view(), name="pasante_crear") ,
    path('Pasante/Editar/<pk>', practica_views.PasanteUpdateView.as_view(), name="pasante_editar") ,
    path('Pasante/Eliminar/<pk>', practica_views.PasanteDeleteView.as_view(), name="pasante_eliminar") ,
    path('Pasante/Detalle/<pk>', practica_views.PasanteDetailView.as_view(), name="pasante_detalle") ,
    #--Carrera
    path('Carrera', practica_views.CarreraListView.as_view(), name="carrera_listar") ,
    path('Carrera/Crear', practica_views.CarreraCreateView.as_view(), name="carrera_crear") ,
    path('Carrera/Editar/<pk>', practica_views.CarreraUpdateView.as_view(), name="carrera_editar") ,
    path('Carrera/Eliminar/<pk>', practica_views.CarreraDeleteView.as_view(), name="carrera_eliminar") ,
    path('Carrera/Detalle/<pk>', practica_views.CarreraDetailView.as_view(), name="carrera_detalle") ,
    #--Universidad
    path('Universidad', practica_views.UniversidadListView.as_view(), name="universidad_listar") ,
    path('Universidad/Crear', practica_views.UniversidadCreateView.as_view(), name="universidad_crear") ,
    path('Universidad/Editar/<pk>', practica_views.UniversidadUpdateView.as_view(), name="universidad_editar") ,
    path('Universidad/Eliminar/<pk>', practica_views.UniversidadDeleteView.as_view(), name="universidad_eliminar") ,
    path('Universidad/Detalle/<pk>', practica_views.UniversidadDetailView.as_view(), name="universidad_detalle") ,
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)