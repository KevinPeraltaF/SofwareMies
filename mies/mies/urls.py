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

urlpatterns = [

    path('admin/', admin.site.urls),
    #MENU PARA LOS USUARIOS
    path('', usuario_views.dashboardUsuario_view, name="dashboard") ,
    #MODULO DE ACCESO A REDES
    path('AccesoRed', red_views.AccesoRedListView.as_view(), name="accesoRed_listar") ,
    path('AccesoRed/Crear', red_views.AccesoRedCreateView.as_view(), name="accesoRed_crear") ,
    path('AccesoRed/Editar/<pk>', red_views.AccesoRedUpdateView.as_view(), name="accesoRed_editar") ,
    path('AccesoRed/Eliminar/<pk>', red_views.AccesoRedDeleteView.as_view(), name="accesoRed_eliminar") ,
    path('AccesoRed/Detalle/<pk>', red_views.AccesoRedDetailView.as_view(), name="accesoRed_detalle") ,
    #MODULO DE EMPLEADO
    path('Empleado', empleado_views.EmpleadoListView.as_view(), name="empleado_listar") ,
    path('Empleado/Crear', empleado_views.EmpleadoCreateView.as_view(), name="empleado_crear") ,
    path('Empleado/Editar/<pk>', empleado_views.EmpleadoUpdateView.as_view(), name="empleado_editar") ,
    path('Empleado/Eliminar/<pk>', empleado_views.EmpleadoDeleteView.as_view(), name="empleado_eliminar") ,
    path('Empleado/Detalle/<pk>', empleado_views.EmpleadoDetailView.as_view(), name="empleado_detalle") ,
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

]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]