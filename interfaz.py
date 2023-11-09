import tkinter as tk
from tkinter import simpledialog
from tkinter import filedialog
import pandas as pd

# Función para mostrar el cuadro de diálogo de subir plano
def subir_plano():
    # Aquí puedes agregar la lógica para subir un plano
    archivo_path = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xls"), ("Archivos CSV", "*.csv")])
    if archivo_path:
        try:
            if archivo_path.endswith(".xls"):
                # Leer un archivo Excel (.xls)
                df = pd.read_excel(archivo_path)
            elif archivo_path.endswith(".csv"):
                # Leer un archivo CSV (.csv)
                df = pd.read_csv(archivo_path)
            
            # Aquí puedes hacer lo que quieras con los datos leídos (por ejemplo, imprimirlos)
            print("Datos leídos:")
            print(df)
        except Exception as e:
            print("Error al leer el archivo:", str(e))

# Función para mostrar el cuadro de diálogo de entrada de datos
def solicitar_datos():
    data1 = simpledialog.askstring("Entrada de Datos", "Ingrese el dato 1:")
    data2 = simpledialog.askstring("Entrada de Datos", "Ingrese el dato 2:")
    data3 = simpledialog.askstring("Entrada de Datos", "Ingrese el dato 3:")
    
    # Imprimir los datos ingresados (puedes hacer lo que quieras con ellos)
    print("Dato 1:", data1)
    print("Dato 2:", data2)
    print("Dato 3:", data3)

# Crear una ventana principal
ventana = tk.Tk()
ventana.title("Ventana con Entrada de Datos")
# Obtener las dimensiones de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Calcular las coordenadas para centrar la ventana
x = (ancho_pantalla - 600) // 2
y = (alto_pantalla - 400) // 2
# Configurar las dimensiones de la ventana
ventana.geometry(f"{600}x{400}+{x}+{y}")

# Botón para subir plano
boton_subir_plano = tk.Button(ventana, text="Subir Plano", command=subir_plano)
boton_subir_plano.pack()

# Botón para aceptar datos
boton_aceptar = tk.Button(ventana, text="Aceptar Datos", command=solicitar_datos)
boton_aceptar.pack()

# Botón para cancelar
boton_cancelar = tk.Button(ventana, text="Cancelar", command=ventana.quit)
boton_cancelar.pack()

# Iniciar el bucle principal de la ventana
ventana.mainloop()