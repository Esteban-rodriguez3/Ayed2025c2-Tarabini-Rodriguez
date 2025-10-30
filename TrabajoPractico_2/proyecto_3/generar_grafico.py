import networkx as nx
import matplotlib.pyplot as plt
import csv
import re
import matplotlib
import os

matplotlib.use('Agg')

def generar_grafico_aldeas(archivo_entrada='aldeas.txt', archivo_salida='red_de_aldeas.png'):
    """
    Lee un archivo de aldeas y genera una visualización del grafo no dirigido
    correspondiente, guardándola como una imagen PNG.
    """
    print("Iniciando la generación del gráfico...")

    # Verificar si el archivo de entrada existe
    if not os.path.exists(archivo_entrada):
        print(f"Error: El archivo '{archivo_entrada}' no se encontró.")
        print("Asegúrate de que el archivo esté en la misma carpeta que este script.")
        return

    # Crear un grafo no dirigido
    G = nx.Graph()

    # --- 1. Leer el archivo aldeas.txt y poblar el grafo ---
    try:
        with open(archivo_entrada, encoding='utf-8') as archivo:
            datos = csv.reader(archivo)
            for dato in datos:
                # Omitir líneas que no tengan 3 campos
                if len(dato) == 3:
                    try:
                        # Limpiar los strings de origen y destino
                        origen = re.sub(r'\\s*', '', dato[0]).strip()
                        destino = re.sub(r'\\s*', '', dato[1]).strip()
                        distancia = int(dato[2].strip())
                        
                        # Agregar la arista solo si origen y destino son válidos
                        if origen and destino:
                            G.add_edge(origen, destino, weight=distancia)
                    
                    except ValueError:
                        # Si falla la conversión a 'int'
                        print(f"Omitiendo línea con distancia no válida: {dato}")
                else:
                    # Si la línea no tiene 3 campos o está mal formada
                    print(f"Omitiendo línea mal formada: {dato}")

        print(f"Grafo creado con {G.number_of_nodes()} nodos y {G.number_of_edges()} aristas.")

        # --- 2. Dibujar el Grafo con mejoras de claridad y tamaño ---
        
        # Aumentar significativamente el tamaño de la figura (lienzo)
        plt.figure(figsize=(25, 20))

        # Calcular una disposición de los nodos (layout)
        # k: ajusta la distancia óptima entre nodos. Valores más altos separan más.
        # seed: para resultados reproducibles.
        print("Calculando disposición de nodos (layout)...")
        pos = nx.spring_layout(G, k=0.9, iterations=100, seed=42)

        # Dibujar los nodos
        nx.draw_networkx_nodes(G, pos, node_size=1500, node_color='#b3e0ff', alpha=0.9, edgecolors='gray', linewidths=1.0)

        # Dibujar las aristas
        nx.draw_networkx_edges(G, pos, edge_color='gray', width=1.5, alpha=0.7)

        # Dibujar las etiquetas de los nodos (nombres de aldeas)
        nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif', font_color='black')

        # Dibujar las etiquetas de las aristas (distancias)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, font_color='darkgreen', bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', boxstyle='round,pad=0.2'))

        # Título y limpieza
        plt.title("Red de Aldeas y Distancias (Grafo Completo)", fontsize=24, weight='bold')
        plt.axis('off') # Ocultar los ejes

        # Ajustar el layout para evitar que las etiquetas se corten
        plt.tight_layout()

        # --- 3. Guardar la imagen en un archivo ---
        plt.savefig(archivo_salida, format="PNG", dpi=150, bbox_inches='tight')
        
        print(f"\n¡Éxito! Gráfico mejorado guardado como: {archivo_salida}")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# --- Punto de entrada principal ---
# Esto permite que el script sea ejecutado directamente desde la terminal
if __name__ == "__main__":
    generar_grafico_aldeas()