# Definición de la clase Pizza
class Pizza:
    def __init__(self, variedad: str):
        self.variedad = variedad

    def establecerVariedad(self, variedad: str):
        self.variedad = variedad

    def obtenerVariedad(self):
        return self.variedad

# Definición de la clase MaestroPizzero
class MaestroPizzero:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.pizzasPorCocinar = []
        self.pizzasPorEntregar = []

    def establecerNombre(self, nombre: str):
        self.nombre = nombre

    def tomarPedido(self, variedad: str) -> Pizza:
        if variedad:
            pizza = Pizza(variedad)
            self.pizzasPorCocinar.append(pizza)
            return pizza

    def cocinar(self):
        self.pizzasPorEntregar.extend(self.pizzasPorCocinar)
        self.pizzasPorCocinar = []

    def entregar(self) -> list:
        if len(self.pizzasPorEntregar) > 2:
            pizzas_a_entregar = self.pizzasPorEntregar[:2]
            self.pizzasPorEntregar = self.pizzasPorEntregar[2:]
        else:
            pizzas_a_entregar = self.pizzasPorEntregar
            self.pizzasPorEntregar = []
        return pizzas_a_entregar

    def obtenerNombre(self):
        return self.nombre

    def obtenerPizzasPorCocinar(self):
        return self.pizzasPorCocinar

    def obtenerPizzasPorEntregar(self):
        return self.pizzasPorEntregar

# Definición de la clase Mozo
class Mozo:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.pizzas = []

    def establecerNombre(self, nombre: str):
        self.nombre = nombre

    def tomarPizzas(self, pizzas: list):
        if len(pizzas) > 2:
            pizzas = pizzas[:2]
        self.pizzas.extend(pizzas)

    def servirPizzas(self):
        self.pizzas = []

    def obtenerNombre(self):
        return self.nombre

    def obtenerPizzas(self):
        return self.pizzas

    def obtenerEstadoLibre(self):
        return len(self.pizzas) <= 1

# Clase de prueba TesterPizzeria
class TesterPizzeria:
    def main(self):
        # Crear un MaestroPizzero
        maestroPizzero = MaestroPizzero('Giovanni')
        
        # Crear dos Mozos
        mozo1 = Mozo('Alfredo')
        mozo2 = Mozo('Carlos')
        
        # Realizar pedidos de pizzas
        maestroPizzero.tomarPedido('Margarita')
        maestroPizzero.tomarPedido('Pepperoni')
        
        # Cocinar las pizzas
        maestroPizzero.cocinar()
        
        # Entregar las pizzas
        entregadas = maestroPizzero.entregar()
        print(f"Pizzas entregadas: {[pizza.obtenerVariedad() for pizza in entregadas]}")
        
        # Tomar pizzas por los mozos
        mozo1.tomarPizzas(entregadas)
        
        # Servir pizzas por el mozo1
        mozo1.servirPizzas()
        print(f"Pizzas de mozo1 después de servir: {mozo1.obtenerPizzas()}")
        
        # Verificar estado libre
        print(f"Mozo1 está libre: {mozo1.obtenerEstadoLibre()}")
        print(f"Mozo2 está libre: {mozo2.obtenerEstadoLibre()}")

if __name__ == '__main__':
    testerPizzeria = TesterPizzeria()
    testerPizzeria.main()