from modules.AVL import NodoArbol, ArbolBinarioBusqueda_AVL
from datetime import date
from modules.Temperaturas_DB import Temperaturas_DB

db = Temperaturas_DB()

db.cargar_muestras("muestras.txt")

print("\n--- INICIO DE PRUEBAS ---")

print(f"Cantidad total de muestras: {db.cantidad_muestras()}")

print("\nDevolver temperatura del 02/01/2025:")
print(f"{db.devolver_temperatura(date(2025, 1, 2))} °C") # Debería ser 38.6

print ("\nMaximo del rango (Enero 2025):")
print(db.max_temp_rango(date(2025, 1, 1), date(2025, 1, 31))) # Debería ser 39.5

print ("\nMínimo del rango (Enero 2025):")
print(db.min_temp_rango(date(2025, 1, 1), date(2025, 1, 31))) # Debería ser 11.9

print ("\nTemperaturas extremas (Febrero 2025):")
print(db.temp_extremos_rango(date(2025, 2, 1), date(2025, 2, 28))) # Debería ser (14.8, 39.9)
    
print("\nListado de temperaturas (primera semana de Marzo 2025):")
fecha_ini = date(2025, 3, 1)
fecha_fin = date(2025, 3, 7)
for linea in db.devolver_temperaturas(fecha_ini, fecha_fin):
    print(linea)

print("\nBorrar la temperatura del 11/01/2025 (39.5 °C)")
db.borrar_temperatura(date(2025, 1, 11))

print (f"Maximo del rango (Enero 2025) después de borrar:")
print(db.max_temp_rango(date(2025, 1, 1), date(2025, 1, 31))) # Debería ser 39.0

print(f"\nCantidad de muestras después de borrar: {db.cantidad_muestras()}")

print("\n--- FIN DE PRUEBAS ---")