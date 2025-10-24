class Vertice:
    def __init__(self, clave):
        self.__id = clave
        self.__conexiones = {}

    def agregarVecino(self, vecino, ponderacion = 0):
        self.__conexiones[vecino] = ponderacion

    def __str__(self)->str:
        # return str (self.__id) + ' conectada a: ' + str ([x.__id for x in self.__conectadoA])
        return str(self.__id)

    def obtenerConexiones(self):
        return self.__conexiones.keys()

    def obtenerId(self):
        return self.__id

    def obtenerPonderacion(self, vecino):
        return self.__conexiones[vecino]

    def asignarDistancia(self, distancia):   # para usar con 'prim'
        self._distancia = distancia

    def obtenerDistancia(self)->int:
        return self._distancia

    def asignarPredecesor(self, predecesor):   # para usar con 'prim'
        self._predecesor = predecesor

    def obtenerPredecesor(self):
        return self._predecesor

    def __lt__(self, otro)->bool:   # para usa en las 'infiltrar' de 'MonticuloBinario'
        return self._distancia < otro._distancia

class Grafo:
    def __init__(self):
        self.__vertices = {}

    def __len__(self):
        return len(self.__vertices)

    def agregarVertice(self, clave):
        nuevo = Vertice(clave)
        self.__vertices[clave] = nuevo
        return nuevo

    def obtenerVertice(self, clave):   # OJO: probar con excepciones
        if clave in self.__vertices:
            return self.__vertices[clave]
        else:
            return None

    def __contains__(self, clave):
        return clave in self.__vertices

    def agregarArista(self, desde, hasta, ponderacion = 0):   # OJO: se puede mejorar
        if desde not in self.__vertices:
            nv = self.agregarVertice(desde)
        if hasta not in self.__vertices:
            nv = self.agregarVertice(hasta)
        self.__vertices[desde].agregarVecino(self.__vertices[hasta],ponderacion)

    def obtenerVertices(self):
        """Devuelve una lista con las claves (aldeas)"""
        return self.__vertices.keys()

    def __iter__(self):
        return iter(self.__vertices.values())
    
if __name__ == '__main__':
    g = Grafo()
    for i in range(6):
        g.agregarVertice(i)
    print(g.obtenerVertices())