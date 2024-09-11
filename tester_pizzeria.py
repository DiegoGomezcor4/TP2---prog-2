from maestro_pizzero import MaestroPizzero
from mozo import Mozo
from pizza import Pizza

class TesterPizzeria:
    def main(self):
        # Punto 5.a. Crear objetos de tipo MaestroPizzero, Mozo y Pizza.
        maestro = MaestroPizzero('Don Pipo') # Un único objeto de tipo MaestroPizzero
        mozo1 = Mozo('Alfredo') # Primer mozo
        mozo2 = Mozo('Carlos') # Segundo mozo
        
        # Punto 5.b. Enviar mensajes a MaestroPizzero: tomarPedido, cocinar y entregar