from maestro_pizzero import MaestroPizzero
from mozo import Mozo
from pizza import Pizza

class TesterPizzeriaEscenario2:
    def main(self):
        # Crear objetos de tipo MaestroPizzero y Mozo
        maestro = MaestroPizzero('Don Pipo')
        mozo1 = Mozo('Alfredo')
        mozo2 = Mozo('Carlos')
        
        # Intentar cocinar sin tomar pedidos (debe no hacer nada)
        maestro.cocinar()
        print(f'Pizzas por cocinar tras intento de cocinar sin pedidos: {maestro.obtenerPizzasPorCocinar()}')
        
        # Intentar entregar sin haber cocinado (debe no hacer nada)
        pizzas_entregadas = maestro.entregar()
        print(f'Pizzas entregadas sin haber cocinado: {pizzas_entregadas}')
        
        # Tomar más de 2 pizzas en un pedido y ver si los mozos pueden manejar más de 2
        maestro.tomarPedido('Margarita')
        maestro.tomarPedido('Napolitana')
        maestro.tomarPedido('Hawaiana')  # Tercer pedido
        maestro.cocinar()  # Cocinar todas las pizzas
        
        pizzas_listas = maestro.entregar()
        print(f'Pizzas listas para entregar por el maestro pizzero: {[pizza.obtenerVariedad() for pizza in pizzas_listas]}')
        
        mozo1.tomarPizzas(pizzas_listas)  # Mozo 1 toma pizzas
        print(f'Mozo 1 tiene las siguientes pizzas: {[pizza.obtenerVariedad() for pizza in mozo1.obtenerPizzas()]}')
        
        # Intentar que mozo1 tome más pizzas de las que puede manejar (máximo 2)
        maestro.tomarPedido('4 Quesos')
        maestro.tomarPedido('Fugazzeta')
        maestro.cocinar()
        pizzas_listas = maestro.entregar()
        
        mozo2.tomarPizzas(pizzas_listas)  # Mozo 2 toma pizzas
        print(f'Mozo 2 tiene las siguientes pizzas: {[pizza.obtenerVariedad() for pizza in mozo2.obtenerPizzas()]}')
        
        # Mozo intenta tomar más de dos pizzas (debe limitarse a 2)
        mozo2.tomarPizzas(pizzas_listas)  # Este intento no debe añadir más pizzas
        print(f'Mozo 2 tras intentar tomar más pizzas: {[pizza.obtenerVariedad() for pizza in mozo2.obtenerPizzas()]}')
        
        # Intentar que los mozos sirvan sin haber tomado pizzas
        mozo1.servirPizzas()
        print(f'Mozo 1 ha servido las pizzas, estado libre: {mozo1.obtenerEstadoLibre()}')

        mozo2.servirPizzas()
        print(f'Mozo 2 ha servido las pizzas, estado libre: {mozo2.obtenerEstadoLibre()}')

# Comprobación de ejecución del programa
if __name__ == '__main__':
    testerPizzeriaEscenario2 = TesterPizzeriaEscenario2()
    testerPizzeriaEscenario2.main()
