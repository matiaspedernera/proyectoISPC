from rest_framework import serializers
from cartadigital.models import Categoria, Producto

class CategoriaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Categoria
		fields = ('id', 'nombre', 'descripcion')


class ProductoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Producto
		fields = ('id','nombre','descripcion','precio', 'stock', 'imagen', 'activo','categoria')
