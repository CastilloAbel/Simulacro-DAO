from abc import ABC, abstractmethod


class Carga(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def __str__(self)->str:
        pass

    @abstractmethod
    def calcularPeso(self)->float:
        pass