
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse_lazy
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
#modelos
from empleado.models import Empleado
from practica.models import Pasante
from capacitacion.models import CapacitacionCabecera
from atencion.models import Atencion
#404
from django.shortcuts import render
from django.template import RequestContext


class dashboard_view(LoginRequiredMixin,TemplateView):
    template_name = "usuario/dashboard.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        consulta={
            'totalEmpleado':Empleado.objects.filter(estado=1).count() ,
            'totalPasantes':Pasante.objects.filter(estado=0).count() ,
            'totalCapacitaciones':CapacitacionCabecera.objects.count() ,
            'totalAtenciones':Atencion.objects.filter(tipoDocumento=3).count() 

        }
        context['valores']= consulta
        return context
        



@login_required
def logout_view(request):
    logout(request)
    success_url = reverse_lazy('login')










