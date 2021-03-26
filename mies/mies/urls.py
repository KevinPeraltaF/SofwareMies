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
from django.urls import path
from usuario import views as usuario_views
from red import views as red_views
urlpatterns = [
    path('', usuario_views.login_view, name="login") ,
    path('admin/', admin.site.urls),
    #MENU PARA LOS USUARIOS
    path('Usuario', usuario_views.dashboardUsuario_view, name="dashboard") ,
    #MODULO DE ACCESO A REDES
    path('AccesoRed', red_views.AccesoRedListView.as_view(), name="accesoRed_listar") ,
    path('AccesoRed/Crear', red_views.AccesoRedCreateView.as_view(), name="accesoRed_crear") ,
    path('AccesoRed/Editar/<pk>', red_views.AccesoRedUpdateView.as_view(), name="accesoRed_editar") ,
    
]
