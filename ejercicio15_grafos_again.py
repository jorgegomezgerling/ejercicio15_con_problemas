# Se requiere implementar un grafo para almacenar las siete maravillas Arquitectonicas modernas y Naturales de mundo, para lo cual se deben tener en cuenta las siguientes actividades:
# a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de uno en las Naturales) y tipo (Natural o Arquitectonica); DONE! 
# b. cada una debe estar relacionada con las itras seis de su tipo, para lo que se debe almacenar la distancia que las separa; DONE! 
# c. hallar el árbol de expansion mínimo de cada tipo de las maravillas;
# d. determinar si existen países que dispongan de maravillas arquitecónicas y Naturales;
# e. determinar si algún país tiene más de una maravilla del mismo tipo;
# f. deberá utilizar un grafo no dirigido. 


from grafo import Grafo

mi_grafo = Grafo(dirigido=False)

class Maravilla:
    
    def __init__(self, nombre, pais, tipo):
        self.nombre = nombre
        self.pais = pais
        self.tipo = tipo
    
    def __str__(self):
        return f'{self.nombre} - {self.pais} - {self.tipo}'
    
mi_grafo.insert_vertice(Maravilla("Gran Muralla", 'China', 'Arquitectonica'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla("Machu Picchu", 'Peru', 'Arquitectonica'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla("Petra", 'Jordania', 'Arquitectonica'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla("Cataratas del Iguazú", ['Argentina', 'Brasil'],'Natural'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla("Monumento a la Bandera", 'Argentina', 'Arquitectonica'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla("Gran Cañón", 'Estados Unidos', 'Natural'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla("Taj Mahal", 'India', 'Arquitectonica'), criterio='nombre')


mi_grafo.insert_arist('Gran Muralla', 'Machu Picchu', 8, criterio_vertice='nombre')
mi_grafo.insert_arist('Gran Muralla', 'Petra', 5, criterio_vertice='nombre')
mi_grafo.insert_arist('Gran Muralla', 'Cataratas del Iguazú', 10, criterio_vertice='nombre')
mi_grafo.insert_arist('Gran Muralla', 'Monumento a la Bandera', 9, criterio_vertice='nombre')
mi_grafo.insert_arist('Gran Muralla', 'Gran Cañón', 7, criterio_vertice='nombre')
mi_grafo.insert_arist('Gran Muralla', 'Taj Mahal', 6, criterio_vertice='nombre')

mi_grafo.insert_arist('Machu Picchu', 'Petra', 3, criterio_vertice='nombre')
mi_grafo.insert_arist('Machu Picchu', 'Cataratas del Iguazú', 9, criterio_vertice='nombre')
mi_grafo.insert_arist('Machu Picchu', 'Monumento a la Bandera', 8, criterio_vertice='nombre')
mi_grafo.insert_arist('Machu Picchu', 'Gran Cañón', 6, criterio_vertice='nombre')
mi_grafo.insert_arist('Machu Picchu', 'Taj Mahal', 5, criterio_vertice='nombre')

mi_grafo.insert_arist('Petra', 'Cataratas del Iguazú', 4, criterio_vertice='nombre')
mi_grafo.insert_arist('Petra', 'Monumento a la Bandera', 3, criterio_vertice='nombre')
mi_grafo.insert_arist('Petra', 'Gran Cañón', 1, criterio_vertice='nombre')
mi_grafo.insert_arist('Petra', 'Taj Mahal', 2, criterio_vertice='nombre')

mi_grafo.insert_arist('Cataratas del Iguazú', 'Monumento a la Bandera', 7, criterio_vertice='nombre')
mi_grafo.insert_arist('Cataratas del Iguazú', 'Gran Cañón', 5, criterio_vertice='nombre')
mi_grafo.insert_arist('Cataratas del Iguazú', 'Taj Mahal', 8, criterio_vertice='nombre')

mi_grafo.insert_arist('Monumento a la Bandera', 'Gran Cañón', 2, criterio_vertice='nombre')
mi_grafo.insert_arist('Monumento a la Bandera', 'Taj Mahal', 4, criterio_vertice='nombre')

mi_grafo.insert_arist('Gran Cañón', 'Taj Mahal', 3, criterio_vertice='nombre')




# ori = 'Gran Muralla'
# des = 'Petra'
# origen = mi_grafo.search_vertice(ori, criterio='nombre')
# destino = mi_grafo.search_vertice(des, criterio='nombre')
# camino_mas_corto = None
# if(origen is not None and destino is not None):
#     if(mi_grafo.has_path(ori, des, criterio='nombre')):
#         camino_mas_corto = mi_grafo.dijkstra(ori, des)
#         fin = des
#         while camino_mas_corto.size() > 0:
#             value = camino_mas_corto.pop()
#             if fin == value[0]:
#                 print(value[0], value[1])
#                 fin = value[2]
# a = input()

bosque = mi_grafo.kruskal()
for arbol in bosque:
    print('arbol')
    for nodo in arbol.split(';'):
        print(nodo)

