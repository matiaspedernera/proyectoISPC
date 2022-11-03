
import Models.conexion,Models.producto ;
from Models.conexion import ConexionBD
from Models.producto import Producto




prod = Producto("Pizza a la piedra","pizza de muzarella a la piedra",1800.50,10,1)

bd=ConexionBD()
bd.insertarProducto(prod)

bd.cerrarConexion()

