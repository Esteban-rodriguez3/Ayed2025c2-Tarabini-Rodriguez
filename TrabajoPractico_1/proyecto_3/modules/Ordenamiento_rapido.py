import random 

def ordenamientoRapido (unaLista):
    ordenamientoRapidoAuxiliar (unaLista, 0, len(unaLista)-1)

def ordenamientoRapidoAuxiliar (unaLista, primero, ultimo):
    if primero<ultimo:
         puntoDivision = particion(unaLista,primero,ultimo)
         ordenamientoRapidoAuxiliar(unaLista,primero,puntoDivision-1)
         ordenamientoRapidoAuxiliar(unaLista,puntoDivision+1,ultimo)

def particion (unaLista, primero, ultimo):
     valorPivote = unaLista[primero]
     marcaIzq = primero+1
     marcaDer = ultimo

     hecho = False
     while not hecho:
         
         while marcaIzq <= marcaDer and unaLista[marcaIzq] <= valorPivote:
           marcaIzq = marcaIzq + 1
         while marcaDer >= marcaIzq and unaLista[marcaDer] >= valorPivote:
           marcaDer = marcaDer -1

         if marcaDer < marcaIzq:
           hecho = True
         else:
           unaLista [marcaIzq], unaLista[marcaDer] = unaLista[marcaDer], unaLista [marcaIzq]
     unaLista[primero], unaLista[marcaDer] = unaLista[marcaDer], unaLista[primero]
     return marcaDer
     
if __name__ == "__main__": 
    unaLista = [random.randint(10000, 99999) for _ in range(500)]  
    print (unaLista)      
    ordenamientoRapido (unaLista)
    print (unaLista)