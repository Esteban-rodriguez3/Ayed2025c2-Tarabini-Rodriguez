
from modules.AVL import ArbolBinarioBusqueda_AVL
from datetime import datetime, timedelta


class Temperaturas_DB:
    def __init__(self):
        self.arbol = ArbolBinarioBusqueda_AVL()

    def guardar_temperatura(self, temperatura, fecha):
        self.arbol[fecha] = temperatura

    def devolver_temperatura(self, fecha):
        try:
            return self.arbol[fecha]
        except KeyError:
            return None  # O lo que quieras devolver si no existe la fecha
    

    def max_temp_rango(self, fecha1, fecha2):
        maximo = -1000
        fecha = fecha1
        while fecha <= fecha2:
            if fecha in self.arbol:
                temp = self.arbol [ fecha ]
                if temp > maximo:
                    maximo = temp
            fecha = fecha + timedelta (1)
        return maximo if maximo != -1000 else None


    def min_temp_rango(self, fecha1, fecha2):
        minimo = 1000
        fecha = fecha1
        while fecha <= fecha2:
            if fecha in self.arbol:
                temp = self.arbol [fecha]
                if temp < minimo:
                    minimo = temp
            fecha = fecha + timedelta (1)
        return minimo if minimo != 1000 else None
    

    def temp_extremos_rango (self, fecha1, fecha2):
        return ( self.min_temp_rango(fecha1, fecha2), self.max_temp_rango (fecha1, fecha2))


    # Opcional: si querés borrar una temperatura
    def borrar_temperatura(self, fecha):
        try:
            self.arbol.eliminar(fecha) # <--- ESTA ES LA FORMA CORRECTA
        except KeyError:
            print(f"No se encontró la temperatura para la fecha {fecha} para borrar.")
            pass

    def devolver_temperaturas (self, fecha1, fecha2):
        resultados = []
        fecha = fecha1
        while fecha <= fecha2:
            if fecha in self.arbol:
                temp = self.arbol[fecha]
                resultados.append(fecha.strftime("%d/%m/%Y") + f":{temp} °C ")
            fecha += timedelta(1)
        return resultados

    def cantidad_muestras (self):
        return len (self.arbol)
    
    def __delitem__(self, clave):
        # Asumiendo que el método _obtener es correcto y devuelve el NODO
        nodo_a_eliminar = self.arbol._obtener(clave, self.arbol.raiz)
        if nodo_a_eliminar:
            self.arbol.eliminar(clave) # Usamos el método eliminar del AVL
        else:
            raise KeyError("Clave no encontrada para eliminar")
    
    def cargar_muestras(self, nombre_archivo):
        "Carga muestras desde un archivo de texto. El formato esperado por línea es: dd/mm/aaaa;temperatura"
        try:
            with open(nombre_archivo, 'r') as f:
                print(f"Cargando muestras desde {nombre_archivo}...")
                count = 0
                for linea in f:
                    linea_limpia = linea.strip()
                    
                    # Ignora líneas vacías o comentarios (que empiezan con #)
                    if not linea_limpia or linea_limpia.startswith('#'):
                        continue
                    
                    # CORREGIDO para usar punto y coma (;)
                    partes = linea_limpia.split(';') 
                    
                    if len(partes) != 2:
                        print(f"  [Error] Línea mal formada, saltando: {linea_limpia}")
                        continue
                        
                    fecha_str = partes[0].strip()
                    temp_str = partes[1].strip()
                    
                    try:
                        # Convertimos el string a un objeto 'date'
                        fecha_obj = datetime.strptime(fecha_str, "%d/%m/%Y").date()
                        temp_obj = float(temp_str)
                        
                        # Usamos el método existente para guardar
                        self.guardar_temperatura(temp_obj, fecha_obj)
                        count += 1
                    
                    except ValueError as e:
                        print(f"  [Error] Datos inválidos en línea '{linea_limpia}': {e}")
                        
            print(f"Carga finalizada. Se agregaron {count} nuevas muestras.")
            
        except FileNotFoundError:
            print(f"Error: No se pudo encontrar el archivo {nombre_archivo}.")
        except Exception as e:
            print(f"Ocurrió un error inesperado al leer el archivo: {e}")