def ordenamientoPorResiduos (unaLista):
    posiciones = [4,3,2,1,0]
    for p in posiciones:
        auxiliar = {i: [ ] for i in range (10)}
        for x in unaLista: 
            cadena = str (x)
            digito = int (cadena [p])
            auxiliar [digito].append(x)
        unaLista = []
        for i in range(10):
            unaLista.extend (auxiliar[i])

