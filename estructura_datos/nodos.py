class NodoSimple:
    def __init__(self, dato):
        self.dato = dato
        self.derecha = None

    def obtener_dato(self):
        return self.dato

class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

    def obtener_dato(self):
        return self.dato


