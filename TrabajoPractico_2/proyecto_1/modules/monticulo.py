class MonticuloBinario:
    def __init__(self):
            self.listaMonticulo = [0]
            self.tamanoActual = 0

    def infiltArriba(self,i): #infiltra un nuevo ítem hacia arriba en el árbol hasta donde sea necesario para mantener la propiedad de montículo
        while i // 2 > 0:
            if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:
                tmp = self.listaMonticulo[i // 2]
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                self.listaMonticulo[i] = tmp
            i = i // 2
        
    def insertar(self,k): #agregar un ítem a una lista es simplemente añadir el elemento al final de la lista
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)


    #infiltAbajo y hijoMin permiten infiltrar un nodo hacia abajo en el árbol 
    def infiltAbajo(self,i): #restaura el ítem raíz tomando el último ítem de la lista y moviéndolo a la posición de la raíz
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i)
            if self.listaMonticulo[i] > self.listaMonticulo[hm]:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm

    def hijoMin(self,i): #restaura la propiedad de orden de montículo empujando el nuevo nodo raíz hacia abajo del árbol hasta su posición correcta
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def eliminarMin(self): #elimino el minimo del monticulo
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)
        return valorSacado

    def construirMonticulo(self,unaLista):
        i = len(unaLista) // 2
        self.tamanoActual = len(unaLista)
        self.listaMonticulo = [0] + unaLista[:]
        while (i > 0):
            self.infiltAbajo(i)
            i = i - 1

if __name__=="__main__":
    monticulo1=MonticuloBinario()
    monticulo1.insertar(26)
    monticulo1.insertar(5)
    monticulo1.insertar(7)
    monticulo1.insertar(3)
    monticulo1.insertar(11)
    print(monticulo1.eliminarMin())
