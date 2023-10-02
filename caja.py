from carga import Carga
class Caja(Carga):
    def __init__(self, contenido, peso):
        self.contenido = contenido
        self.peso = peso

    def __str__(self)->str:
        return f"Contenido: {self.contenido}, Peso: {self.calcularPeso()}Kg"

    def calcularPeso(self)->float:
        return self.peso