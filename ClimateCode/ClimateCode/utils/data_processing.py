import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Funcion cargar los dataset a dataframe
def Cargar_Datos(ruta_archivo):
    try:
        #saber si el archivo es csv o exel
        if ruta_archivo.endswith('.csv'):
            df= pd.read_csv(ruta_archivo)
        elif ruta_archivo.endswith('.xlsx'):
            df= pd.read_excel(ruta_archivo)
        else:
            raise ValueError(f"este archivo {ruta_archivo} no es soportado.")
        return df
    except Exception as e:
        raise Exception(f"Error al cargar el archivo {e}")
    
#Fucion Normarlizar los datos
def Normalizar_Datos(df):
    #eliminar los valores null
    df= df.dropna()
    # aca normalizar columnas depende del dataset
    return df

#Funcion crear graficos 
"""MEJORAR"""
def Crear_Grafico(df,columna_x,columna_y,tipo='line'):
    plt.figure(figsize=(10,6))
    if tipo=='line':
        sns.lineplot(data=df, x=columna_x, y=columna_y)
    elif tipo=='bar':
        sns.lineplot(data=df, x=columna_x, y=columna_y)
    elif tipo=='scatter':
        sns.lineplot(data=df, x=columna_x, y=columna_y)
    else:
        raise ValueError(f"Tipo de grafico no soportado {tipo}")
    
    plt.title(f"Grafico de {columna_x} vs {columna_y}")
    plt.xlabel(columna_x)
    plt.ylabel(columna_y)
    plt.grid(True)
    plt.show()
    


#Funcion Combinar datasets
"""MEJORAR DESPUES PARA QUE COMBINE SOLO  EL MISMO TIPO DE DATASET
   Y EL MISMO TIPO DE VARIBLE
"""
#lista cambiarla por direccion de archivo
def Combinar_Datasets(lista_dataset):
    try:
        df_combined=pd.concat([pd.read_csv(dataset) for dataset in lista_dataset],ignore_index=True)
        return df_combined
    except Exception as e:
        raise Exception(f"Error al combinar dataset:{e}")
    
