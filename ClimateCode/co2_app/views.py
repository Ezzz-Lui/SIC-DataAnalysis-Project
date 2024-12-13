from django.shortcuts import render
from django.http import JsonResponse
from co2_app.utils.data_processing import Cargar_Datos

# Create your views here 
def index(request):
    return render(request, 'index.html')

def cargar_datos_view(request):
    if request.method == 'POST' and request.FILES.get('dataset'):
        dataset = request.FILES['dataset']
        df = Cargar_Datos(dataset.temporary_file_path())
        # Guardar el dataframe en la base de datos
        return JsonResponse({'mensaje': 'Datos cargados y limpiados correctamente.'})
    return render(request, 'cargar_datos.html')