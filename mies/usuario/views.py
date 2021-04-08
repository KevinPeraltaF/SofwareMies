from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse_lazy
# Create your views here.
from django.contrib.auth.models import  Group

@login_required
def dashboard_view(request):
    print(request.user.user_permissions.all())
    return render(request,'usuario/dashboard.html')



@login_required
def logout_view(request):
    logout(request)
    # Redirect to a success page.
    success_url = reverse_lazy('login')