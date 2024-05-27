class Pila:
    def __init__(self):
        self.tope = None

    def apilar(self, dato):
        nodo = Nodo(dato, self.tope)
        self.tope = nodo

    def desapilar(self):
        if self.esta_vacia():
            raise ValueError("pila vacía")
        dato = self.tope.dato
        self.tope = self.tope.prox
        return dato

    def ver_tope(self):
        if self.esta_vacia():
            raise ValueError("pila vacía")
        return self.tope.dato

    def esta_vacia(self):
        return self.tope is None

class Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox
