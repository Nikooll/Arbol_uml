class NodoGrafo:
    def __init__(self, dato):
        self.dato = dato
        self.adyacentes = []

class Grafo:
    def __init__(self):
        self.nodos = {}

    def agregarNodo(self, dato):
        if dato not in self.nodos:
            self.nodos[dato] = NodoGrafo(dato)

    def agregarArista(self, nodo1, nodo2):
        if nodo1 in self.nodos and nodo2 in self.nodos:
            self.nodos[nodo1].adyacentes.append(self.nodos[nodo2])
            self.nodos[nodo2].adyacentes.append(self.nodos[nodo1])

    def eliminarNodo(self, dato):
        if dato in self.nodos:
            del self.nodos[dato]
            for nodo in self.nodos.values():
                if self.nodos[dato] in nodo.adyacentes:
                    nodo.adyacentes.remove(self.nodos[dato])

    def eliminarArista(self, nodo1, nodo2):
        if nodo1 in self.nodos and nodo2 in self.nodos:
            self.nodos[nodo1].adyacentes.remove(self.nodos[nodo2])
            self.nodos[nodo2].adyacentes.remove(self.nodos[nodo1])
