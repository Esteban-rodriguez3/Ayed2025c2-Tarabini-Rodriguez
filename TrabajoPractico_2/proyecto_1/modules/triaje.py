
import msvcrt
from modules.coladeprioridad import ColaDePrioridad
from modules import paciente as pac 
import datetime 

class SalaEmergencia:
    """SalaEmergencia: administra una cola de acuerdo a la prioridad y el orden de llegada"""
    def __init__(self):
        self.__cola = ColaDePrioridad()

    def ingresarPaciente(self, p_paciente:pac.Paciente=None):
        """ingresarPaciente: ingresa un nuevo paciente a la sala"""
        if p_paciente is None:
            # Pasamos la hora actual al crear el paciente
            p_paciente = pac.Paciente(llegada=datetime.datetime.now())
        self.__cola.agregar(p_paciente)

    def atenderPaciente(self) -> pac.Paciente:
        """atenderPaciente: un paciente es atendido; se lo quita de la cola"""
        return self.__cola.sacar()

    @property
    def pacientesEsperando(self) -> int:
        return len(self.__cola)

    def __str__(self):
        return str(self.__cola)


if __name__ == '__main__':
    print('* PRUEBA: inicio')

    print ('instrucciones:')
    print('- I : ingresa un paciente')
    print('- A : se atiende un paciente')
    print('- cualquier otra tecla sale de la prueba')
    print('---')

    salita = SalaEmergencia()
    continuar = True
    while continuar:
        tecla = msvcrt.getch()
        if tecla == b'I' or tecla == b'i':   # ingresa un paciente
            p = pac.Paciente(llegada=datetime.datetime.now())
            print('ingresa paciente:', str(p))
            salita.ingresarPaciente(p)
        elif tecla == b'A' or tecla == b'a':   # se atiende un paciente
            paciente_atendido = salita.atenderPaciente()
            if paciente_atendido:
                print('paciente atendido:', str(paciente_atendido))
            else:
                print('No hay pacientes para atender.')
        else:
            continuar = False
        print('pacientes esperando:', salita.pacientesEsperando)
        print('---')

    print('* PRUEBA: fin')