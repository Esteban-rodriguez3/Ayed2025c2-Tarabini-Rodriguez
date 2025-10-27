# -*- coding: utf-8 -*-

from random import randint, choices
import datetime 

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
# probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6] 

class Paciente:
    # Modificamos __init__ para aceptar la hora de llegada
    def __init__(self, llegada=None):
        n = len(nombres)
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]
        
        # Guardamos la hora de llegada como criterio de desempate
        if llegada is None:
            self.__llegada = datetime.datetime.now()
        else:
            self.__llegada = llegada

    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_riesgo(self):
        return self.__riesgo
    
    def get_descripcion_riesgo(self):
        return self.__descripcion
    
    def get_llegada(self):
        return self.__llegada

    def __lt__(self, other):
        """
        Define cómo se comparan dos pacientes.
        El Montículo Binario usará esto para ordenarlos.
        """
        if not isinstance(other, Paciente):
            return NotImplemented

        # Criterio 1: Nivel de Riesgo (el menor número es MÁS prioritario)
        if self.__riesgo != other.__riesgo:
            return self.__riesgo < other.__riesgo
        
        # Criterio 2: Hora de Llegada (la menor hora es MÁS prioritario)
        return self.__llegada < other.__llegada
    
    def __str__(self):
        cad = self.__nombre + ' '
        cad += self.__apellido + '\t -> '
        cad += str(self.__riesgo) + '-' + self.__descripcion
        # Añadimos la hora para verificar el desempate
        cad += ' (llegó: ' + self.__llegada.strftime('%H:%M:%S') + ')'
        return cad