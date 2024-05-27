import random

"""Módulo conteniendo la clase Grafo, junto a la subclase GrafoPesado,
    ambas implementaciones del TDA Grafo."""

""" 
Parámetros
    ----------
    dirigido : bool, opcional, default: False
        Determina si el grafo es dirigido o no dirigido.

    vertices_iniciales: list, opcional, default: None
        La lista inicial de vértices a inicializar en el grafo.

    Atributos
    ----------
    dirigido : bool
        Indica si el grafo es dirigido o no dirigido.

    vertices : dict{dict}
        Cada clave de vertices representa un vértice, con las claves de su diccionario valor representando sus adyacentes.
        En caso de ser una instancia de GrafoPesado, cada clave adyacente tiene como valor asociado el peso de esa conexión
        (0 por defecto en una instancia de Grafo)

    Primitivas
    -----
    Grafo:
        
    Agrega un vértice al grafo
        agregar_vertice(v)

    Elimina un vértice del grafo
        borrar_vertice(v)

    Recibe un par de vertices y agrega una arista entre estos
    (unidireccional o bidireccional dependiendo de si es dirigido o no)
        agregar_arista(v, w)

    Recibe un par de vertices y elimina la arista que los une en caso de que exista.
        borrar_arista(v, w)

    Recibe un vertice v y devuelve la lista de vertices adyacentes al mismo.
        adyacentes(v) --> list

    Devuelve una lista con todos los vertices del grafo.  
        obtener_vertices() --> list

    Recibe un par de vertices y devuelve True si existe una arista entre ellos o False en caso contrario.
        estan_unidos(v, w) --> bool

    Devuelve un vertice al azar.
        vertice_aleatorio() --> v

    Devuelve la cantidad de vertices en el grafo.
        cantidad_vertices() --> int

    GrafoPesado(Grafo):

    Recibe un par de vertices y un peso y agrega una arista entre estos con dicho peso asignado
    (unidireccional o bidireccional dependiendo de si es dirigido o no)
        agregar_arista(v, w, peso)

    Devuelve el peso asociado a la arista que une al par de vertices (v, w)
    (En caso de que esta exista)
        ver_peso(v, w)

    Implementa
    ----------
    __len__
        Llamar a ''len(grafo)'' (''grafo'' es un instancia de ''Grafo/GrafoPesado'')
        Devuelve la cantidad de vértices en el grafo.

    __contains__
        Para ''grafo'' una instancia de ''Grafo/GrafoPesado'' y ''x'' un objecto no mutable,
        ''x in grafo'' devuelve ''True'' si ''x'' es un vértice en ''grafo''.

    __iter__
        Para ''grafo'' una instancia de ''Grafo/GrafoPesado'', ''for v in grafo'' llama internamente 
        al método __iter__, el cual devuelve un iterador para recorrer todos los vértices del grafo.

    __repr__
        Para ''grafo'' una instancia de ''Grafo/GrafoPesado'', devuelve la representación del grafo en formato string
        apuntando con una flecha con punta -> o sin -- desde cada vértice a sus adyacentes en caso de ser dirigido
        o no dirigido respectivamente.

    """

class Grafo:

    def __init__(self, dirigido=False, vertices_iniciales=[]):
        self.dirigido = dirigido
        self.vertices = {}
        if vertices_iniciales:
            for v in vertices_iniciales:
                self.vertices[v] = {}
        return
            
    def agregar_vertice(self, x):
        self.vertices[x] = {}

    def borrar_vertice(self, x):
        if x in self.vertices:
            self.vertices.pop(x)
            for v in self.vertices.keys():
                if x in self.vertices[v]:
                    self.vertices[v].pop(x)
        else:
            print("No existe el vertice especificado")
            return
        
    def agregar_arista(self, v, w):
        if v in self and w in self:
            self.vertices[v][w] = None
            if not self.dirigido:
                self.vertices[w][v] = None
        else:
            print("No existen los vertices especificados")
            return

    def borrar_arista(self, v, w):
        if v in self.vertices:
            if w in self.vertices[v]:
                self.vertices[v].pop(w)
            else:
                print("La arista especificada no existe")
                return
            if not self.dirigido:
                self.vertices[w].pop(v)
        else:
            print("La arista especificada no existe")
            return

    def adyacentes(self, v):
        if v in self:
            return list(self.vertices[v].keys())
        return []
        
    def obtener_vertices(self):
        return list(self.vertices.keys())

    def estan_unidos(self, v, w):
        return v in self.vertices and w in self.vertices[v]

    def vertice_aleatorio(self):
        if len(self.vertices) != 0:
            return random.choice(list(self.vertices.keys()))
        return None
    
    def cantidad_vertices(self):
        return len(self.vertices)
    
    def __iter__(self):
        return iter(self.vertices.keys())

    def __len__(self):
        return len(self.vertices)

    def __contains__(self, x):
        return x in self.vertices
    
    def __repr__(self):
        repr = ""
        repr+="Vertice:\tAristas:\n\n"
        for v in self.vertices:
            adj = ""
            for w in self.vertices[v]:
                adj+="{}, ".format(w)
            flecha = "----------"
            if self.dirigido:
                flecha = "--------->"
            repr+="   {} {} {}\n".format(v, flecha, adj[:len(adj)-2])
        return repr

class GrafoPesado(Grafo):

    def agregar_arista(self, v, w, peso=0):
        if v in self and w in self:
            self.vertices[v][w] = peso
            if not self.dirigido:
                self.vertices[w][v] = peso
        else:
            print("No existen los vertices especificados")
            return
    
    def ver_peso(self, v, w):
        if w in self.vertices[v]:
            return self.vertices[v].get(w)
        else:
            print("La arista especificada no existe")

    def __repr__(self):
        repr = ""
        repr+="Vertice:\tAristas:\n\n"
        for v in self.vertices:
            adj = ""
            for w in self.vertices[v]:
                adj+="{}: {}, ".format(w, self.vertices[v].get(w))
            flecha = "----------"
            if self.dirigido:
                flecha = "--------->"
            repr+="   {} {} {}\n".format(v, flecha, adj[:len(adj)-2])
        return repr