from django.contrib import admin
# co2_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cargar-datos/', views.cargar_datos_view, name='cargar_datos'),
    path('procesar-datos/', views.procesar_datos, name='procesar_datos'),  # Asegúrate de que esta ruta esté definida
]