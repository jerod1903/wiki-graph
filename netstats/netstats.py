#!/usr/bin/python3
from grafo import Grafo
import sys
from biblioteca import lecturaArchivos, procesarEntrada, verificarParametros, procesarOperacion
from errores import *

def main():
    wikigraph = lecturaArchivos(sys.argv)
    pagerank = []
    for linea in sys.stdin:
        try:
            entrada, operacion, parametros = procesarEntrada(linea)
            verificarParametros(entrada, operacion, parametros)
            procesarOperacion(wikigraph, pagerank, operacion, parametros)
        except ErrorParametros:
            print(ErrorParametros.Error())
            continue
        except ErrorComando:
            print(ErrorComando.Error())
            continue
        except ErrorNum:
            print(ErrorNum.Error())
            continue
        except PaginaInexistente:
            print(PaginaInexistente.Error())
            continue
        except RecursionError:
            print("ERROR: La operación solicitada no pudo ser completada.")


if __name__ == "__main__":
    main()