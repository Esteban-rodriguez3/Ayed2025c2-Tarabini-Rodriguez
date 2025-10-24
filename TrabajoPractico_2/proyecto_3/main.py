import re
import csv
from modules.grafo import Grafo
from modules.lib import prim

print('\n*** INICIO')

mapa = Grafo()

with open('aldeas.txt', encoding='utf-8') as archivo:
    datos = csv.reader(archivo)
    for dato in datos:
        # Primero, verificar que la línea tenga 3 campos
        if len(dato) == 3:
            try:
                # Limpiar los strings de origen y destino con REGEX
                origen = re.sub(r'\\s*', '', dato[0]).strip()
                destino = re.sub(r'\\s*', '', dato[1]).strip()
                
                # Convertir la distancia
                distancia = int(dato[2].strip())
                
                # AGREGAR ARISTA EN AMBAS DIRECCIONES (Grafo No Dirigido)
                mapa.agregarArista(origen, destino, distancia)
                mapa.agregarArista(destino, origen, distancia) 
            
            except ValueError:
                # Si falla la conversión a 'int'
                print(f"Omitiendo línea con distancia no válida: {dato}")
        else:
            # Si la línea no tiene 3 campos
            print(f"Omitiendo línea mal formada: {dato}")

print('+ datos cargados')

print('\n----------')
print('+ aldeas ordenadas alfabeticamente:')
lista = list(mapa.obtenerVertices())
lista.sort()
print(lista)

print('\n----------')
print('+ listado de aldeas con su predecesora')
prim(mapa, 'Peligros')
distancia_total = 0
for nombre in lista:
    aldea = mapa.obtenerVertice(nombre)
    distancia = aldea.obtenerDistancia()
    if distancia == 0:
        print(f'{nombre} es el punto de partida')
    else:
        print(f'{nombre} recibe de {aldea.obtenerPredecesor()}')
        distancia_total += distancia

print('\n----------')
print('+ listado de aldeas y a quién deben enviar réplicas (MST)')

# 1. Crear un diccionario para guardar los "hijos" de cada aldea en el MST
mst_hijos = {nombre: [] for nombre in lista}

# 2. Poblar el diccionario
for nombre in lista:
    aldea = mapa.obtenerVertice(nombre)
    predecesor = aldea.obtenerPredecesor()
    if predecesor is not None:
        # Añadir esta aldea como "hija" de su predecesor
        mst_hijos[str(predecesor)].append(nombre)

# 3. Imprimir los resultados
for nombre in lista:
    print(f'* {nombre} envía réplicas a:')
    if mst_hijos[nombre]:
        for hijo in mst_hijos[nombre]:
            print(f'\t{hijo}')
    else:
        print('\t(a nadie, es una hoja del árbol)')

print('\n----------')
print('+ la suma de todas las distanicas recorridas por las palomas es', distancia_total,)

print('\n*** FIN')