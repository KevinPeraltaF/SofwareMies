from django.shortcuts import render

from red.models import AccesoRed

# Create your views here.

def index_view(request):
    #return render(request, 'login.html')
    return render(request, 'red/acceso_red.html')
    #return render(request, 'red/acceso_red.html')