import sys;

sys.path.append('.\\Models')
from conexion import ConexionBD
from producto import Producto

prod = Producto("Pizza","Muzzarella",900,1,1)

bd=ConexionBD()
bd.insertarProducto(prod)
#bd.borrarProducto()
#bd.actualizarProducto()

bd.cerrarConexion()

