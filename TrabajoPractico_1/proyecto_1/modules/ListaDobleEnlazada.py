class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.prev = None
        self.next = None


class ListaDobleEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self._longitud = 0

    def esta_vacia(self):
        return self._longitud == 0

    def agregar_al_inicio(self, item):
        nuevo = Nodo(item)
        if self.esta_vacia():
            self.primero = self.ultimo = nuevo
        else:
            nuevo.next = self.primero
            self.primero.prev = nuevo
            self.primero = nuevo
        self._longitud += 1

    def agregar_al_final(self, item):
        nuevo = Nodo(item)
        if self.esta_vacia():
            self.primero = self.ultimo = nuevo
        else:
            self.ultimo.next = nuevo
            nuevo.prev = self.ultimo
            self.ultimo = nuevo
        self._longitud += 1

    def insertar(self, item, posicion=None):
        if posicion is None:
            self.agregar_al_final(item)
            return

        if posicion < 0 or posicion > self._longitud:
            raise IndexError("Posición inválida")

        if posicion == 0:
            self.agregar_al_inicio(item)
        elif posicion == self._longitud:
            self.agregar_al_final(item)
        else:
            nuevo = Nodo(item)
            actual = self.primero
            for _ in range(posicion):
                actual = actual.next
            anterior = actual.prev
            anterior.next = nuevo
            nuevo.prev = anterior
            nuevo.next = actual
            actual.prev = nuevo
            self._longitud += 1

    def extraer(self, posicion=None):
        if self.esta_vacia():
            raise IndexError("Lista vacía")

        if posicion is None:
            posicion = self._longitud - 1

        if posicion < 0 or posicion >= self._longitud:
            raise IndexError("Posición inválida")

        if posicion == 0:
            dato = self.primero.dato
            self.primero = self.primero.next
            if self.primero:
                self.primero.prev = None
            else:
                self.ultimo = None
        elif posicion == self._longitud - 1:
            dato = self.ultimo.dato
            self.ultimo = self.ultimo.prev
            if self.ultimo:
                self.ultimo.next = None
            else:
                self.primero = None
        else:
            actual = self.primero
            for _ in range(posicion):
                actual = actual.next
            dato = actual.dato
            actual.prev.next = actual.next
            actual.next.prev = actual.prev

        self._longitud -= 1
        return dato