# -*- coding: utf-8 -*-
"""
Sala de emergencias
"""

import time
import datetime
import modules.paciente as pac
import random

# Ya no usamos una lista, importamos la Sala de Emergencia
from modules.triaje import SalaEmergencia

n = 20  # cantidad de ciclos de simulación

sala_emergencia = SalaEmergencia() 

# Ciclo que gestiona la simulación
for i in range(n):
    # Fecha y hora de entrada de un paciente
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    # Se crea un paciente un paciente por segundo
    # Le pasamos la hora de llegada al constructor
    paciente = pac.Paciente(llegada=ahora)
    
    sala_emergencia.ingresarPaciente(paciente) # <-- USAMOS TU MÉTODO
    
    print(f"Ingresa paciente: {paciente}")


    # Atención de paciente en este ciclo: en el 50% de los casos
    if random.random() < 0.5:
        
        # Verificamos que haya pacientes antes de intentar atender
        if sala_emergencia.pacientesEsperando > 0:
            paciente_atendido = sala_emergencia.atenderPaciente() 
            
            print('*'*40)
            print('Se atiende el paciente:', paciente_atendido)
            print('*'*40)
        else:
            print("No hay pacientes en espera.")
    else:
        # se continúa atendiendo paciente de ciclo anterior
        print("... (Atendiendo paciente de ciclo anterior) ...")
        pass
    
    print()

    # Se muestran los pacientes restantes en la cola de espera
    print('Pacientes que faltan atenderse:', sala_emergencia.pacientesEsperando)
    
    # El loop 'for' ya no funciona igual, usamos el __str__ que definimos
    print(str(sala_emergencia))
    # NOTA: Esto imprimirá los pacientes en el orden del array interno
    # del montículo, NO en orden de prioridad. Es la forma más simple
    # de ver quiénes quedan sin destruir la cola.
    
    print()
    print('-*-'*15)
    
    time.sleep(1)