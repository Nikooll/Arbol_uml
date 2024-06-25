class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def buscarValor(self, dato):
        return self._buscarValor(self.raiz, dato)

    def _buscarValor(self, nodo, dato):
        if nodo is None:
            return None
        if dato == nodo.dato:
            return nodo
        elif dato < nodo.dato:
            return self._buscarValor(nodo.izquierda, dato)
        else:
            return self._buscarValor(nodo.derecha, dato)

    def recorridoInorden(self):
        self._recorridoInorden(self.raiz)

    def _recorridoInorden(self, nodo):
        if nodo is not None:
            self._recorridoInorden(nodo.izquierda)
            print(nodo.dato, end=" ")
            self._recorridoInorden(nodo.derecha)

    def recorridoPostorden(self):
        self._recorridoPostorden(self.raiz)

    def _recorridoPostorden(self, nodo):
        if nodo is not None:
            self._recorridoPostorden(nodo.izquierda)
            self._recorridoPostorden(nodo.derecha)
            print(nodo.dato, end=" ")

    def recorridoPreorden(self):
        self._recorridoPreorden(self.raiz)

    def _recorridoPreorden(self, nodo):
        if nodo is not None:
            print(nodo.dato, end=" ")
            self._recorridoPreorden(nodo.izquierda)
            self._recorridoPreorden(nodo.derecha)

    def agregarRecursivo(self, dato):
        self.raiz = self._agregarRecursivo(self.raiz, dato)

    def _agregarRecursivo(self, nodo, dato):
        if nodo is None:
            return NodoArbol(dato)
        if dato < nodo.dato:
            nodo.izquierda = self._agregarRecursivo(nodo.izquierda, dato)
        else:
            nodo.derecha = self._agregarRecursivo(nodo.derecha, dato)
        return nodo

    def eliminarRecursivo(self, dato):
        self.raiz = self._eliminarRecursivo(self.raiz, dato)

    def _eliminarRecursivo(self, nodo, dato):
        if nodo is None:
            return nodo
        if dato < nodo.dato:
            nodo.izquierda = self._eliminarRecursivo(nodo.izquierda, dato)
        elif dato > nodo.dato:
            nodo.derecha = self._eliminarRecursivo(nodo.derecha, dato)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            temp = self._minValueNode(nodo.derecha)
            nodo.dato = temp.dato
            nodo.derecha = self._eliminarRecursivo(nodo.derecha, temp.dato)
        return nodo

    def _minValueNode(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    def altura(self):
        return self._altura(self.raiz)

    def _altura(self, nodo):
        if nodo is None:
            return 0
        else:
            altura_izquierda = self._altura(nodo.izquierda)
            altura_derecha = self._altura(nodo.derecha)
            return 1 + max(altura_izquierda, altura_derecha)

    def balancear(self):
        pass  # Implementación del método de balanceo
