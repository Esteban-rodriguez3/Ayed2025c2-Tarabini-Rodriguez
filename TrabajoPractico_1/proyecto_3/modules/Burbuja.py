import random

def ordenamientoBurbuja(unaLista):
    for pasada in range(len(unaLista)-1, 0, -1):
        for i in range(pasada):
            if unaLista[i] > unaLista[i+1]:
                unaLista[i],unaLista[i+1] = unaLista[i+1],unaLista[i]

def ordenamientoBurbujaCorta(unaLista):
    intercambios = True
    numero_pasada = len(unaLista)-1
    while numero_pasada > 0 and intercambios:
        intercambios = False
        for i in range(numero_pasada):
            if unaLista[i] > unaLista[i+1]:
                unaLista[i],unaLista[i+1] = unaLista[i+1],unaLista[i]
                intercambios = True
        numero_pasada = numero_pasada - 1

if __name__ == "__main__": 
    CANTIDAD = 500
    ensayo = [random.randint(10000,99999) for _ in range(CANTIDAD)]
    ensayo_ordenado = sorted(ensayo)
    ordenamientoBurbuja(ensayo)
        
    if ensayo == ensayo_ordenado:
        print("La lista ha sido ordenada correctamente.")