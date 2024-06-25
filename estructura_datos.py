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


class ListaEnlazadaSimple:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def agregar_inicio(self, dato):
        nuevo_nodo = NodoSimple(dato)
        nuevo_nodo.derecha = self.cabeza
        self.cabeza = nuevo_nodo

    def eliminar_ultimo(self):
        if self.esta_vacia():
            return None
        actual = self.cabeza
        if actual.derecha is None:
            self.cabeza = None
            return actual.dato
        while actual.derecha.derecha is not None:
            actual = actual.derecha
        ultimo = actual.derecha
        actual.derecha = None
        return ultimo.dato

    def recorrer(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.obtener_dato(), end=" -> ")
            actual = actual.derecha
        print("None")


class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    # Similar methods for adding, removing, and traversing

    def agregar_inicio(self, dato):
        nuevo_nodo = NodoDoble(dato)
        nuevo_nodo.derecha = self.cabeza
        self.cabeza = nuevo_nodo

    def eliminar_ultimo(self):
        if self.esta_vacia():
            return None
        actual = self.cabeza
        if actual.derecha is None:
            self.cabeza = None
            return actual.dato
        while actual.derecha.derecha is not None:
            actual = actual.derecha
        ultimo = actual.derecha
        actual.derecha = None
        return ultimo.dato

    def recorrer(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.obtener_dato(), end=" -> ")
            actual = actual.derecha
        print("None")