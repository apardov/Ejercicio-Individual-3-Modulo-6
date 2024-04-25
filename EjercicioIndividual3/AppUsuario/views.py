from django.shortcuts import render
from .models import AppUsuarios


# Create your views here.

def obtenerUsuarios(request):
    usuarios = AppUsuarios.objects.all()
    return render(request, 'base.html', {'usuarios': usuarios})
