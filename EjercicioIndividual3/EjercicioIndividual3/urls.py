from django.contrib import admin
from django.urls import path

from AppUsuario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.obtenerUsuarios, name='obtenerUsuarios'),
]
