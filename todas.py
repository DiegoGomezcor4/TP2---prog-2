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
        return self.obtenerPizzasPorEntregar
    
    from pizza import Pizza

class Mozo:
    # Constructores
    def __init__(self, nom: str):
        # Atributos de instancia
        self.nombre = nom
        self.pizzas = [] # Lista vacia de pizzas
    
    # Comandos
        # Comando para establecer el nombre del mozo
    def establecerNombre(self, nom: str):
        self.nombre = nom
    
        # Comando para que el mozo tome pizzas
    def tomarPizzas(self, pizzas: list):
        # El mozo puede tomar hasta un maximo de 2 pizzas
        if len(self.pizzas) < 2:
            self.pizzas.extend(pizzas[:2 - len(self.pizzas)])
    
        # Comando para que el mozo sirva las pizzas (limpia la lista de pizzas)
    def servirPizzas(self):
        self.pizzas.clear()
    
    # Consultas
        # Consulta para obtener el nombre del mozo
    def obtenerNombre(self):
        return self.nombre
    
        # Consulta para obtener la lista de pizzas que tiene el mozo
    def obtenerPizzas(self):
        return self.pizzas 
    
        # Consulta para saber si el mozo esta libre (tiene menos de 2 pizzas)
    def obtenerEstadoLibre(self):
        # Retorna True si la cantidad de pizzas es 0 o 1 , y False si es 1
        return len(self.pizzas) < 2
    
    
class Pizza:
    # Constructores
    def __init__(self, var: str):
        # Atributo de instancia
        self.variedad = var
    
    # Comandos
    def establecerVariedad(self, var: str):
        self.variedad = var
    
    # Consultas
    def obtenerVariedad(self):
        return self.variedad