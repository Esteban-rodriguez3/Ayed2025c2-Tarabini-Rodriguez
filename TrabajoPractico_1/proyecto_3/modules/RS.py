def ordenamientoPorResiduos (unaLista):
    posiciones = [4,3,2,1,0]
    lista_ordenada = unaLista[:]
    for p in posiciones:
        auxiliar = {i: [ ] for i in range (10)}
        for x in lista_ordenada: 
            cadena = str (x)
            digito = int (cadena [p])
            auxiliar [digito].append(x)
        lista_ordenada = []
        for i in range(10):
            lista_ordenada.extend (auxiliar[i])
    return lista_ordenada 

if __name__ == "__main__":
    import random
    lista_prueba = [random.randint(10000, 99999) for _ in range(500)]
    print("Lista original:", lista_prueba)
    
    lista_ordenada = ordenamientoPorResiduos(lista_prueba)
    lista_ordenada_verificada = sorted(lista_prueba)

    if lista_ordenada == lista_ordenada_verificada:
        print("La lista ha sido ordenada correctamente.")
