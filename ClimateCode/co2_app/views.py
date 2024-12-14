from django.shortcuts import render
from django.http import JsonResponse
from co2_app.utils.data_processing import Cargar_Datos 
import pandas as pd
import base64
import matplotlib.pyplot as plt
import io
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
    # Obtener los datos del formulario
    pais = request.POST.get('pais')
    año = request.POST.get('año')
    metrica = request.POST.get('metrica')

    # Aquí debes obtener los datos reales según el país y el año seleccionados
    # Este es solo un ejemplo de cómo definir los datos
    # Suponiendo que tienes una función para obtener los datos
    datos = None  # Inicializa la variable de datos

    if pais and año and metrica:
        # Simulación de datos de ejemplo. Aquí es donde debes poner tu lógica para obtener los datos reales.
        datos = {
            'pais': pais,
            'año': año,
            'co2_total': 1200,  # Ejemplo de valor CO2 total
            'co2_habitante': 5.6,  # Ejemplo de valor CO2 por habitante
            'co2_producto_interno': 0.8  # Ejemplo de valor CO2 por Producto Interno
        }

        # Crear el gráfico de CO2 Total
        paises = ['País A', 'País B', 'País C']
        co2_totales = [1200, 1500, 1000]

        fig, ax = plt.subplots()
        ax.bar(paises, co2_totales, color='teal')
        ax.set_xlabel('Países')
        ax.set_ylabel('CO2 Total (en toneladas)')
        ax.set_title('Emisiones de CO2 por País')

        # Guardar el gráfico en un objeto de BytesIO para integrarlo en la plantilla HTML
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_data = base64.b64encode(buffer.read()).decode('utf-8')

        # Renderizar la plantilla con los datos y el gráfico
        return render(request, 'cargar_datos.html', {'image_data': image_data, 'datos': datos})

    else:
        # Si no se seleccionan los valores en el formulario
        return render(request, 'cargar_datos.html', {'error': 'Por favor, selecciona todos los campos.'})


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