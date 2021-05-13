
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse_lazy
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


#404
from django.shortcuts import render
from django.template import RequestContext


class dashboard_view(LoginRequiredMixin,TemplateView):
    template_name = "usuario/dashboard.html"
  
        



@login_required
def logout_view(request):
    logout(request)
    success_url = reverse_lazy('login')










