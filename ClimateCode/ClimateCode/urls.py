
from django.contrib import admin
from django.urls import path
from . import views
from co2_app import views as co2_views
from django.urls import include


# LUIS CAMBIA LAS VIEWS
urlpatterns = [
    path('admin/', admin.site.urls),   
    path('',co2_views.index,name='index'),
    path('cargar-datos/',views.cargar_datos_view,name='Cargar_Datos'),
    path('co2_app/', include('co2_app.urls')),
    

]


