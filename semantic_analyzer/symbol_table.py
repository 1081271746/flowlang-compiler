class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def define(self, name):
        """
        Guarda una variable en la tabla de símbolos.
        """
        self.symbols[name] = {
            "type": "number"
        }

    def exists(self, name):
        """
        Verifica si una variable ya fue definida.
        """
        return name in self.symbols

    def get_all(self):
        """
        Retorna todas las variables guardadas.
        """
        return self.symbols