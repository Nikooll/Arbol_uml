class Nodo:
    def __init__(self, dato):
        self.dato = dato

    def obtener_dato(self):
        return self.dato

    def establecer_dato(self, dato):
        self.dato = dato


class NodoSimple(Nodo):
    def __init__(self, dato):
        super().__init__(dato)
        self.izquierda = None
        self.derecha = None


class NodoDoble(Nodo):
    def __init__(self, dato):
        super().__init__(dato)
        self.siguiente = None
        self.anterior = None
