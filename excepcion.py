class PesoExcedido(Exception):
    def __init__(self, message="Se ha excedido el Peso"):
        self.message = message
        super().__init__(self.message)

class SinCargas(Exception):
    def __init__(self, message="Sin cargas disponibles"):
        self.message = message
        super().__init__(self.message)
