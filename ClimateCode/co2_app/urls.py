from django.contrib import admin
from django.urls import path
from . import views

app_name = 'co2_app'

urlpatterns = [
    path('', views.index, name='index'),  # Página principal
    path('cargar-datos/', views.cargar_datos_view, name='cargar_datos'),  # Vista para cargar datos
    path('procesar-datos/', views.procesar_datos, name='procesar_datos'),  # Vista para procesar datos
]
