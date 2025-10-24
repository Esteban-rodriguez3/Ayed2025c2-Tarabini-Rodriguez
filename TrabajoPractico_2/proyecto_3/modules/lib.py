import sys
from .monticulo import MonticuloBinario

def prim(G, inicio):
    """algoritmo de Prim"""
    punto_cero = None
    cp = MonticuloBinario()
    for v in G:
        if v.obtenerId() == inicio:
            v.asignarDistancia(0)
        else:
            v.asignarDistancia(sys.maxsize)
        v.asignarPredecesor(None)
        cp.insertar(v)
    while cp.hayElementos():
        verticeActual = cp.eliminarMinimo()
        for verticeSiguiente in verticeActual.obtenerConexiones():
            nuevoCosto = verticeActual.obtenerPonderacion(verticeSiguiente)
            if verticeSiguiente in cp and nuevoCosto < verticeSiguiente.obtenerDistancia():
                verticeSiguiente.asignarPredecesor(verticeActual)
                verticeSiguiente.asignarDistancia(nuevoCosto)
                cp.reacomodarElemento(verticeSiguiente)