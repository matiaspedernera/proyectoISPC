from django.shortcuts import render
from django.http import HttpResponse 
from django.http import JsonResponse

from cartadigital.models import Usuario


# Create your views here.
def inicioApi(request):
    return HttpResponse("Bienvenido a la API de CartaDigtal")

def listaUsuarios(request):
    usuarios = list(Usuario.objects.values())
    return JsonResponse(usuarios, safe= False)








