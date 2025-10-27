from modules.monticulo import MonticuloBinario

class ColaDePrioridad: 
    def __init__(self):
        self.__monticulo = MonticuloBinario () 

    def agregar (self, elemento): #agregar un elemento segun su prioridad
        self.__monticulo.insertar (elemento)

    def sacar (self): #elimina y devuelve el elemento de mayor prioridad (el minimo)
        return self.__monticulo.eliminarMinimo ()

    def __len__ (self): #devuelve la cantidad de elementos en la cola 
        return len (self.__monticulo)

    def __str__(self):
        # Devuelve la representación en string del montículo
        return str(self.__monticulo)