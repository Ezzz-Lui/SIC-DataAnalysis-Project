from django.shortcuts import render
from django.http import JsonResponse
from co2_app.utils.data_processing import Cargar_Datos
import pandas as pd

# Create your views here 
def index(request):
    # df = pd.read_csv('/utils/data/co2.csv')
    paises = ['Argentina', 'Bolivia', 'Brasil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Perú', 'Surinam', 'Uruguay', 'Venezuela']
    print(paises)  
    return render(request, 'index.html')

def cargar_datos_view(request):
    # if request.method == 'POST' and request.FILES.get('dataset'):
        # Guardar el dataframe en la base de datos
        paises = ['Argentina', 'Bolivia', 'Brasil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Perú', 'Surinam', 'Uruguay', 'Venezuela']
        print(paises)
        
        return render(request,'cargar_datos.html')

def cargar_datos(request):
    paises = ['Argentina', 'Bolivia', 'Brasil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Perú', 'Surinam', 'Uruguay', 'Venezuela']
    # df = pd.read_csv('ClimateCode/co2_app/utils/data/co2.csv')
    
    # paises = df['pais '].unique()  # Remove trailing space from 'pais'
    # años = df['año'].unique()
    # print(paises)  

    pais_seleccionado = request.POST.get('pais')  # Remove trailing space from 'pais'
    # anio_seleccionado = request.POST.get('año')  

    # Si se recibe un POST con datos seleccionados, filtramos los datos
    # if pais_seleccionado and anio_seleccionado:
    #     datos_filtrados = df[(df['pais'] == pais_seleccionado) & (df['año'] == int(anio_seleccionado))]
    # else:
    #     datos_filtrados = []
    print(paises)

    return render(request, 'cargar_datos.html', {
        'paises': paises,
        # 'años': años,
        'pais_seleccionado': pais_seleccionado,  # Pasar el país seleccionado
        # 'anio_seleccionado': anio_seleccionado,  # Pasar el año seleccionado
        # 'datos_filtrados': datos_filtrados,
    })