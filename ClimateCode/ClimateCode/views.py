from django.shortcuts import render
from django.http import JsonResponse
from .utils.data_processing import Cargar_Datos,Normalizar_Datos

"""MEJORAR LUIS!"""

# def cargar_datos_view(request):
#     if request.method == 'POST' and request.FILES.get('dataset'):
#         dataset = request.FILES['dataset']
#         df = cargar_datos(dataset.temporary_file_path())
#         df_limpio = limpiar_datos(df)
#         # Guardar el dataframe en la base de datos
#         return JsonResponse({'mensaje': 'Datos cargados y limpiados correctamente.'})
#     return render(request, 'cargar_datos.html')