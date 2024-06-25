from .nodos import NodoSimple, NodoDoble

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

    def agregar_inicio(self, dato):
        nuevo_nodo = NodoDoble(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

    def eliminar_ultimo(self):
        if self.esta_vacia():
            return None
        actual = self.cabeza
        if actual.siguiente is None:
            self.cabeza = None
            return actual.dato
        while actual.siguiente is not None:
            actual = actual.siguiente
        ultimo = actual
        ultimo.anterior.siguiente = None
        return ultimo.dato

    def recorrer(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.obtener_dato(), end=" <-> ")
            actual = actual.siguiente
        print("None")
