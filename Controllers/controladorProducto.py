import sys;

sys.path.append('.\\Models')
from conexion import ConexionBD
from producto import Producto

prod = Producto("Hamburguesa","Big Mac",1800.50,1,1)

bd=ConexionBD()
#bd.insertarProducto(prod)
bd.borrarProducto(10)

bd.cerrarConexion()

