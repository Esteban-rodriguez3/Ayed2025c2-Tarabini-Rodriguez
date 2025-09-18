# mazo.py

from modules.ListaDobleEnlazada import ListaDobleEnlazada  # Importa la clase ListaDobleEnlazada
from modules.carta import Carta

class DequeEmptyError(Exception):
    pass  # Define una excepción personalizada para cuando el mazo está vacío

class Mazo:
    def __init__(self):
        super().__init__()

    def poner_carta_arriba(self, p_carta):
        if not isinstance(p_carta, Carta):
            raise TypeError()
        self.agregar_al_inicio(p_carta)

    def sacar_carta_arriba(self, mostrar=False):
        if self.esta_vacia():
            raise DequeEmptyError()
        carta = self.extraer(0)
        if mostrar:
            carta.visible = True
        return carta

    def poner_carta_abajo(self, p_carta):
        if not isinstance(p_carta, Carta):
            raise TypeError()
        self.agregar_al_final(p_carta)