import sys

ruta = sys.argv[1]
with open(ruta,'r') as txt:
    for linea in txt:
        linea = linea.split("\t")
        if linea[0] == "Club Atlético River Plate":
            print(linea)

# Comunidades (★★)

def comunidades(grafo, parametros):
    pagina = parametros[0]
    if not pagina in grafo:
        raise PaginaInexistente
    comunidades = labelPropagation(grafo)
    for comunidad in comunidades.values():
        if pagina in comunidad:
            print(", ".join(list(comunidad)))
            print(len(list(comunidad)))
            return

LP_CONV = 25

def labelPropagation(grafo):
    links_entrada = inbound(grafo)
    label = {}
    i = 0
    for v in grafo:
        label[v] = v
    X = grafo.obtener_vertices()
    random.shuffle(X)
    convergence = False
    for _ in range(LP_CONV):
        for v in X:
            label[v] = max_freq(v, label, links_entrada)
    comunidades = {}
    for v, lbl in label.items():
        comunidades[lbl] = comunidades.get(lbl, []) + [v]
    return comunidades

def max_freq(v, label, links_entrada):
    vecinos = []
    for link in links_entrada[v]:
        vecinos.append(label[link])
    return max(set(vecinos), key=vecinos.count)

Coeficiente de Clustering (★★)

def clustering(grafo, parametros):
    if len(parametros) == 0:
        print("{:.3f}".format(clusteringNetworkAvg(grafo)))
        return
    pagina = parametros[0]
    if not pagina in grafo:
        raise PaginaInexistente
    print("{:.3f}".format(clusteringLocal(grafo, pagina)))
    return

def clusteringNetworkAvg(grafo):
    clustering = 0
    for v in grafo:
        clustering += clusteringLocal(grafo, v)
    return clustering/len(grafo)

def clusteringLocal(grafo, v):
    links = 0
    adj = set(grafo.adyacentes(v))
    if len(adj) < 2:
        return 0
    for u in adj:
        for w in grafo.adyacentes(u):
            if w in adj and w != u and w != v:
                links += 1
    k_posibles = len(adj)*(len(adj)-1)
    return links / k_posibles

class PaginaInexistente(ValueError):
    def Error():
        return "ERROR: La/s página/s solicitada/s no existe/n dentro de la red."

class ErrorNum(ValueError):
    def Error():
        return "ERROR: Por favor ingrese un número válido."

Ciclo de n artículos (★★★)

def cicloN(grafo, parametros):
    pagina, n = parametros[0], parametros[1]
    if not pagina in grafo:
        return
    if not n.isdigit() or int(n) <= 2:
        return
    ciclo = ciclo_n(grafo, pagina, int(n))
    if ciclo is not None:
        print(" -> ".join(ciclo))
    else:
        print("No se encontro recorrido")
    return

def ciclo_n(grafo, origen, n):
    padres = {}
    orden = {}
    padres[origen] = None
    orden[origen] = 0
    visitados = set()
    ciclo = dfs_ciclo(grafo, origen, n, padres, orden, visitados)
    return ciclo

def dfs_ciclo(grafo, v, n, padres, orden, visitados):
    for w in grafo.adyacentes(v):
        if not w in visitados:
            padres[w] = v
            orden[w] = orden[v] + 1
            if orden[w] == n:
                return
            visitados.add(v)
            ciclo = dfs_ciclo(grafo, w, n, padres, orden, visitados)
            if ciclo is not None:
                return ciclo
        else:
            if orden[w] == 0: # es el origen
                if orden[v] + 1 == n:
                    return reconstruir_ciclo(padres, w, v)
    return None

# Coeficiente de Clustering (★★)

def clustering(grafo, parametros):
    if len(parametros) == 0:
        print("{:.3f}".format(clusteringNetworkAvg(grafo)))
        return
    pagina = parametros[0]
    if not pagina in grafo:
        raise PaginaInexistente
    print("{:.3f}".format(clusteringLocal(grafo, pagina)))
    return

def clusteringNetworkAvg(grafo):
    clustering = 0
    for v in grafo:
        clustering += clusteringLocal(grafo, v)
    return clustering/len(grafo)

def clusteringLocal(grafo, v):
    links = 0
    adj = set(grafo.adyacentes(v))
    if len(adj) < 2:
        return 0
    for u in adj:
        for w in grafo.adyacentes(u):
            if w in adj and w != u and w != v:
                links += 1
    k_posibles = len(adj)*(len(adj)-1)
    return links / k_posibles