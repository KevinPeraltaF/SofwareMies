from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def login_view(request):
    return render(request, 'usuario/login.html')

@login_required
def dashboardUsuario_view(request):
    return render(request,'usuario/dashboardUsuario.html')