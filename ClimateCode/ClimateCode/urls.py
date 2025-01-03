from django.contrib import admin
from django.urls import path
from . import views
from co2_app import views as co2_views
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', co2_views.index, name='index'),
    path('co2_app/', include('co2_app.urls')),
    path('cargar-datos/', co2_views.cargar_datos_view, name='Cargar_Datos'),
]
