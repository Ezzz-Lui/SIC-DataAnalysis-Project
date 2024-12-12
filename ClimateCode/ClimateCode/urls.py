
from django.contrib import admin
from django.urls import path
from . import views

# LUIS CAMBIA LAS VIEWS
urlpatterns = [
    path('admin/', admin.site.urls),
    path('datar-datos/',views.Cargar_Datos_View,name='Cargar_Datos'),
    path('vizualizar-graficos/',views.vizualizar_graficos,name='visualizar_graficos')
    
]
