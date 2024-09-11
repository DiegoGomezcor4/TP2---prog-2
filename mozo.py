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