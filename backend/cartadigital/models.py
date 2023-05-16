from django.db import models

# Create your models here.
#clase categoria
class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=50)
    

    def __str__(self):
         
        return f" {self.nombre} - {self.descripcion}"

#clase producto
class Producto(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=50)
    precio = models.FloatField(default=0)
    stock = models.IntegerField(default=0)
    imagen = models.CharField(max_length=60)
    categoria = models.ForeignKey(
        Categoria,
        related_name="producto_categoria",
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f" {self.nombre} - {self.precio} - {self.stock} - {self.categoria}" 
