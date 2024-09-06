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
    
