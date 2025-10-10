import random
import timeit
from matplotlib import pyplot as plt 
from modules.Burbuja import ordenamientoBurbuja
from modules.Ordenamiento_rapido import ordenamientoRapido
from modules.RS import ordenamientoPorResiduos

CANTIDAD = 5000
REPETICIONES = 5

print("* INICIO")

enes = list(range(250,CANTIDAD+1,250))
# listas para guardar los tiempos de ordenamiento para los distintos 'enes'
tiempos_burbuja = []
tiempos_radixsort = []
tiempos_quicksort = []
tiempos_sorted = []

numeros = [random.randint(10000,99999) for _ in range(CANTIDAD)]

for n in enes:
    lista_burbuja = numeros[0:n].copy()
    medidor_b = timeit.Timer("ordenamientoBurbuja(lista_burbuja)", "from __main__ import ordenamientoBurbuja, lista_burbuja")
    tiempo_b = medidor_b.timeit(number=REPETICIONES)
    tiempos_burbuja.append(tiempo_b)

    lista_quicksort = numeros[0:n].copy()
    medidor_q = timeit.Timer("ordenamientoRapido(lista_quicksort)", "from __main__ import ordenamientoRapido, lista_quicksort")
    tiempo_q = medidor_q.timeit(number=REPETICIONES)
    tiempos_quicksort.append(tiempo_q)

    lista_radixsort = numeros[0:n].copy()
    medidor_r = timeit.Timer("ordenamientoPorResiduos(lista_radixsort)", "from __main__ import ordenamientoPorResiduos, lista_radixsort")
    tiempo_r = medidor_r.timeit(number=REPETICIONES)
    tiempos_radixsort.append(tiempo_r)

    lista_para_sorted = numeros[0:n].copy()
    medidor_s = timeit.Timer("sorted(lista_para_sorted)", "from __main__ import lista_para_sorted")
    tiempo_s = medidor_s.timeit(number=REPETICIONES)
    tiempos_sorted.append(tiempo_s)

print(f'n: {n:4d} - Tiempos (Burbuja/QuickSort/Residuos/Timsort): {tiempo_b:.4f}s / {tiempo_q:.4f}s / {tiempo_r:.4f}s / {tiempo_s:.4f}s')

# Gráfico con los pares (n,tiempo) obtenidos
figura,ejes = plt.subplots()
ejes.plot(enes,tiempos_burbuja, 'bo-', enes, tiempos_quicksort, 'go-', enes, tiempos_radixsort, 'mx-')
ejes.set_title("Comparación de tiempos de ordenamiento")
ejes.legend(["Burbuja","Quicksort","PorResiduos"])
ejes.set_xlabel("Cantidad de elementos (n)")
ejes.set_ylabel("Tiempo (s)")
plt.grid()
plt.show()

print("* FIN")

#Código para generar imagen

figura, ejes = plt.subplots()
ejes.plot(enes, tiempos_quicksort, 'go-', label="Quicksort")
ejes.plot(enes, tiempos_radixsort, 'mx-', label="PorResiduos")
ejes.plot(enes, tiempos_sorted, 'co-', label="Timsort (sorted)")

ejes.set_title("Comparación de tiempos de ordenamiento")
ejes.set_xlabel("Cantidad de elementos (n)")
ejes.set_ylabel(f"Tiempo total para {REPETICIONES} ejecuciones (s)")
ejes.legend()
plt.grid(True)

# Guardar imagen para verla en GitHub
plt.savefig("comparacion_ordenamientos.png", dpi=150)

plt.show()