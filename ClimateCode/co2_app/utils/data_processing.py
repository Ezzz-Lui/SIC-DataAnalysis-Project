import pandas as pd

def Cargar_Datos(file_path):
    try:
        df = pd.read_csv(file_path)
        
        return {
            'paises': df['pais'].unique().tolist(),
            'años_registrados': df['año'].unique().tolist(),
            'dataframe': df
        }
    except Exception as e:
        print(f"Error al cargar datos: {e}")
        return None

def analizar_tendencia_co2(df, pais):
    """
    Analizar la tendencia de emisiones de CO2 para un país específico
    
    Args:
        df (pandas.DataFrame): DataFrame de datos
        pais (str): Nombre del país a analizar
    
    Returns:
        dict: Información de tendencia de CO2
    """
    datos_pais = df[df['pais'] == pais].sort_values('año')
    
    return {
        'pais': pais,
        'variacion_co2_total': calcular_variacion_porcentual(datos_pais['co2_total']),
        'variacion_co2_habitante': calcular_variacion_porcentual(datos_pais['co2_habitante'])
    }

def calcular_variacion_porcentual(serie):
    """
    Calcular variación porcentual de una serie de datos
    
    Args:
        serie (pandas.Series): Serie de datos numéricos
    
    Returns:
        float: Porcentaje de variación
    """
    primera_observacion = serie.iloc[0]
    ultima_observacion = serie.iloc[-1]
    
    return round(((ultima_observacion - primera_observacion) / primera_observacion) * 100, 2)

