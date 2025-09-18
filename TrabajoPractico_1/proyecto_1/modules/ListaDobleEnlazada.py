class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None


class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    def esta_vacia(self):
        return self.tamanio == 0

    def agregar_al_inicio(self, item):
        nuevo = Nodo(item)
        if self.esta_vacia():
            self.cabeza = self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
        self.tamanio += 1

    def agregar_al_final(self, item):
        nuevo = Nodo(item)
        if self.esta_vacia():
            self.cabeza = self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo
        self.tamanio += 1

    def insertar(self, item, posicion=None):
        if posicion is None:
            self.agregar_al_final(item)
            return

        if posicion < 0 or posicion > self.tamanio:
            raise IndexError("Posición inválida")

        if posicion == 0:
            self.agregar_al_inicio(item)
        elif posicion == self.tamanio:
            self.agregar_al_final(item)
        else:
            nuevo = Nodo(item)
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            anterior = actual.anterior
            anterior.siguiente = nuevo
            nuevo.anterior = anterior
            nuevo.siguiente = actual
            actual.anterior = nuevo
            self.tamanio += 1

    def extraer(self, posicion=None):
        if self.esta_vacia():
            raise IndexError("Lista vacía")

        if posicion is None or posicion == -1:
            posicion = self.tamanio - 1

        if posicion < -1 or posicion >= self.tamanio:
            raise IndexError("Posición inválida")

        if posicion == 0:
            dato = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            if self.cabeza:
                self.cabeza.anterior = None
            else:
                self.cola = None
            self.tamanio -= 1
        elif posicion == self.tamanio - 1:
            dato = self.cola.dato
            self.cola = self.cola.anterior
            if self.cola:
                self.cola.siguiente = None
            else:
                self.cabeza = None
            self.tamanio -= 1
        else:
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            dato = actual.dato
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior
            self.tamanio -= 1
        return dato

    def copiar (self):
        lista_aux = ListaDobleEnlazada ()
        actual = self.cabeza
        while actual is not None:
            lista_aux.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return lista_aux
    
    def invertir(self):
        actual = self.cabeza
        self.cabeza, self.cola = self.cola, self.cabeza
        while actual:
            actual.anterior, actual.siguiente = actual.siguiente, actual.anterior
            actual = actual.anterior 

    def concatenar(self, otra):
        if otra.esta_vacia():
            return
        if self.esta_vacia():
            self.cabeza = otra.cabeza
            self.cola = otra.cola
        else:
            self.cola.siguiente = otra.cabeza
            otra.cabeza.anterior = self.cola
            self.cola = otra.cola
        self.tamanio += len(otra)
    
    def __str__(self):
        # sirve para poder mostrar el contenido de una LDE por consola con la función print
        elementos = []
        actual = self.cabeza
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " <-> ".join(elementos)
    
    def __len__(self):
       return self.tamanio
    
    def __add__(self, otra):
        # devuelve una nueva lista: copia de self + copia de otra
        nueva = self.copiar()
        nueva.concatenar(otra)
        return nueva

    def __iter__(self):
        actual = self.cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente

    def __str__(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " <-> ".join(elementos)

#Ensayos
if __name__ == "__main__":
    print('*** ENSAYOS ***')
    print('* INICIO')
    lista = ListaDobleEnlazada()
    if lista.esta_vacia():
        print('lista sin elementos')
    lista.agregar_al_final('abc')
    lista.agregar_al_final('xyz')
    lista.agregar_al_final('rst')
    lista.agregar_al_final('00')
    lista.agregar_al_inicio('ini')
    lista.insertar('qqq',2)
    print('cantidad de elementos:', len(lista))
    print('elementos:', lista)
    print('extraer la cola:', lista.extraer())
    print('extraer la cabeza:', lista.extraer(0))
    print('cantidad de elementos:', len(lista))
    print('elementos:', lista)
    lista.invertir()
    print('lista invertida:', lista)
    print('extraer tercer elemento', lista.extraer(2))
    print('final', lista)
    otra_lista = ListaDobleEnlazada()
    otra_lista.agregar_al_final('chuchu')
    otra_lista.agregar_al_final('zucuzucu')
    otra_lista.agregar_al_final('pikipiki')
    print('otra lista:', otra_lista)
    print('listas sumadas:', lista+otra_lista)
    print('* FIN')