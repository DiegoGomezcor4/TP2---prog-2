from pizza import Pizza

class MaestroPizzero:
    # Constructores
    def __init__(self, nom: str):
        # Atributos de instancia
        self.nombre = nom
        self.pizzasPorCocinar = []
        self.pizzasPorEntregar = []

    # Comandos:
        # Comando para establecer el nombre del m pizzero
    def establecerNombre(self, nom: str):
        self.nombre = nom

        # Comando para tomar un pedido (crea una pizza y la agrega a pizzasPorCocinar)
    def tomarPedido(self, var: str):
        if var: # Requiere que el parametro var no este vacio
            pizza = Pizza(var)
            self.pizzasPorCocinar.append(pizza)
            return pizza  # Devuelve el objeto pizza

        # Comando para cocinar (mueve pizzad de pizzasPorCocinar a pizzasPorEntregar)
    def cocinar(self):
        if self.pizzasPorCocinar:
            self.pizzasPorEntregar.extend(self.pizzasPorCocinar)
            self.pizzasPorCocinar.clear()
    
        # Comando para entregar hasta 2 pizzas (remueve de pizzasPorEntregar)
    def entregar(self):
        a_entregar = self.pizzasPorEntregar[:2]
        self.pizzasPorEntregar = self.pizzasPorEntregar[2:]
        return a_entregar



    # Consultas
        # Consulta para obtener el nombre del maestro pizzero
    def obtenerNombre(self):
        return self.nombre
    
        # Consulta para obtener las pizzas pendientes por cocinar
    def obtenerPizzasPorCocinar(self):
        return self.pizzasPorCocinar
    
        # Consulta para obtener las pizzas listas para entregar
    def obtenerPizzasPorEntregar(self):
        return self.pizzasPorEntregar