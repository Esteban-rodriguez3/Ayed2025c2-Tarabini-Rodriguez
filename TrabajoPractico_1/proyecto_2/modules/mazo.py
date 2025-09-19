# mazo.py

from modules.ListaDobleEnlazada import ListaDobleEnlazada  # Importa la clase ListaDobleEnlazada
from modules.carta import Carta

class DequeEmptyError(Exception):
    pass  # Define una excepción personalizada para cuando el mazo está vacío

class Mazo:
    def __init__(self):
        self.cartas = ListaDobleEnlazada() # MODIFICAR PARA HACERLO ASI

    def poner_carta_arriba(self, p_carta):
        if not isinstance(p_carta, Carta):
            raise TypeError()
        self.cartas.agregar_al_inicio(p_carta)

    def sacar_carta_arriba(self, mostrar=False):
        if self.esta_vacia():
            raise DequeEmptyError()
        carta = self.cartas.extraer(0)
        if mostrar:
            carta.visible = True
        return carta

    def poner_carta_abajo(self, p_carta):
        if not isinstance(p_carta, Carta):
            raise TypeError()
        self.cartas.agregar_al_final(p_carta)
        
    def __len__(self):
       return self.cartas.tamanio
   
    def esta_vacia(self):
        return self.cartas.tamanio == 0
    
    def __str__(self):
        return str(self.cartas)