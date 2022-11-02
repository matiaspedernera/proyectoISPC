
class Producto:
    def __init__(self,nom,descrip,precio,stock,cate) -> None:
        self.nombre=nom
        self.descripcion=descrip
        self.precio=precio
        self.stock=stock
        self.categoria=cate
    def getNombre(self):
        return (self.nombre)