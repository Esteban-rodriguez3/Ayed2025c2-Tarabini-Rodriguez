from modules.monticulo import MonticuloBinario


class ColaDePrioridad:
    def __init__(self):
        self.items = MonticuloBinario()

    def estaVacia(self):
        return self.items.tamanoActual == 0 

    def agregar(self, item):
        self.items.insertar(item)

    def avanzar(self):
        return self.items.eliminarMin()

    def tamano(self):
        return self.items.tamanoActual
     
