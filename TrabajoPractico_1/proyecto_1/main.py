import time, random, csv
import matplotlib.pyplot as plt
from odf.opendocument import OpenDocumentSpreadsheet
from odf.style import Style, TableColumnProperties, TableRowProperties, TextProperties
from odf.table import Table, TableColumn, TableRow, TableCell
from odf.text import P
from modules.ListaDobleEnlazada import ListaDobleEnlazada 

# ----------------------------
# Función para medir tiempos
# ----------------------------

def medir_tiempos(funcion, N_valores):
    tiempos = []
    for N in N_valores:
        lista = ListaDobleEnlazada()
        for _ in range(N):
            lista.agregar_al_final(random.randrange(500))
        inicio = time.time()
        funcion(lista)
        fin = time.time()
        tiempos.append(fin - inicio)
    return tiempos

print('* INICIO')

# Valores de prueba
N = list(range(10000, 100001, 10000))
tiempos_len = medir_tiempos(lambda l: len(l), N)
tiempos_copiar = medir_tiempos(lambda l: l.copiar(), N)
tiempos_invertir = medir_tiempos(lambda l: l.invertir(), N)

# ----------------------------
# Guardar en CSV
# ----------------------------

with open('tiempos.csv', 'w', newline='') as archivo:
    salida = csv.writer(archivo, dialect='excel')
    salida.writerow(["N"] + N)
    salida.writerow(["len"] + tiempos_len)
    salida.writerow(["copiar"] + tiempos_copiar)
    salida.writerow(["invertir"] + tiempos_invertir)

print("Archivo tiempos.csv generado")

# ----------------------------
# Guardar en ODS
# ----------------------------
doc = OpenDocumentSpreadsheet()
tabla = Table(name="Tiempos LDE")

# Columnas
tabla.addElement(TableColumn(numbercolumnsrepeated=4))

# Encabezado
fila = TableRow()
for titulo in ["Operación"] + [str(n) for n in N]:
    celda = TableCell()
    celda.addElement(P(text=titulo))
    fila.addElement(celda)
tabla.addElement(fila)

# Filas con datos
for nombre, datos in [("len", tiempos_len), ("copiar", tiempos_copiar), ("invertir", tiempos_invertir)]:
    fila = TableRow()
    celda = TableCell()
    celda.addElement(P(text=nombre))
    fila.addElement(celda)
    for valor in datos:
        celda = TableCell()
        celda.addElement(P(text=str(valor)))
        fila.addElement(celda)
    tabla.addElement(fila)

doc.spreadsheet.addElement(tabla)
doc.save("tiempos.ods")

print("Archivo tiempos.ods generado")

# ----------------------------
# Generar gráfica PNG
# ----------------------------
plt.figure(figsize=(8,6))
plt.plot(N, tiempos_len, 'bs-', label="len")        # azul
plt.plot(N, tiempos_copiar, 'ro-', label="copiar")  # rojo
plt.plot(N, tiempos_invertir, 'y^-', label="invertir")  # amarillo

plt.title("Tres operaciones sobre LDE")
plt.xlabel("cantidad de elementos")
plt.ylabel("tiempo (s)")
plt.legend()
plt.grid()

plt.savefig("operaciones_LDE.png", dpi=150)
plt.show()

print("Imagen operaciones_LDE.png generada")
print('* FIN')
