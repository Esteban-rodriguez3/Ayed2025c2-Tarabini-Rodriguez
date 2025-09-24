import time
import random
import csv
import matplotlib.pyplot as plt
import xlsxwriter
from modules.ListaDobleEnlazada import ListaDobleEnlazada


def medir_tiempos(funcion, N_valores):
    """Mide el tiempo de ejecución de una función sobre una ListaDobleEnlazada para diferentes tamaños (N)."""
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

# --- Script Principal ---

print('* INICIO DEL PROCESO')

# 1. Definir los tamaños de N para las pruebas
N_valores = list(range(10000, 100001, 10000))

# 2. Medir los tiempos para cada operación
print("Midiendo tiempos para 'len', 'copiar' e 'invertir'...")
tiempos_len = medir_tiempos(lambda l: len(l), N_valores)
tiempos_copiar = medir_tiempos(lambda l: l.copiar(), N_valores)
tiempos_invertir = medir_tiempos(lambda l: l.invertir(), N_valores)

# 3. Generar y guardar la gráfica PNG
print("Generando la imagen del gráfico...")
nombre_imagen = "operaciones_LDE.png"

plt.figure(figsize=(8, 6))
plt.plot(N_valores, tiempos_len, 'bs-', label="len")
plt.plot(N_valores, tiempos_copiar, 'ro-', label="copiar")
plt.plot(N_valores, tiempos_invertir, 'y^-', label="invertir")

plt.title("Tres operaciones sobre Lista Doblemente Enlazada")
plt.xlabel("Cantidad de elementos (N)")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.legend()
plt.grid(True)

plt.savefig(nombre_imagen, dpi=150)
print(f"Imagen '{nombre_imagen}' guardada.")

# 4. Crear el archivo CSV con los datos
print("Creando el archivo CSV 'tiempos.csv'...")
nombre_csv = 'tiempos.csv'
with open(nombre_csv, 'w', newline='') as archivo_csv:
    salida = csv.writer(archivo_csv)
    salida.writerow(["N"] + N_valores)
    salida.writerow(["len"] + tiempos_len)
    salida.writerow(["copiar"] + tiempos_copiar)
    salida.writerow(["invertir"] + tiempos_invertir)
print(f"Archivo '{nombre_csv}' generado exitosamente.")


# 5. Crear el archivo Excel con los datos y la imagen
print("Creando el archivo Excel 'reporte_tiempos.xlsx'...")
nombre_excel = 'reporte_tiempos.xlsx'
workbook = xlsxwriter.Workbook(nombre_excel)
worksheet = workbook.add_worksheet("Resultados")

# Formato
worksheet.set_column('A:A', 12)
worksheet.set_column('B:K', 15)
bold_format = workbook.add_format({'bold': True})

# Escribir datos
header = ["Operación"] + N_valores
data_rows = [
    ["len"] + tiempos_len,
    ["copiar"] + tiempos_copiar,
    ["invertir"] + tiempos_invertir
]

worksheet.write_row('A1', header, bold_format)
for row_num, row_data in enumerate(data_rows, 1):
    worksheet.write_row(row_num, 0, row_data)

# Insertar imagen
fila_insercion_imagen = len(data_rows) + 3
worksheet.insert_image(f'A{fila_insercion_imagen}', nombre_imagen)

# Guardar y cerrar Excel
workbook.close()
print(f"Archivo '{nombre_excel}' generado exitosamente.")

print('* FIN DEL PROCESO')