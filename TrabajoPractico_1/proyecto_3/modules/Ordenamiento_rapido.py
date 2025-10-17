import random 

def ordenamientoRapido (unaLista):
    ordenamientoRapidoAuxiliar (unaLista, 0, len(unaLista)-1)

def ordenamientoRapidoAuxiliar (unaLista, primero, ultimo):
    if primero < ultimo:
        
        medio = (primero + ultimo) // 2
        
        if unaLista[primero] > unaLista[ultimo]:
            unaLista[primero], unaLista[ultimo] = unaLista[ultimo], unaLista[primero]
        if unaLista[primero] > unaLista[medio]:
            unaLista[primero], unaLista[medio] = unaLista[medio], unaLista[primero]
        if unaLista[medio] > unaLista[ultimo]:
            unaLista[medio], unaLista[ultimo] = unaLista[ultimo], unaLista[medio]
        
        unaLista[primero], unaLista[medio] = unaLista[medio], unaLista[primero]

        puntoDivision = particion(unaLista, primero, ultimo)

        ordenamientoRapidoAuxiliar(unaLista, primero, puntoDivision - 1)
        ordenamientoRapidoAuxiliar(unaLista, puntoDivision + 1, ultimo)

def particion (unaLista, primero, ultimo):
    valorPivote = unaLista[primero]
    marcaIzq = primero + 1
    marcaDer = ultimo
    hecho = False
    while not hecho:
        while marcaIzq <= marcaDer and unaLista[marcaIzq] <= valorPivote:
            marcaIzq = marcaIzq + 1
        while unaLista[marcaDer] >= valorPivote and marcaDer >= marcaIzq:
            marcaDer = marcaDer - 1
        if marcaDer < marcaIzq:
            hecho = True
        else:
            unaLista[marcaIzq], unaLista[marcaDer] = unaLista[marcaDer], unaLista[marcaIzq]
    
    unaLista[primero], unaLista[marcaDer] = unaLista[marcaDer], unaLista[primero]
    return marcaDer
     
if __name__ == "__main__": 
    unaLista = [random.randint(10000, 99999) for _ in range(500)]  
    
    ordenamientoRapido(unaLista)
    lista_ordenada = sorted (unaLista)
    
    if unaLista == lista_ordenada:
        print("La lista ha sido ordenada correctamente.")