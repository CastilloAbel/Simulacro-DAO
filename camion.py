from carga import Carga
from excepcion import *
class Camion:


    def __init__(self, patente, carga_maxima) -> None:
        self._patente = patente
        self._estado = "Disponible"
        self._carga_maxima = carga_maxima
        self._cargas = dict()
    

    def __str__(self) -> str:
        return f"Patente: {self.patente}, Estado: {self.estado}, Carga Maxima: {self.carga_maxima}, Cantidad de Cargas: {self.cantidad_cargas()}, Peso del camion: {self.peso_cargas()}"


    @property
    def patente(self)->str:
        return self._patente
    

    @property
    def estado(self)->str:
        return self._estado
    

    @property
    def carga_maxima(self)->float:
        return self._carga_maxima
    

    @property
    def cargas(self)->dict:
        return self._cargas


    @estado.setter
    def estado(self, estado):
        self._estado = estado


    def cantidad_cargas(self)->int:
        return len(list(self.cargas))


    def subir_cargas(self, carga:Carga):
        if self.peso_cargas() + carga.calcularPeso() >= self.carga_maxima:
            raise PesoExcedido()
        elif self.estado == "Disponible":
            self.cargas[carga.contenido] = carga
        else:
            print("Camion no disponible")


    def bajar_cargas(self, carga:Carga):
        if self.cantidad_cargas() > 0 and self.estado == "Disponible":
            self.cargas.pop(carga.contenido)
        else:
            raise SinCargas()
        

    def peso_cargas(self)->float:
       return sum(list(map(lambda x: x.calcularPeso(), self.cargas.values())))
    

    def a_reparacion(self):
        self.estado = "Reparando"


    def sale_reparado(self):
        self.estado = "Disponible"


    def en_viaje(self):
        self.estado = "Viajando" if self.listo_para_salir() else "Disponible"


    def de_regreso(self):
        self.estado = "Disponible"


    def listo_para_salir(self)->bool:
        return self.peso_cargas() / self.carga_maxima >= 0.75 and self.estado == "Disponible"


    def cargas_en_orden(self)->list:
        return list(map(lambda x: x.__str__(), self.cargas.values()))