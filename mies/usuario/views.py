from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, 'usuario/login.html')


def dashboardUsuario_view(request):
    return render(request,'usuario/dashboardUsuario.html')