from collections.abc import Iterable
from typing import Any
from django.db import models

# CLASE CATEGORIA
class Categoria(models.Model):
    #id_Categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=False)
    descripcion = models.CharField(max_length=50, blank=False)
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'categoria'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
# CLASE USUARIO
class Usuario(models.Model):
    #id_Usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=False)
    apellido = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=60, blank=False)
    password = models.CharField(max_length=20, blank=False)
    tipo_Usuario = models.CharField(max_length=20)
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'



# CLASE PEDIDO
class Pedido(models.Model): 
   # id_Pedido = models.AutoField(primary_key=True)
    fecha_Hora = models.DateTimeField(blank=False)
    estado = models.CharField(max_length=100, blank=False)
    tipo = models.CharField(max_length=100, blank=False)
    observacion = models.CharField (max_length=100)
    numeroMesa = models.IntegerField
    #id_Usuario = models.ForeignKey(
    usuario = models.ForeignKey(
        Usuario,
        #to_field="id_Usuario",
        related_name= "pedido_usuario",
        on_delete=models.CASCADE
    )
    def __unicode__(self):
        return self.fecha_Hora
    def __str__(self):
        return self.fecha_Hora
    class Meta:
        db_table = 'pedido'
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

# CLASE PRODUCTO
class Producto(models.Model):
    #id_Producto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=False)
    descripcion = models.TextField(max_length=1000, blank=False)
    precio = models.DecimalField(max_length=10, blank=False, decimal_places=2, max_digits=10)
    stock = models.IntegerField(default=0)
    imagen = models.CharField(max_length=60)
    # id_Categoria = models.ForeignKey(
    categoria = models.ForeignKey(
        Categoria, 
        #to_field="id_Categoria",
        related_name= "producto_categoria",
        on_delete=models.CASCADE
    )
    #numeroPedido = models.ManyToManyField(
    pedido = models.ManyToManyField(
        Pedido,
        related_name= "producto_pedido"
    )
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'



# CLASE CARTA 
class Carta(models.Model):
    #numeroCarta = models.IntegerField (primary_key=True)
    nombre = models.CharField(max_length=45)
    idioma = models.CharField(max_length=45)
    #codigoProducto = models.ManyToManyField(
    producto = models.ManyToManyField(
        Producto,
        related_name= "producto_carta"
    )
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'carta'
        verbose_name = 'Carta'
        verbose_name_plural = 'Cartas'


# CLASE CALIFICACIÓN
class Calificacion(models.Model):
    #id_Calificacion = models.AutoField (primary_key=True)
    calificacion = models.IntegerField
    comentario = models.CharField (max_length=45)
    # id_Producto = models.ForeignKey(
    producto = models.ForeignKey(
        Producto,
        #to_field="id_Producto",
        related_name= "calificacion_producto",
        on_delete=models.CASCADE
    )
    def __unicode__(self):
        return self.calificacion
    def __str__(self):
        return self.calificacion
    class Meta:
        db_table = 'calificacion'
        verbose_name = 'Calificacion'
        verbose_name_plural = 'Calificaciones'

# CLASE FACTURA
class Factura(models.Model):
    #id_Factura = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=False)
    cantidad = models.IntegerField(blank=False)
    descripcion = models.TextField (max_length=1000, blank=False)
    importe = models.IntegerField(blank=False)
    def __unicode__(self):
        return self.cantidad
    def __str__(self):
        return self.cantidad
    class Meta:
        db_table = 'factura'
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'

# CLASE VENTA
class Venta(models.Model):
    #id_Venta = models.AutoField(primary_key=True)
    descuento = models.IntegerField
    fecha_hora = models.DateTimeField
    importe = models.IntegerField
    #id_Pedido = models.ForeignKey(
    pedido = models.ForeignKey(
        Pedido,
        #to_field="id_Pedido",
        related_name= "venta_pedido",
        on_delete=models.CASCADE
    )
    #id_Factura = models.ForeignKey(
    factura = models.ForeignKey(
        Factura,
        #to_field="id_Factura",
        related_name= "venta_factura",
        on_delete=models.CASCADE
    )
    def __unicode__(self):
        return self.descuento
    def __str__(self):
        return self.descuento
    class Meta:
        db_table = 'venta'
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

# CLASE COMENTARIO
class Comentario(models.Model):
   #id_Comentario = models.AutoField(primary_key=True)
    comentario = models.CharField(max_length=50)
    fecha_hora = models.DateTimeField(blank=False)
    asunto = models.CharField (max_length=20, blank=False)
    #id_Usuario = models.ForeignKey(
    usuario = models.ForeignKey(
        Usuario,
        #to_field="id_Usuario",
        related_name= "comentario_usuario",
        on_delete=models.CASCADE
    )
    def __unicode__(self):
        return self.id_Comentario
    def __str__(self):
        return self.id_Comentario
    class Meta:
        db_table = 'comentario'
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

# CLASE MESA
class Mesa(models.Model):
    #id_Mesa = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=100, blank=False)
    ubicacion = models.TextField(max_length=1000, blank=False)
    cant_personas = models.IntegerField(blank=False)
    def __unicode__(self):
        return self.estado
    def __str__(self):
        return self.estado
    class Meta:
        db_table = 'mesa'
        verbose_name = 'Mesa'
        verbose_name_plural = 'Mesas'
 
#CLASE RESERVA
class Reserva(models.Model):
    #numeroReserva = models.AutoField(primary_key=True)
    fecha_hora = models.DateTimeField(blank=False)
    estado = models.CharField(max_length=100, blank=False)
    detalle = models.CharField (max_length=45, blank=False)
    #id_Usuario = models.ForeignKey(
    usuario = models.ForeignKey(
        Usuario,
        #to_field="id_Usuario",
        related_name= "reserva_usuario",
        on_delete=models.CASCADE
    )
    #id_Mesa = models.ForeignKey(
    mesa = models.ForeignKey(
        Mesa,
        #to_field="id_Mesa",
        related_name= "reserva_mesa",
        on_delete=models.CASCADE
    )
    def __unicode__(self):
        return self.fecha_hora
    def __str__(self):
        return self.fecha_hora
    class Meta:
        db_table = 'reserva'
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
 









