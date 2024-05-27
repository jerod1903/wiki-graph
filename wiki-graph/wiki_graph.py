from grafo import Grafo
from errores import *
import random
import heapq
from cola import Cola

"""Wiki-graph es un módulo que contiene funciones de grafos, que permitan hacer distintas operaciones 
    sobre un grafo que modela Internet, sin importar cuál es la red específica."""

LISTAR = "listar_operaciones"
OPERACIONES = ["camino", "mas_importantes", "lectura", "rango", "navegacion"]
CAMINO = OPERACIONES[0]
MASIMPORTANTES = OPERACIONES[1]
LEC2AM = OPERACIONES[2]
RANGO = OPERACIONES[3]
NAVEGACION = OPERACIONES[4]

def lecturaArchivos(args):
    ruta = args[1]
    with open(ruta,'r') as parsed:
        g = Grafo(dirigido=True)
        for linea in parsed:
            pagina = linea.strip("\n").split("\t")
            titulo = pagina[0]
            links = pagina[1:]
            g.agregar_vertice(titulo)
            for link in links:
                if not link in g:
                    g.agregar_vertice(link)
                g.agregar_arista(titulo, link)
    return g

def verificarParametros(entrada, operacion, parametros):
    if operacion == LISTAR:
        if not len(entrada) == 1:
            raise ErrorParametros
        return
    elif operacion in {MASIMPORTANTES, NAVEGACION}:
        if not len(parametros) == 1:
            raise ErrorParametros
        return
    elif operacion in {CAMINO, RANGO}:
        if not len(parametros) == 2:
            raise ErrorParametros
        return
    elif operacion == LEC2AM:
        if not len(parametros) >= 2:
            raise ErrorParametros
        return
    raise(ErrorComando)

def procesarEntrada(entrada):
    entrada = entrada.split()
    if len(entrada) == 0:
        raise ErrorParametros
    operacion = entrada[0]
    parametros = []
    if len(entrada) > 1:
        parametros = " ".join(entrada[1:]).split(",")
    return entrada, operacion, parametros

def procesarOperacion(grafo, pagerank, operacion, parametros):
    if operacion == LISTAR:
        listarOperaciones(OPERACIONES)
    elif len(parametros) == 1:
        if operacion == MASIMPORTANTES:
            pagerank += MasImportantes(grafo, pagerank, parametros)
        elif operacion == NAVEGACION:
            Navegacion(grafo, parametros)
    elif len(parametros) >= 2:
        if operacion == CAMINO:
            CaminoMasCorto(grafo, parametros)
        elif operacion == RANGO:
            enRangoN(grafo, parametros)
        elif operacion == LEC2AM:
            Lectura2AM(grafo, parametros)

# Listar operaciones

def listarOperaciones(operaciones):
    for operacion in operaciones:
        print(operacion)
    return

# Camino más corto (★)

def CaminoMasCorto(grafo, parametros):
    origen, destino = parametros[0], parametros[1]
    if not origen in grafo or not destino in grafo:
        raise PaginaInexistente
    camino = camino_minimo_bfs(grafo, origen, destino)
    if len(camino) > 0:
        print(" -> ".join(camino))
        print("Costo: {}".format(len(camino)-1))
        return
    print("No se encontro recorrido")
    return

def camino_minimo_bfs(grafo, origen, destino):
    visitados = set()
    padre = {}
    dist = {}
    for v in grafo:
        dist[v] = float('inf')
    q = Cola()
    padre[origen] = None
    dist[origen] = 0
    q.encolar(origen)
    while not q.esta_vacia():
        v = q.desencolar()
        visitados.add(v)
        for w in grafo.adyacentes(v):
            if dist[v] + 1 < dist[w]:
                padre[w] = v
                dist[w] = dist[v] + 1
                if w == destino:
                    return reconstruir_camino(padre, origen, destino)
            q.encolar(w)
    return []

def reconstruir_camino(padre, origen, destino):
    camino = []
    v = destino
    while v != origen:
        camino.append(v)
        v = padre[v]
    camino.append(v)
    return camino[::-1]

# Artículos más importantes (★★★)

def MasImportantes(grafo, pagerank, parametros):
    n = int(parametros[0])
    if n <= 0:
        raise ErrorNum
    if len(pagerank) > 0:
        pr = pagerank
        topN(n, pr)
        return []
    else:
        pr = pageRank(grafo)
        topN(n, pr)
        return pr
    
def topN(n, pagerank):
    topN = heapq.nlargest(int(n), pagerank, key=lambda x: x[1])
    res = [p for p,_ in topN]
    print(", ".join(res))
    return

D = 0.85 # Coeficiente de amortiguación (https://en.wikipedia.org/wiki/PageRank)
PR_CONV = 25

def pageRank(grafo):
    pagerank = {}   
    init = (1-D)/len(grafo)
    for v in grafo:
        pagerank[v] = init
    links_salida = {}
    links_entrada = inbound(grafo)
    for i in range(PR_CONV):
        nueva_iter = {}
        auxPageRank(grafo, pagerank, nueva_iter, links_salida, links_entrada)
        pagerank = nueva_iter
    return nueva_iter.items()

def auxPageRank(grafo, last, pagerank, links_salida, links_entrada):
    for p in grafo:
        pagerank[p] = (1-D)/len(grafo)
        for l in links_entrada[p]:
            if l not in links_salida:
                links_salida[l] = len(grafo.adyacentes(l))
            pagerank[p] += D*(last[l]/links_salida[l])
        
def inbound(grafo):
    inbound = {}
    for v in grafo:
        for w in grafo.adyacentes(v):
            inbound[w] = inbound.get(w, []) + [v]
    return inbound

# Lectura a las 2 a.m. (★★)

def Lectura2AM(grafo, parametros):
    paginas = parametros
    for pagina in paginas:
        if pagina not in grafo:
            raise PaginaInexistente
    orden_lectura = ordenLectura(grafo, paginas)
    if orden_lectura is not None:
        print(", ".join(orden_lectura))
        return
    print("No existe forma de leer las paginas en orden")

def ordenLectura(grafo, paginas):
    orden = []
    grafoAux = Grafo(True, paginas)
    for pagina in paginas:
        for link in grafo.adyacentes(pagina):
            if link in grafoAux:
                grafoAux.agregar_arista(link, pagina)
    gr_ent = grados_entrada(grafoAux)
    pilaAux = [] # Python nos deja simular el comportamiento de una pila con un arreglo
    for pagina in grafoAux:
        if gr_ent[pagina] == 0:
            pilaAux.append(pagina)
    while not len(pilaAux) == 0:
        p = pilaAux.pop()
        orden.append(p)
        for l in grafoAux.adyacentes(p):
            gr_ent[l] -= 1
            if gr_ent[l] == 0:
                pilaAux.append(l)
    if len(orden) == len(paginas) and len(orden) != 2:
        return orden
    return None

def grados_entrada(grafo):
    gr_ent = {}
    for v in grafo:
        gr_ent[v] = gr_ent.get(v, 0)
        for w in grafo.adyacentes(v):
            gr_ent[w] = gr_ent.get(w, 0) + 1
    return gr_ent

# Todos en Rango (★)

def enRangoN(grafo, parametros):
    pagina, n = parametros[0], parametros[1]
    if not pagina in grafo:
        raise PaginaInexistente
    if not n.isdigit() or int(n) <= 0:
        raise ErrorNum
    rango = distancia_n_bfs(grafo, pagina, int(n))
    print(rango)
    return

def distancia_n_bfs(grafo, origen, n):
    q = Cola()
    q.encolar(origen)
    distancia = {}
    distancia[origen] = 0
    contador = 0
    while not q.esta_vacia():
        v = q.desencolar()
        for w in grafo.adyacentes(v):
            if not w in distancia:
                distancia[w] = distancia[v] + 1
                q.encolar(w)
                if distancia[w] == n:
                    contador +=1
                if distancia[w] > n:
                    return contador
    return contador

# Navegacion por primer link (★)

def Navegacion(grafo, parametros):
    origen = parametros[0]
    if not origen in grafo:
        raise PaginaInexistente
    print(" -> ".join(navegacionPor1Link(grafo, origen)))
    return

LIMITE = 20

def navegacionPor1Link(grafo, origen):
    resultado = [origen]
    v = origen
    i = 0
    adj = grafo.adyacentes(v)
    while len(adj) != 0 and i < LIMITE:
        v = adj[0]
        resultado.append(v)
        adj = grafo.adyacentes(v)
        i+=1
    return resultado