class NodoArbol:
    def __init__(self, clave, valor, izquierdo=None, derecho=None, padre=None):
        self.__clave = clave
        self.__cargaUtil = valor
        self.__hijoIzquierdo = izquierdo
        self.__hijoDerecho = derecho
        self.__padre = padre
        self.__factorEquilibrio = 0

    def tieneHijoIzquierdo(self):
        return self.__hijoIzquierdo is not None

    def tieneHijoDerecho(self):
        return self.__hijoDerecho is not None

    def esHijoIzquierdo(self):
        return self.__padre and self.__padre.__hijoIzquierdo == self

    def esHijoDerecho(self):
        return self.__padre and self.__padre.__hijoDerecho == self

    def esRaiz(self):
        return  self.__padre is None

    def esHoja(self):
        return not (self.__hijoDerecho or self.__hijoIzquierdo)

    def tieneAlgunHijo(self):
        return self.__hijoDerecho or self.__hijoIzquierdo

    def tieneAmbosHijos(self):
        return self.__hijoDerecho and self.__hijoIzquierdo
    
    def tieneUnSoloHijo(self):
        return (self.tieneHijoIzquierdo() or self.tieneHijoDerecho()) and not self.tieneAmbosHijos()
    
    def reemplazarDatoDeNodo(self, clave, valor, hizq, hder):
        self.__clave = clave
        self.__cargaUtil = valor
        self.__hijoIzquierdo = hizq
        self.__hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.__hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.__hijoDerecho.padre = self
        
    @property
    def clave(self):
        return self.__clave

    @clave.setter
    def clave(self,nueva_clave):
        self.__clave = nueva_clave

    @property
    def cargaUtil(self):
        return self.__cargaUtil

    @cargaUtil.setter
    def cargaUtil(self, nueva_carga):
        self.__cargaUtil = nueva_carga

    @property
    def hijoIzquierdo(self):
        return self.__hijoIzquierdo

    @hijoIzquierdo.setter
    def hijoIzquierdo(self, nodo):
        self.__hijoIzquierdo = nodo

    @property
    def hijoDerecho(self):
        return self.__hijoDerecho

    @hijoDerecho.setter
    def hijoDerecho(self, nodo):
        self.__hijoDerecho = nodo

    @property
    def padre(self):
        return self.__padre

    @padre.setter
    def padre(self, nodo):
        self.__padre = nodo
        
    @property
    def factorEquilibrio(self):
        return self.__factorEquilibrio

    @factorEquilibrio.setter
    def factorEquilibrio(self, valor):
        self.__factorEquilibrio = valor

    def encontrarSucesor(self):
        suc = None
        if self.tieneHijoDerecho():
            suc = self.hijoDerecho.encontrarMin()
        else:
            actual = self
            padre = actual.padre
            while padre is not None and actual == padre.hijoDerecho:
                actual = padre
                padre = actual.padre
            suc = padre
        return suc
    
    def encontrarMin(self):
        actual = self
        while actual.tieneHijoIzquierdo():
            actual = actual.hijoIzquierdo
        return actual    
    
    def __iter__(self): #El código para un iterador inorden de un árbol binario
        if self.tieneHijoIzquierdo():
           for elem in self.hijoIzquierdo:
                yield elem
        yield self.clave
        if self.tieneHijoDerecho():
            for elem in self.hijoDerecho:
                yield elem

class ArbolBinarioBusqueda_AVL:
    def __init__(self):
        self.raiz = None
        self.tamano = 0

    def longitud(self):
        return self.tamano

    def __len__(self):
        return self.tamano

    def __iter__(self):
        if self.raiz:
            return self.raiz.__iter__()
        else:
            return iter([])

    def agregar(self,clave,valor):
        if self.raiz:
            self._agregar(clave,valor,self.raiz)
        else:
            self.raiz = NodoArbol(clave,valor)
        self.tamano = self.tamano + 1

        if __name__ == "__main__":   
            print (self.raiz.cargaUtil) 
          
            if self.raiz.tieneHijoIzquierdo ():
               print (self.raiz.hijoIzquierdo.cargaUtil)
            else :
               print ("No tiene hijo izquierdo")
            if self.raiz.tieneHijoDerecho ():
               print (self.raiz.hijoDerecho.cargaUtil)
            else : 
               print ("No tiene hijo derecho")
            print (self.tamano)   

    def _agregar(self,clave,valor,nodoActual):
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                self._agregar(clave,valor,nodoActual.hijoIzquierdo)
            else:
                nodoActual.hijoIzquierdo = NodoArbol(clave,valor,padre=nodoActual)
                self.actualizarEquilibrio(nodoActual.hijoIzquierdo)
        elif clave > nodoActual.clave:
            if nodoActual.tieneHijoDerecho():
                self._agregar(clave,valor,nodoActual.hijoDerecho)
            else:
                nodoActual.hijoDerecho = NodoArbol(clave,valor,padre=nodoActual) 
                self.actualizarEquilibrio(nodoActual.hijoDerecho)
        else:
            nodoActual.cargaUtil = valor
    def __setitem__ (self, clave, valor):
        self.agregar (clave,valor)

    def actualizarEquilibrio(self,nodo):
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
            self.reequilibrar(nodo)
            return
        if nodo.padre != None:
            if nodo.esHijoIzquierdo():
                    nodo.padre.factorEquilibrio += 1
            elif nodo.esHijoDerecho():
                    nodo.padre.factorEquilibrio -= 1

            if nodo.padre.factorEquilibrio != 0:
                    self.actualizarEquilibrio(nodo.padre)  

    def rotarIzquierda(self,rotRaiz):
        nuevaRaiz = rotRaiz.hijoDerecho
        rotRaiz.hijoDerecho = nuevaRaiz.hijoIzquierdo
        if nuevaRaiz.hijoIzquierdo != None:
            nuevaRaiz.hijoIzquierdo.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoIzquierdo():
                    rotRaiz.padre.hijoIzquierdo = nuevaRaiz
            else:
                rotRaiz.padre.hijoDerecho = nuevaRaiz
        nuevaRaiz.hijoIzquierdo = rotRaiz
        rotRaiz.padre = nuevaRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio + 1 - min(0, nuevaRaiz.factorEquilibrio)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio + 1 + max(0, rotRaiz.factorEquilibrio)
    
    def rotarDerecha(self,rotRaiz):
        nuevaRaiz = rotRaiz.hijoIzquierdo
        rotRaiz.hijoIzquierdo = nuevaRaiz.hijoDerecho
        if nuevaRaiz.hijoDerecho is not None:
            nuevaRaiz.hijoDerecho.padre = rotRaiz
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoDerecho():
                rotRaiz.padre.hijoDerecho = nuevaRaiz
            else: rotRaiz.padre.hijoIzquierdo = nuevaRaiz
        nuevaRaiz.hijoDerecho = rotRaiz
        rotRaiz.padre = nuevaRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio - 1 - max(0, nuevaRaiz.factorEquilibrio)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio - 1 + min(0, rotRaiz.factorEquilibrio)
    
    def reequilibrar(self, nodo):
        if nodo.factorEquilibrio < 0:
            if nodo.hijoDerecho.factorEquilibrio > 0:
                self.rotarDerecha(nodo.hijoDerecho)
                self.rotarIzquierda(nodo)
            else:
                self.rotarIzquierda(nodo)
        elif nodo.factorEquilibrio > 0:
            if nodo.hijoIzquierdo.factorEquilibrio < 0:
                self.rotarIzquierda(nodo.hijoIzquierdo)
                self.rotarDerecha(nodo)
            else:
                self.rotarDerecha(nodo)

    def obtener(self,clave):
       if self.raiz:
        res = self._obtener(clave,self.raiz)
        if res:
            return res.cargaUtil
        else:
            return None
       else:
            return None

    def _obtener(self,clave,nodoActual):
        if not nodoActual:
            return None
        elif nodoActual.clave == clave:
            return nodoActual
        elif clave < nodoActual.clave:
            return self._obtener(clave,nodoActual.hijoIzquierdo)
        else:
            return self._obtener(clave,nodoActual.hijoDerecho)

    def __getitem__(self,clave):
        result = self.obtener(clave)
        if result is None:
            raise KeyError("Key not found")
        return result
    
    def __contains__(self,clave):
        if self._obtener(clave,self.raiz):
            return True
        else:
            return False
    
    # Método auxiliar para calcular la altura de un nodo
    def _altura(self, nodo):
        if nodo is None:
            return -1 
        return 1 + max(self._altura(nodo.hijoIzquierdo), self._altura(nodo.hijoDerecho))
      
    def eliminar(self, clave):
        nodoAEliminar = self._obtener(clave, self.raiz)

        if not nodoAEliminar:
            raise KeyError('Error, la clave no está en el árbol')

        if self.tamano == 1 and nodoAEliminar == self.raiz:
            self.raiz = None
            self.tamano = 0
            return 

        if nodoAEliminar.esRaiz():
            self.remover(nodoAEliminar)
            if self.raiz is not None:
                 self._rebalance_up(self.raiz)
        else:
            padre_original = nodoAEliminar.padre
            self.remover(nodoAEliminar)
            self._rebalance_up(padre_original)
        self.tamano = self.tamano - 1


    def remover(self, nodoActual):
        if nodoActual.esRaiz():
             # Caso 1: Raíz es hoja
             if nodoActual.esHoja():
                  self.raiz = None
             # Caso 2: Raíz con un hijo
             elif nodoActual.tieneUnSoloHijo():
                  self.raiz = nodoActual.hijoIzquierdo if nodoActual.tieneHijoIzquierdo() else nodoActual.hijoDerecho
                  self.raiz.padre = None 
             # Caso 3: Raíz con dos hijos
             else:
                  sucesor = nodoActual.encontrarSucesor()
                  nodoActual.clave = sucesor.clave
                  nodoActual.cargaUtil = sucesor.cargaUtil
                  self.remover(sucesor) 
             return

        # Caso 1: el nodo es una hoja
        if nodoActual.esHoja():
            if nodoActual.esHijoIzquierdo():
                nodoActual.padre.hijoIzquierdo = None
            else:
                nodoActual.padre.hijoDerecho = None

        # Caso 2: el nodo tiene un solo hijo
        elif nodoActual.tieneUnSoloHijo():
             if nodoActual.tieneHijoIzquierdo():
                if nodoActual.esHijoIzquierdo():
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo
                else:
                    nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo
                nodoActual.hijoIzquierdo.padre = nodoActual.padre
             else:
                if nodoActual.esHijoIzquierdo():
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho
                else:
                    nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho
                nodoActual.hijoDerecho.padre = nodoActual.padre

        # Caso 3: el nodo tiene dos hijos
        else:
            sucesor = nodoActual.encontrarSucesor()
            nodoActual.clave = sucesor.clave
            nodoActual.cargaUtil = sucesor.cargaUtil
            self.remover(sucesor)

    def _rebalance_up(self, nodo):
        # Recorrer hacia arriba desde el nodo dado hasta la raíz
        current_node = nodo
        while current_node is not None:
            # 1. Recalcular el factor de equilibrio
            left_h = self._altura(current_node.hijoIzquierdo)
            right_h = self._altura(current_node.hijoDerecho)
            current_node.factorEquilibrio = left_h - right_h

            # 2. Verificar si hay desequilibrio
            if abs(current_node.factorEquilibrio) > 1:
                self.reequilibrar(current_node)
                pass 
            current_node = current_node.padre

if __name__ == "__main__":
    arbol_de_prueba = ArbolBinarioBusqueda_AVL ()
    arbol_de_prueba.agregar (30,"Melina")
    
    arbol_de_prueba.agregar (10, "Esteban")
    
    arbol_de_prueba.agregar (20, "Juan")