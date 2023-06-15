from rest_framework import serializers
from cartadigital.models import Categoria, Producto, Pedido
from authentication.models import CustomUser

class CategoriaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Categoria
		fields = ('id', 'nombre', 'descripcion')


class ProductoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Producto
		fields = ('id','nombre','descripcion','precio', 'stock', 'imagen', 'activo','categoria')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','email', 'username', 'first_name',
                  'last_name', 'password', 'is_staff')
	
class PedidoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pedido
		fields = ('id','estado','tipo', 'observacion', 'usuario', 'producto')
