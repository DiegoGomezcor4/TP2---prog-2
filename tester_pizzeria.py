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
        maestro.tomarPedido('Margarita') # Maestro toma pedido de pizza Margarita
        maestro.tomarPedido('Napolitana') # Maestro toma el pedido de pizza napolitana
        
        maestro.cocinar() # Cocinar las pizzas tomadas en los pedidos
        pizza_listas = maestro.entregar() # Entregar hasta 2 pizzas
        
        print(f'Pizzas listas para entregar por el maestro pizzero: {[pizza.obtenerVariedad() for pizza in pizza_listas]}')
        
        # Punto 5.c. Enviar mensajes a los mozos: tomarPizzas y servirPizzas.
        mozo1.servirPizzas() # Mozo 1 sirve las pizzas
        print(f'Mozo 1 ha servido las pizzas, estado libre: {mozo1.obtenerEstadoLibre()}')
        
        # Simulamos otro pedido
        maestro.tomarPedido('4 Quesos') # Nuevo pedido
        maestro.cocinar() # Cocinarlo
        pizza_listas = maestro.entregar() # Entregar hasta 2 pizzas
        
        print(f'Pizzas listas para entregar por el maestro pizzero: {[pizza.obtenerVariedad() for pizza in pizza_listas]}')
        
        mozo2.tomarPizzas(pizza_listas) # Mozo 2 tomas las pizzas
        print(f'Mozo 2 tiene las siguientes pizzas: {[pizza.obtenerVariedad() for pizza in mozo2.obtenerPizzas()]}')
        
        mozo2.servirPizzas() # Mozo 2 sirve las pizzas
        print(f'Mozo 2 ha servido las pizzas, estado libre : {mozo2.obtenerEstadoLibre()}')
        
# Comprobacion de ejecucion del programa

if __name__ == '__main__':
    testerPizzeria = TesterPizzeria()
    testerPizzeria.main()
    
"""
Salida Esperada:
Pizzas listas para entregar por el maestro pizzero: ['Margarita', 'Napolitana']
Mozo 1 tiene las siguientes pizzas: ['Margarita', 'Napolitana']
Mozo 1 ha servido las pizzas, estado libre : True
Pizzas listas para entregar por el maestro pizzero: ['4 Quesos']
Mozo 2 tiene las siguientes pizzas: ['4 Quesos']
Mozo 2 ha servido las pizas, estado libre : True

"""