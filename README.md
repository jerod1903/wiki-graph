Wiki-graph es un módulo que contiene funciones de grafos, que permiten hacer distintas operaciones sobre un grafo que modela Internet, sin importar cuál es la red específica.
En el caso de prueba, se utiliza un recorrido BFS, por links, realizado desde la página de Wikipedia de Argentina (75000 páginas/nodos en el ejemplo grande, 5000 en el reducido).
Dentro del repositorio hay también una implementación del Tipo de Dato Abstracto Grafo.
De querer utilizar un modelo de Wikipedia más actualizado, se puede descargar el último dump desde acá:
[https://wikimedia.bringyour.com/](https://dumps.wikimedia.org/backup-index.html)
y seguir los pasos especificados en wiki_parser.py.
( El ejemplo corre sobre Python3)

Para inicializar el ejemplo se debe abrir la terminal y ejecutar lo siguiente:

  cd <directorio_descarga>

  cd wiki-graph

  python3 main.py <nombre_archivo_ejemplo> #75000 0 5000 nodos


Operaciones básicas:
- listar_operaciones: Muestra una lista de las operaciones disponibles.

- camino: Recibe una página de origen y destino y muestra el camino mínimo entre ellas.
  Ejemplo:
  
    camino Argentina,Barcelona
    Argentina -> Madres de Plaza de Mayo -> Barcelona
    Costo: 2
  
- mas_importantes: Muestra las n páginas más importantes de la red en base al algoritmo PageRank, desarrollado por Larry   Page y Sergey Brin, creadores de Google.
  Ejemplo:
  
    mas_importantes 3
    Argentina, Estados Unidos, Buenos Aires
  
- lectura: Recibe una lista de páginas y determina si es posible navegar a través de ellas en orden.
  
- rango: Muestra la cantidad de páginas que se encuentran a distancia n de la página especificada.
  Ejemplo:
  
    rango Buenos Aires,3
    37257
  
- navegacion: Recibe una página y devuelve un recorrido de navegación por primer link, desde dicha página a una página sin salida.
  Ejemplo:
    navegacion Messi
    Messi -> Lionel Messi -> Premio Golden Boy -> Selección de fútbol de Francia -> Guardameta (fútbol) -> Peter Shilton -> Nottingham Forest -> Nottingham Forest Football         Club -> Múnich -> Augsburgo -> Reino Unido -> Idioma córnico -> Cornualles -> Nomenclatura de las Unidades Territoriales Estadísticas -> Provincias de España -> Provincia      de España -> Pamplona -> ciudad

  
