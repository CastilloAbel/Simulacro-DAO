from carga import Carga

class Packing(Carga):
    def __init__(self, contenido, peso_por_caja, cantidad, peso_estructura):
        self.contenido = contenido
        self.peso_por_caja = peso_por_caja
        self.cantidad = cantidad
        self.peso_estructura = peso_estructura
    

    def __str__(self)->str:
        return f"Contenido: {self.contenido}, Peso por caja: {self.peso_por_caja}, Cantidad de cajas: {self.cantidad}, Peso de la estructura: {self.peso_estructura}, Peso del Packing: {self.calcularPeso()}Kg"

    def calcularPeso(self)->float:
        return (self.cantidad * self.peso_por_caja) + self.peso_estructura

