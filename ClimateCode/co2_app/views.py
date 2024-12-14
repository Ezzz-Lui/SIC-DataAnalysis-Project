from django.shortcuts import render
from django.http import JsonResponse
from co2_app.utils.data_processing import Cargar_Datos
import pandas as pd
import os

# Página principal: muestra los datos iniciales cargados
def index(request):
    try:
        # Ruta al archivo CSV
        file_path = os.path.join(os.getcwd(), 'co2_app', 'utils', 'data', 'co2.csv')
        df = pd.read_csv(file_path)
        
        # Preparar datos para enviar al template
        context = {
            'paises': df['pais'].unique().tolist(),
            'años': sorted(df['año'].unique().tolist(), reverse=True),
            'metricas': [
                {'valor': 'co2_total', 'nombre': 'CO2 Total'},
                {'valor': 'co2_habitante', 'nombre': 'CO2 por Habitante'},
                {'valor': 'co2_producto_interno', 'nombre': 'CO2 por Producto Interno'}
            ]
        }
        
        return render(request, 'index.html', context)  # Renderizar el template principal
    except Exception as e:
        print(f"Error al cargar datos: {e}")
        return render(request, 'index.html', {'error': 'No se pudieron cargar los datos iniciales.'})


# Vista para procesar datos enviados por el usuario
def procesar_datos(request):
    if request.method == 'POST':
        pais = request.POST.get('pais')
        año = request.POST.get('año')
        metrica = request.POST.get('metrica')
        
        try:
            # Leer el archivo CSV
            file_path = os.path.join(os.getcwd(), 'co2_app', 'utils', 'data', 'co2.csv')
            df = pd.read_csv(file_path)
            
            # Filtrar datos
            datos_filtrados = df[(df['pais'] == pais) & (df['año'] == int(año))]
            
            if not datos_filtrados.empty:
                datos = {
                    'pais': pais,
                    'año': año,
                    'metrica': metrica,
                    'valor': datos_filtrados[metrica].values[0]
                }
                return render(request, 'cargar_datos.html', {'datos': datos})
            else:
                return render(request, 'cargar_datos.html', {'error': 'No se encontraron datos para los filtros seleccionados.'})
        except Exception as e:
            print(f"Error al procesar datos: {e}")
            return render(request, 'cargar_datos.html', {'error': 'Hubo un error procesando los datos.'})
    
    return render(request, 'cargar_datos.html')  # Renderizar con datos vacíos si no es POST


# Vista para cargar datos (simulación)
def cargar_datos_view(request):
    try:
        # Ruta del archivo CSV
        file_path = os.path.join(os.getcwd(), 'co2_app', 'utils', 'data', 'co2.csv')
        print(f"Intentando cargar: {file_path}")
        
        # Llama a la función personalizada para cargar datos
        resultado = Cargar_Datos(file_path)
        print(f"Resultado: {resultado}")
        
        if resultado is None:
            return render(request, 'error.html', {'mensaje': 'Error al cargar los datos.'})
        
        # Preparar contexto para el template
        context = {
            'paises': resultado['paises'],
            'años': resultado['años_registrados']
        }
        return render(request, 'cargar_datos.html', context)
    except Exception as e:
        print(f"Error en cargar_datos_view: {e}")
        return render(request, 'error.html', {'mensaje': 'Ocurrió un error inesperado.'})
