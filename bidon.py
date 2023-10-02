from carga import Carga
class Bidon(Carga):
    def __init__(self, contenido, capacidad, densidad):
        self.contenido = contenido
        self.capacidad = capacidad
        self.densidad = densidad

    def __str__(self)->str:
        return f"Contenido: {self.contenido}, Capacidad: {self.capacidad}, Densidad: {self.densidad}, Peso: {self.calcularPeso()}Kg"


    def calcularPeso(self)->float:
        return self.capacidad * self.densidad