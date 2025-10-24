class MonticuloBinario:
    """cola de prioridad"""
    def __init__ (self):
        self.__listaMonticulo = [None]
        self.__tamano = 0

    def __infiltrarArriba(self, i):
        padre = i // 2
        while padre > 0:
            if self.__listaMonticulo[i] < self.__listaMonticulo[padre]:
                self.__listaMonticulo[padre],self.__listaMonticulo[i] = self.__listaMonticulo[i],self.__listaMonticulo[padre]
            i = padre
            padre = i // 2

    def insertar(self, elemento):
        self.__listaMonticulo.append(elemento)
        self.__tamano += 1
        self.__infiltrarArriba(self.__tamano)

    def __hijoMenor(self, i):
        hijo_izquierdo = i * 2
        hijo_derecho = hijo_izquierdo + 1
        hijo_menor = hijo_izquierdo
        if hijo_derecho <= self.__tamano:
            if self.__listaMonticulo[hijo_derecho] < self.__listaMonticulo[hijo_izquierdo]:
                hijo_menor = hijo_derecho
        return hijo_menor

    def __infiltrarAbajo(self, i):
         while (i * 2) <= self.__tamano:
            hm = self.__hijoMenor(i)
            if self.__listaMonticulo[hm] < self.__listaMonticulo[i]:
                self.__listaMonticulo[i],self.__listaMonticulo[hm] = self.__listaMonticulo[hm],self.__listaMonticulo[i]
            i = hm

    def eliminarMinimo(self):
        elemento = self.__listaMonticulo[1]
        self.__listaMonticulo[1] = self.__listaMonticulo[self.__tamano]
        self.__tamano -= 1
        self.__listaMonticulo.pop()
        self.__infiltrarAbajo(1)
        return elemento

    def construirMonticulo(self, unaLista):
        for cosa in unaLista:
            self.insertar(cosa)

    def hayElementos(self):
        return self.__tamano != 0

    def reacomodarElemento(self, uno):
        ubicacion = self.__listaMonticulo.index(uno)
        self.__infiltrarArriba(ubicacion)

    def __str__(self)->str:
        lista = []
        for cosa in self.__listaMonticulo[1:]:
            lista.append(repr(cosa))
        return ' - '.join(lista)
    
    def __len__ (self)->int:
        return self.__tamano

    def __contains__(self, elemento):
        return elemento in self.__listaMonticulo

if __name__ == "__main__":
    print('* PRUEBA: inicio')
    monticulo = MonticuloBinario()
    monticulo.construirMonticulo([45,12,34,6,7,98,67,1])
    print(monticulo)
    print('* PRUEBA: fin')