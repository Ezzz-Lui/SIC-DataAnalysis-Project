from django.shortcuts import render
from django.http import JsonResponse
from co2_app.utils.data_processing import Cargar_Datos 
import pandas as pd
import os

def index(request):
    return render(request, 'index.html')  

def mostrar_datos(request):
    try:
        file_path = os.path.join(os.getcwd(), 'co2_app', 'utils', 'data', 'co2.csv')
        df = pd.read_csv(file_path)
        
        context = {
            'paises': df['pais'].unique().tolist(),
            'años': sorted(df['año'].unique().tolist(), reverse=True),
            'metricas': [
                {'valor': 'co2_total', 'nombre': 'CO2 Total'},
                {'valor': 'co2_habitante', 'nombre': 'CO2 por Habitante'},
                {'valor': 'co2_producto_interno', 'nombre': 'CO2 por Producto Interno'}
            ]
        }
        
        return render(request, 'cargar_datos.html', context)
    except Exception as e:
        print(f"Error: {e}")
        return render(request, 'cargar_datos.html', {})
    

def procesar_datos(request):
    if request.method == 'POST':
        pais = request.POST.get('pais')
        año = request.POST.get('año')
        metrica = request.POST.get('metrica')
        
        file_path = os.path.join(os.getcwd(), 'co2_app', 'utils', 'data', 'co2.csv')
        df = pd.read_csv(file_path)
        
        # Filtrar datos
        datos_filtrados = df[(df['pais'] == pais) & (df['año'] == int(año))]
        
        if not datos_filtrados.empty:
            datos = {
                'pais': pais,
                'año': año,
                'co2_total': datos_filtrados['co2_total'].values[0],
                'co2_habitante': datos_filtrados['co2_habitante'].values[0],
                'co2_producto_interno': datos_filtrados['co2_producto_interno'].values[0]
            }
            print(datos)
            return render(request, 'cargar_datos.html', {'datos': datos})
    
    return render(request, 'cargar_datos.html')    


# Obtén el directorio actual
print(os.getcwd())

# Carga el CSV (ajusta la ruta según tu estructura)
df = pd.read_csv('co2_app/utils/data/co2.csv')
print(df['pais'].unique())
print(df['año'].unique())
#CODIGO SOLO PARA PROBAR QUE SALE EN LA CONSOLA WASA
def cargar_datos_view(request):
    import os
    current_dir = os.getcwd()
    print(f"Directorio actual: {current_dir}")
    
    file_path = os.path.join(current_dir, 'co2_app', 'utils', 'data', 'co2.csv')
    print(f"Intentando cargar: {file_path}")
    
    resultado = Cargar_Datos(file_path)
    print(f"Resultado: {resultado}")
    
    if resultado is None:
        print("Error: No se pudieron cargar los datos")
        return render(request, 'error.html', {'mensaje': 'Error al cargar los datos'})
    
    context = {
        'paises': resultado['paises'],
        'años': resultado['años_registrados']
    }
    print(f"Context: {context}")
    
    return render(request, 'cargar_datos.html', context)