from django.shortcuts import render
from django.http import HttpResponse 
from rest_framework import generics
from cartadigital.models import Categoria, Producto
from cartadigital.serializers import CategoriaSerializer, ProductoSerializer

# Create your views here.
#def inicio(request):
#   return HttpResponse("Bienvenido a CartaDigtal App")
 

class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
