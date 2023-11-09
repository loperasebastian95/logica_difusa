import tkinter as tk
from tkinter import messagebox
import json
import os

def insert_row(frame,button):
    if(len(input_rows)>1):
         button.config(state="normal")
         
    labelRubrica = tk.Label(frame, text="Rubrica: "+str(len(input_rows)+1))
    labelBajo = tk.Label(frame, text="Bajo")
    labelMedio = tk.Label(frame, text="Medio")
    labelAlto = tk.Label(frame, text="Alto")
    labelValor1 = tk.Label(frame, text="Valor: 1")
    labelValor2 = tk.Label(frame, text="Valor: 2")
    labelValor3 = tk.Label(frame, text="Valor: 1")
    labelValor4 = tk.Label(frame, text="Valor: 2")
    labelValor5 = tk.Label(frame, text="Valor: 1")
    labelValor6 = tk.Label(frame, text="Valor: 2")

    entryMateria = tk.Entry(frame)
    entryRubrica = tk.Entry(frame)
    entryValor1_1 = tk.Entry(frame)
    entryValor1_2 = tk.Entry(frame)
    
    entryValor2_1 = tk.Entry(frame)
    entryValor2_2 = tk.Entry(frame)
    
    entryValor3_1 = tk.Entry(frame)
    entryValor3_2 = tk.Entry(frame)
    
    selected_option_bajo = tk.StringVar()
    select_menu_bajo = tk.OptionMenu(frame, selected_option_bajo, "Mayor", "Igual", "Entre", "Menor", "Menor o Igual", "Mayor o Igual")
    
    selected_option_medio = tk.StringVar()
    select_menu_medio = tk.OptionMenu(frame, selected_option_medio, "Mayor", "Igual", "Entre", "Menor", "Menor o Igual", "Mayor o Igual")
    
    selected_option_alto = tk.StringVar()
    select_menu_alto = tk.OptionMenu(frame, selected_option_alto, "Mayor", "Igual", "Entre", "Menor", "Menor o Igual", "Mayor o Igual")
    
    row = len(input_rows)
    rowL = len(label_rows)
    rowSM = len(select_menu_rows)
    
    #Label rubrica
    labelRubrica.grid(row=rowL*6+1, column=0)
    
    labelBajo.grid(row=rowL*6+1,column=2)
    labelMedio.grid(row=rowL*7+1,column=2)
    labelAlto.grid(row=rowL*8+1,column=2)
    
    select_menu_bajo.grid(row=rowSM*6+1,column=4)
    select_menu_medio.grid(row=rowSM*7+1,column=4)
    select_menu_alto.grid(row=rowSM*8+1,column=4)
    
    #Valor 1
    labelValor1.grid(row=rowL*6+1, column=5)
    #Valor 2
    labelValor2.grid(row=rowL*6+1, column=7)
    
    #Valor 3
    labelValor3.grid(row=rowL*7+1, column=5)
    #Valor 4
    labelValor4.grid(row=rowL*7+1, column=7)
    
    #Valor 5
    labelValor5.grid(row=rowL*8+1, column=5)
    #Valor 6
    labelValor6.grid(row=rowL*8+1, column=7)

    entryRubrica.grid(row=rowL*6+1,column=1)
    entryValor1_1.grid(row=rowL*6+1, column=6)
    entryValor1_2.grid(row=rowL*6+1, column=8)
    entryValor2_1.grid(row=rowL*7+1, column=6)
    entryValor2_2.grid(row=rowL*7+1, column=8)
    entryValor3_1.grid(row=rowL*8+1, column=6)
    entryValor3_2.grid(row=rowL*8+1, column=8)
    
    input_rows.append((entryMateria,entryRubrica,entryValor1_1,entryValor1_2,entryValor2_1,entryValor2_2,entryValor3_1,entryValor3_2))  # To keep track of rows of input fields
    label_rows.append((labelRubrica,labelBajo,labelMedio,labelAlto,labelValor1,labelValor2,labelValor3,labelValor4,labelValor5,labelValor6))
    select_menu_rows.append((select_menu_bajo,select_menu_medio,select_menu_alto))
    select_data_rows.append((selected_option_bajo,selected_option_medio,selected_option_alto))
    
    

def delete_row(frame,button):
    print(len(input_rows))
    if len(input_rows)==1:
        button.config(state="disabled")  
    elif input_rows:
        row = input_rows.pop()
        rowL = label_rows.pop()
        rowSM = select_menu_rows.pop()
        select_data_rows.pop()
        for widget in row:
            widget.grid_remove()
        for widget in rowL:
            widget.grid_remove()
        for widget in rowSM:
            widget.grid_remove()
    

def open_new_frame():
    input_rows.clear()  # To keep track of rows of input fields
    label_rows.clear()
    new_frame = tk.Toplevel(root)
    new_frame.title("Creacion de una nueva materia")
    new_frame.geometry("800x480")
    
    # Create widgets and use the grid manager within the new frame
    labelMateria = tk.Label(new_frame, text="Materia: ")
    labelRubrica = tk.Label(new_frame, text="Rubrica: "+str(len(input_rows)+1))
    labelBajo = tk.Label(new_frame, text="Bajo")
    labelMedio = tk.Label(new_frame, text="Medio")
    labelAlto = tk.Label(new_frame, text="Alto")
    labelValor1 = tk.Label(new_frame, text="Valor: 1")
    labelValor2 = tk.Label(new_frame, text="Valor: 2")
    labelValor3 = tk.Label(new_frame, text="Valor: 1")
    labelValor4 = tk.Label(new_frame, text="Valor: 2")
    labelValor5 = tk.Label(new_frame, text="Valor: 1")
    labelValor6 = tk.Label(new_frame, text="Valor: 2")

    entryMateria = tk.Entry(new_frame)
    entryRubrica = tk.Entry(new_frame)
    entryValor1_1 = tk.Entry(new_frame)
    entryValor1_2 = tk.Entry(new_frame)
    
    entryValor2_1 = tk.Entry(new_frame)
    entryValor2_2 = tk.Entry(new_frame)
    
    entryValor3_1 = tk.Entry(new_frame)
    entryValor3_2 = tk.Entry(new_frame)
    
    selected_option_bajo = tk.StringVar()
    select_menu_bajo = tk.OptionMenu(new_frame, selected_option_bajo, "Mayor", "Igual", "Entre", "Menor", "Menor o Igual", "Mayor o Igual")
    
    selected_option_medio = tk.StringVar()
    select_menu_medio = tk.OptionMenu(new_frame, selected_option_medio, "Mayor", "Igual", "Entre", "Menor", "Menor o Igual", "Mayor o Igual")
    
    selected_option_alto = tk.StringVar()
    select_menu_alto = tk.OptionMenu(new_frame, selected_option_alto, "Mayor", "Igual", "Entre", "Menor", "Menor o Igual", "Mayor o Igual")
    
    
    #Label Materia
    labelMateria.grid(row=0, column=0)
    #Label rubrica
    labelRubrica.grid(row=3, column=0)
    
    labelBajo.grid(row=3,column=2)
    labelMedio.grid(row=4,column=2)
    labelAlto.grid(row=5,column=2)
    
    select_menu_bajo.grid(row=3,column=4)
    select_menu_medio.grid(row=4,column=4)
    select_menu_alto.grid(row=5,column=4)
    
    #Valor 1
    labelValor1.grid(row=3, column=5)
    #Valor 2
    labelValor2.grid(row=3, column=7)
    
    #Valor 3
    labelValor3.grid(row=4, column=5)
    #Valor 4
    labelValor4.grid(row=4, column=7)
    
    #Valor 5
    labelValor5.grid(row=5, column=5)
    #Valor 6
    labelValor6.grid(row=5, column=7)

    entryMateria.grid(row=0,column=1)
    entryRubrica.grid(row=3,column=1)
    entryValor1_1.grid(row=3, column=6)
    entryValor1_2.grid(row=3, column=8)
    entryValor2_1.grid(row=4, column=6)
    entryValor2_2.grid(row=4, column=8)
    entryValor3_1.grid(row=5, column=6)
    entryValor3_2.grid(row=5, column=8)
    
    
    
    input_rows.append((entryMateria,entryRubrica,entryValor1_1,entryValor1_2,entryValor2_1,entryValor2_2,entryValor3_1,entryValor3_2))  # To keep track of rows of input fields
    label_rows.append((labelRubrica,labelBajo,labelMedio,labelAlto,labelValor1,labelValor2,labelValor3,labelValor4,labelValor5,labelValor6))
    select_menu_rows.append((select_menu_bajo,select_menu_medio,select_menu_alto))
    select_data_rows.append((selected_option_bajo,selected_option_medio,selected_option_alto))
    
    delete_button = tk.Button(new_frame, text="Eliminar Rubrica",width=15, height=2,cursor="hand2")
    delete_button.grid(row=4, column=10, columnspan=2)

    # Bind the delete_row function to the button with lambda to pass the button reference
    delete_button.config(command=lambda button=delete_button: delete_row(new_frame, button))
    delete_button.config(state="disabled")
    
    #delete_button = tk.Button(new_frame, text="Eliminar Rubrica", command=lambda: delete_row(new_frame,delete_button))
    #delete_button.grid(row=4, column=7, columnspan=2)

    insert_button = tk.Button(new_frame, text="Agregar Rubrica",width=15, height=2,cursor="hand2",  command=lambda: insert_row(new_frame,delete_button))
    insert_button.grid(row=3, column=10, columnspan=2)
    
    guardar = tk.Button(new_frame, text="Guardar",width=15, height=2,cursor="hand2",  command=lambda: saveDataRubrica(new_frame,entryMateria))
    guardar.grid(row=5, column=10, columnspan=2)
    
def saveDataRubrica(frame,titleMateria):
    dataJson = []
    jsonArray = []
    if not titleMateria.get():
        messagebox.showinfo("Informacion","Debe llenar el nombre de la materia")
        frame.focus_set()
        return
    countRows = 0
    for entry in input_rows:
        entryMateria,entryRubrica,entryValor1_1,entryValor1_2,entryValor2_1,entryValor2_2,entryValor3_1,entryValor3_2 = entry
        selectOne,selectTwo,selectThree = select_data_rows[countRows]
        if (not entryMateria.get() or (not entryRubrica.get())):
            messagebox.showinfo("Informacion","Debe llenar el nombre de la materia")
            frame.focus_set()
            return
        else:
            datos = {
                "nombreRubrica":entryRubrica.get(),
                "operador1":selectOne.get(),
                "operador2":selectTwo.get(),
                "operador3":selectThree.get(),
                "valorBajoInicial":entryValor1_1.get(),
                "valorBajoFinal":entryValor1_2.get(),
                "valorMedioInicial":entryValor2_1.get(),
                "valorMedioFinal":entryValor2_2.get(),
                "valorAltoInicial":entryValor3_1.get(),
                "valorAltoFinal":entryValor3_2.get()           
            }
            dataJson.append(datos)
        countRows+=1
    jsonRespuesta = {
        "nombreMateria":titleMateria.get(),
        "datosMateria":dataJson
    }
    jsonArray.append(jsonRespuesta)
    jsonRespuesta2 = json.dumps(jsonArray,indent=4)
    
    file_path = 'materias.txt'  # Replace with the path to your file
    if os.path.exists(file_path):    
        with open('materias.txt', 'r') as archivo:
            datosArchivo = archivo.read()

        if not datosArchivo:
            with open('materias.txt', 'w') as archivo:
                # Escribe información en el archivo
                archivo.write(jsonRespuesta2)
            messagebox.showinfo("Informacion operacion","Datos almacenados correctamente")   
            frame.destroy()
        else:
            existing_data = json.loads(datosArchivo)
            existing_data.append(jsonRespuesta)
            # Convert the updated list back to a JSON string
            updated_json = json.dumps(existing_data, indent=4)
            with open('materias.txt', 'w') as archivo:
                # Escribe información en el archivo
                 archivo.write(updated_json)
            messagebox.showinfo("Informacion operacion","Datos almacenados correctamente")   
            frame.destroy()
    else:
        with open('materias.txt', 'w') as archivo:
            archivo.write(jsonRespuesta2)
            
        messagebox.showinfo("Informacion operacion","Datos almacenados correctamente")   
        frame.destroy()
        
        

# El archivo se cierra automáticamente cuando salimos del bloque "with"
     
def procesar_datos():
    file_path = 'materias.txt'  # Replace with the path to your file
    if os.path.exists(file_path): 
        with open('materias.txt', 'r') as archivo:
            datosArchivo = json.load(archivo)
    
    for materia in datosArchivos:
        if(materia['operador']=='Mayor'):
            pass
#def selected_option()
    
    

root = tk.Tk()
root.title("PROGRAMA DE LÓGICA DIFUSA")
root.geometry("720x480")
root.configure(bg="#4c98cf")

input_rows = []  # To keep track of rows of input fields
label_rows = []
label_materias_rows=[]
select_menu_rows = []
select_data_rows = []

# Create a button to open a new frame
new_frame_button = tk.Button(root, text="Crear Materia",width=15, height=2,cursor="hand2", command=open_new_frame)
new_frame_button.place(rely=0.5, relx=0.20)

editar_button = tk.Button(root, text="Editar Rubricas",width=15, height=2,cursor="hand2", command=open_new_frame)
editar_button.place(rely=0.5, relx=0.42)

cargar_button = tk.Button(root, text="Cargar calificaciones",width=15, height=2,cursor="hand2", command=open_new_frame)
cargar_button.place(rely=0.5, relx=0.65)

cargar_button = tk.Button(root, text="Procesar",width=15, height=2,cursor="hand2", command=procesar_datos)
cargar_button.place(rely=0.8, relx=0.42)


root.mainloop()
