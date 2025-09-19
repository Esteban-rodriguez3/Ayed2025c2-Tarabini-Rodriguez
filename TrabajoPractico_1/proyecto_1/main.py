# Aplicación principal
import time, random, csv
from modules.ListaDobleEnlazada import ListaDobleEnlazada 

def medir_tiempos(funcion, N_valores):
    tiempos = []
    for N in N_valores:
        lista = ListaDobleEnlazada()
        for _ in range(N):
            lista.agregar_al_final(random.randrange(500))
        inicio = time.time()
        funcion(lista)
        fin = time.time()
        tiempos.append(fin - inicio)
    return tiempos

print('* INICIO')

N = list(range(10000, 100001, 10000))
tiempos_len = medir_tiempos(lambda l: len(l), N)
tiempos_copiar = medir_tiempos(lambda l: l.copiar(), N)
tiempos_invertir = medir_tiempos(lambda l: l.invertir(), N)

with open('data/datos.csv', 'w', newline='') as archivo:
    salida = csv.writer(archivo, dialect='excel')
    salida.writerow(N)
    salida.writerow(tiempos_len)
    salida.writerow(tiempos_copiar)
    salida.writerow(tiempos_invertir)

print('* FIN')