
from django.contrib import admin
from django.urls import path
from . import views
from co2_app import views as co2_views

# LUIS CAMBIA LAS VIEWS
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cargar-datos/',views.cargar_datos_view,name='Cargar_Datos'),
    path('',co2_views.index,name='index'),
]