from maestro_pizzero import MaestroPizzero
from mozo import Mozo
from pizza import Pizza

class TesterPizzeria:
    def main(self):
        # Crear objetos de tipo MaestroPizzero, Mozo y Pizza.
        maestro = MaestroPizzero('Don Pipo')  # Un único objeto de tipo MaestroPizzero
        mozo1 = Mozo('Alfredo')  # Primer mozo
        mozo2 = Mozo('Carlos')  # Segundo mozo
        
        # El Maestro toma pedidos
        maestro.tomarPedido('Margarita')  # Maestro toma pedido de pizza Margarita
        maestro.tomarPedido('Napolitana')  # Maestro toma el pedido de pizza Napolitana
        
        # El Maestro cocina las pizzas tomadas en los pedidos
        maestro.cocinar()
        pizza_listas = maestro.entregar()  # Entregar hasta 2 pizzas
        
        print(f'Pizzas listas para entregar por el maestro pizzero: {[pizza.obtenerVariedad() for pizza in pizza_listas]}')
        
        # El mozo1 toma las pizzas y las sirve
        mozo1.tomarPizzas(pizza_listas)
        print(f'Mozo 1 tiene las siguientes pizzas: {[pizza.obtenerVariedad() for pizza in mozo1.obtenerPizzas()]}')
        mozo1.servirPizzas()  # Mozo 1 sirve las pizzas
        print(f'Mozo 1 ha servido las pizzas, estado libre: {mozo1.obtenerEstadoLibre()}')
        
        # Simulamos otro pedido
        maestro.tomarPedido('4 Quesos')  # Nuevo pedido
        maestro.cocinar()  # Cocinarlo
        pizza_listas = maestro.entregar()  # Entregar hasta 2 pizzas
        
        print(f'Pizzas listas para entregar por el maestro pizzero: {[pizza.obtenerVariedad() for pizza in pizza_listas]}')
        
        # El mozo2 toma las pizzas y las sirve
        mozo2.tomarPizzas(pizza_listas)
        print(f'Mozo 2 tiene las siguientes pizzas: {[pizza.obtenerVariedad() for pizza in mozo2.obtenerPizzas()]}')
        mozo2.servirPizzas()  # Mozo 2 sirve las pizzas
        print(f'Mozo 2 ha servido las pizzas, estado libre: {mozo2.obtenerEstadoLibre()}')

# Comprobación de ejecución del programa
if __name__ == '__main__':
    testerPizzeria = TesterPizzeria()
    testerPizzeria.main()

"""
Pizzas listas para entregar por el maestro pizzero: ['Margarita', 'Napolitana']
Mozo 1 tiene las siguientes pizzas: ['Margarita', 'Napolitana']
Mozo 1 ha servido las pizzas, estado libre: True
Pizzas listas para entregar por el maestro pizzero: ['4 Quesos']
Mozo 2 tiene las siguientes pizzas: ['4 Quesos']
Mozo 2 ha servido las pizzas, estado libre: True
"""