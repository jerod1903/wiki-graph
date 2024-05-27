class Nodo_heap(object):
    def __init__(self,dato):
        self.dato = dato
    
    def obtener_valor():
        return dato
    
    def __lt__(self, other):
        return self.dato>other.dato
    
    def __gt__(self, other):
        return self.dato<other.dato
    
    def __eq__(self, other):
        return self.dato==other.dato

    def __str__(self):
        return str(self.dato)
    
    def __repr__(self):
        return str(self.dato)