import tkinter as tk
from tkinter import messagebox
import json
import os
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
from tkinter import filedialog

def insert_row(frame,button):
    if(len(input_rows)>1):
         button.config(state="normal")
         
    labelMateria = tk.Label(frame, text="Materia: ")   
    labelRubrica = tk.Label(frame, text="Rubrica: "+str(len(input_rows)+1))
    labelBajo = tk.Label(frame, text="Bajo")
    labelAceptable = tk.Label(frame, text="Aceptable")
    labelMedio = tk.Label(frame, text="Medio")
    labelAlto = tk.Label(frame, text="Alto")
    labelValor1 = tk.Label(frame, text="Valor: 1")
    labelValor2 = tk.Label(frame, text="Valor: 2")
    labelValor3 = tk.Label(frame, text="Valor: 1")
    labelValor4 = tk.Label(frame, text="Valor: 2")
    labelValor5 = tk.Label(frame, text="Valor: 1")
    labelValor6 = tk.Label(frame, text="Valor: 2")
    labelValor7 = tk.Label(frame, text="Valor: 1")
    labelValor8 = tk.Label(frame, text="Valor: 2")

    entryMateria = tk.Entry(frame)
    entryRubrica = tk.Entry(frame)
    entryValor1_1 = tk.Entry(frame)
    entryValor1_2 = tk.Entry(frame)
    
    entryValor2_1 = tk.Entry(frame)
    entryValor2_2 = tk.Entry(frame)
    
    entryValor3_1 = tk.Entry(frame)
    entryValor3_2 = tk.Entry(frame)
    
    entryValor4_1 = tk.Entry(frame)
    entryValor4_2 = tk.Entry(frame)
    
    selected_option_bajo = tk.StringVar()
    select_menu_bajo = tk.OptionMenu(frame, selected_option_bajo, "Mayor", "Igual", "Entre", "Menor", "Menor o Igual", "Mayor o Igual")
    
    selected_option_aceptable = tk.StringVar()
    select_menu_aceptable = tk.OptionMenu(frame, selected_option_aceptable, "Mayor", "Igual", "Entre", "Menor", "Menor o Igual", "Mayor o Igual")
    
    selected_option_medio = tk.StringVar()
    select_menu_medio = tk.OptionMenu(frame, selected_option_medio, "Mayor", "Igual", "Entre", "Menor", "Menor o Igual", "Mayor o Igual")
    
    selected_option_alto = tk.StringVar()
    select_menu_alto = tk.OptionMenu(frame, selected_option_alto, "Mayor", "Igual", "Entre", "Menor", "Menor o Igual", "Mayor o Igual")
    
    row = len(input_rows)
    rowL = len(label_rows)
    rowSM = len(select_menu_rows)
    
    #Label rubrica
    labelMateria.grid(row=rowL*7,column=0)
    labelRubrica.grid(row=rowL*7+1, column=0)
    
    labelBajo.grid(row=rowL*6+1,column=2)
    labelAceptable.grid(row=rowL*7+1,column=2)
    labelMedio.grid(row=rowL*8+1,column=2)
    labelAlto.grid(row=rowL*9+1,column=2)
    
    select_menu_bajo.grid(row=rowSM*6+1,column=4)
    select_menu_aceptable.grid(row=rowSM*7+1,column=4)
    select_menu_medio.grid(row=rowSM*8+1,column=4)
    select_menu_alto.grid(row=rowSM*9+1,column=4)
    
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
    
    #Valor 7
    labelValor7.grid(row=rowL*9+1, column=5)
    #Valor 8
    labelValor8.grid(row=rowL*9+1, column=7)

    entryMateria.grid(row=rowL*7,column=1)
    entryRubrica.grid(row=rowL*7+1,column=1)
    entryValor1_1.grid(row=rowL*6+1, column=6)
    entryValor1_2.grid(row=rowL*6+1, column=8)
    entryValor2_1.grid(row=rowL*7+1, column=6)
    entryValor2_2.grid(row=rowL*7+1, column=8)
    entryValor3_1.grid(row=rowL*8+1, column=6)
    entryValor3_2.grid(row=rowL*8+1, column=8)
    entryValor4_1.grid(row=rowL*9+1, column=6)
    entryValor4_2.grid(row=rowL*9+1, column=8)
    
    input_rows.append((entryMateria,entryRubrica,entryValor1_1,entryValor1_2,entryValor2_1,entryValor2_2,entryValor3_1,entryValor3_2,entryValor4_1,entryValor4_2))  # To keep track of rows of input fields
    label_rows.append((labelMateria,labelRubrica,labelBajo,labelMedio,labelAlto,labelValor1,labelValor2,labelValor3,labelValor4,labelValor5,labelValor6,labelValor7,labelValor8))
    select_menu_rows.append((select_menu_bajo,select_menu_aceptable,select_menu_medio,select_menu_alto))
    select_data_rows.append((selected_option_bajo,selected_option_aceptable,selected_option_medio,selected_option_alto))
    
    

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
    #new_frame.pack(fill="both",expand=True)
    
    # Create widgets and use the grid manager within the new frame
    labelMateria = tk.Label(new_frame, text="Materia: ")
    labelRubrica = tk.Label(new_frame, text="Rubrica: "+str(len(input_rows)+1))
    labelBajo = tk.Label(new_frame, text="Bajo")
    labelAceptable = tk.Label(new_frame, text="Aceptable")
    labelMedio = tk.Label(new_frame, text="Medio")
    labelAlto = tk.Label(new_frame, text="Alto")
    labelValor1 = tk.Label(new_frame, text="Valor: 1")
    labelValor2 = tk.Label(new_frame, text="Valor: 2")
    labelValor3 = tk.Label(new_frame, text="Valor: 1")
    labelValor4 = tk.Label(new_frame, text="Valor: 2")
    labelValor5 = tk.Label(new_frame, text="Valor: 1")
    labelValor6 = tk.Label(new_frame, text="Valor: 2")
    labelValor7 = tk.Label(new_frame, text="Valor: 1")
    labelValor8 = tk.Label(new_frame, text="Valor: 2")

    entryMateria = tk.Entry(new_frame)
    entryRubrica = tk.Entry(new_frame)
    entryValor1_1 = tk.Entry(new_frame)
    entryValor1_2 = tk.Entry(new_frame)
    
    entryValor2_1 = tk.Entry(new_frame)
    entryValor2_2 = tk.Entry(new_frame)
    
    entryValor3_1 = tk.Entry(new_frame)
    entryValor3_2 = tk.Entry(new_frame)
    
    entryValor4_1 = tk.Entry(new_frame)
    entryValor4_2 = tk.Entry(new_frame)
    
    selected_option_bajo = tk.StringVar()
    select_menu_bajo = tk.OptionMenu(new_frame, selected_option_bajo, "Mayor", "Igual", "Entre", "Menor", "Menor o Igual", "Mayor o Igual")
    
    selected_option_aceptable = tk.StringVar()
    select_menu_aceptable = tk.OptionMenu(new_frame, selected_option_aceptable, "Mayor", "Igual", "Entre", "Menor", "Menor o Igual", "Mayor o Igual")
    
    selected_option_medio = tk.StringVar()
    select_menu_medio = tk.OptionMenu(new_frame, selected_option_medio, "Mayor", "Igual", "Entre", "Menor", "Menor o Igual", "Mayor o Igual")
    
    selected_option_alto = tk.StringVar()
    select_menu_alto = tk.OptionMenu(new_frame, selected_option_alto, "Mayor", "Igual", "Entre", "Menor", "Menor o Igual", "Mayor o Igual")
    
    
    #Label Materia
    labelMateria.grid(row=0, column=0)
    #Label rubrica
    labelRubrica.grid(row=3, column=0)
    
    labelBajo.grid(row=3,column=2)
    labelAceptable.grid(row=4,column=2)
    labelMedio.grid(row=5,column=2)
    labelAlto.grid(row=6,column=2)
    
    select_menu_bajo.grid(row=3,column=4)
    select_menu_aceptable.grid(row=4,column=4)
    select_menu_medio.grid(row=5,column=4)
    select_menu_alto.grid(row=6,column=4)
    
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
    
    labelValor7.grid(row=6, column=5)
    labelValor8.grid(row=6, column=7)

    entryMateria.grid(row=0,column=1)
    entryRubrica.grid(row=3,column=1)
    entryValor1_1.grid(row=3, column=6)
    entryValor1_2.grid(row=3, column=8)
    entryValor2_1.grid(row=4, column=6)
    entryValor2_2.grid(row=4, column=8)
    entryValor3_1.grid(row=5, column=6)
    entryValor3_2.grid(row=5, column=8)
    entryValor4_1.grid(row=6, column=6)
    entryValor4_2.grid(row=6, column=8)
    
    input_rows.append((entryMateria,entryRubrica,entryValor1_1,entryValor1_2,entryValor2_1,entryValor2_2,entryValor3_1,entryValor3_2,entryValor4_1,entryValor4_2))  # To keep track of rows of input fields
    label_rows.append((labelRubrica,labelBajo,labelMedio,labelAlto,labelValor1,labelValor2,labelValor3,labelValor4,labelValor5,labelValor6,labelValor7,labelValor8))
    select_menu_rows.append((select_menu_bajo,select_menu_aceptable,select_menu_medio,select_menu_alto))
    select_data_rows.append((selected_option_bajo,selected_option_aceptable,selected_option_medio,selected_option_alto))
    
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
        entryMateria,entryRubrica,entryValor1_1,entryValor1_2,entryValor2_1,entryValor2_2,entryValor3_1,entryValor3_2,entryValor4_1,entryValor4_2 = entry
        selectOne,selectTwo,selectThree,selectFour = select_data_rows[countRows]
        listaElementos = []
        if (selectOne.get() == "Mayor" or selectOne.get() == "Menor" or selectOne.get() == "Mayor o Igual" or selectOne.get() == "Menor o Igual" or selectOne.get() == "Igual"):
            listaElementos.append(entryValor1_1.get())
        else:
            listaElementos.append(entryValor1_1.get())
            listaElementos.append(entryValor1_2.get())
            
        if (selectTwo.get() == "Mayor" or selectTwo.get() == "Menor" or selectTwo.get() == "Mayor o Igual" or selectTwo.get() == "Menor o Igual" or selectTwo.get() == "Igual"):
            listaElementos.append(entryValor2_1.get())
        else:
            listaElementos.append(entryValor2_1.get())
            listaElementos.append(entryValor2_2.get())
            
        if (selectThree.get() == "Mayor" or selectThree.get() == "Menor" or selectThree.get() == "Mayor o Igual" or selectThree.get() == "Menor o Igual" or selectThree.get() == "Igual"):
            listaElementos.append(entryValor3_1.get())
        else:
            listaElementos.append(entryValor3_1.get())
            listaElementos.append(entryValor3_2.get())
            
        if (selectFour.get() == "Mayor" or selectFour.get() == "Menor" or selectFour.get() == "Mayor o Igual" or selectFour.get() == "Menor o Igual" or selectFour.get() == "Igual"):
            listaElementos.append(entryValor4_1.get())
        else:
            listaElementos.append(entryValor4_1.get())
            listaElementos.append(entryValor4_2.get())
        
        if (not entryMateria.get() or (not entryRubrica.get())):
            messagebox.showinfo("Informacion","Debe llenar el nombre de la materia")
            frame.focus_set()
            return
        elif (validarNumero(listaElementos)):
            messagebox.showinfo("Atencion","Todos los datos deben ser numéricos para continuar")
            frame.focus_set()
            return
        else:
            datos = {
                "nombreRubrica":entryRubrica.get(),
                "operador1":selectOne.get(),
                "operador2":selectTwo.get(),
                "operador3":selectThree.get(),
                "operador4":selectFour.get(),
                "valorBajoInicial":entryValor1_1.get(),
                "valorBajoFinal":entryValor1_2.get(),
                "valorAceptableInicial":entryValor2_1.get(),
                "valorAceptableFinal":entryValor2_2.get(),
                "valorMedioInicial":entryValor3_1.get(),
                "valorMedioFinal":entryValor3_2.get(),
                "valorAltoInicial":entryValor4_1.get(),
                "valorAltoFinal":entryValor4_2.get()             
            }
        countRows+=1
    jsonRespuesta = {
        "nombreMateria":titleMateria.get(),
        "datosMateria":datos
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
        

def procesar_datos(nombreMateria,calificacionMateria):
    file_path = 'materias.txt'  # Reemplaza con la ruta a tu archivo
    try:
        with open(file_path, 'r') as archivo:
            datosArchivo = json.load(archivo)
    except FileNotFoundError:
        print(f"El archivo {file_path} no se encontró.")
        return
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON: {file_path}")
        return

    calificacion_general = ctrl.Consequent(np.arange(0,5,0.1),'calificacionGeneral')
    calificacion_general['Baja'] = fuzz.trapmf(calificacion_general.universe, [0, 0, 2.9, 2.9])
    calificacion_general['Aceptable'] = fuzz.trapmf(calificacion_general.universe, [2.9, 3.0, 3.5, 3.5])
    calificacion_general['Media'] = fuzz.trapmf(calificacion_general.universe, [3.5, 3.6, 4.0, 4.0])
    calificacion_general['Alta'] = fuzz.trapmf(calificacion_general.universe, [4.0, 4.1, 5, 5])

    calificaciones = []

    for materia in datosArchivo:
        if(nombreMateria == materia['nombreMateria']):
            calificacion = ctrl.Antecedent(np.arange(0, 5.1, 0.1),materia['nombreMateria'])
            datosMateria = materia['datosMateria']
            if datosMateria['operador1'] == 'Entre':
                detalle = materia['datosMateria']
                calificacion['Baja'] = fuzz.trapmf(calificacion.universe, [float(detalle['valorBajoInicial']),
                                                                            float(detalle['valorBajoInicial']),
                                                                        float(detalle['valorBajoFinal']),
                                                                        float(detalle['valorBajoFinal'])])
            elif datosMateria['operador1'] == 'Mayor':
                calificacion['Baja'] = fuzz.trapmf(calificacion.universe, [float(detalle['valorBajoFinal']),
                                                                        0,
                                                                        5,
                                                                        1])
            elif datosMateria['operador1'] == 'Menor':
                calificacion['Baja'] = fuzz.trapmf(calificacion.universe, [0,
                                                                        0,
                                                                        float(detalle['valorBajoInicial']),1]),
            
            elif datosMateria['operador1'] == 'Igual':
                calificacion['Baja'] = fuzz.trapmf(calificacion.universe, [float(detalle['valorBajoInicial']),
                                                                        1,
                                                                        float(detalle['valorBajoInicial']),1])        
            elif datosMateria['operador1'] == 'Menor o Igual':
                calificacion['Baja'] = fuzz.trapmf(calificacion.universe, [0,
                                                                        0,
                                                                        float(detalle['valorBajoInicial']),1])
            
            elif datosMateria['operador1'] == 'Mayor o Igual':
                calificacion['Baja'] = fuzz.trapmf(calificacion.universe, [float(detalle['valorBajoInicial']),
                                                                    0,
                                                                    5,
                                                                    1])
                
            if datosMateria['operador2'] == 'Entre':
                detalle = materia['datosMateria']
                calificacion['Aceptable'] = fuzz.trapmf(calificacion.universe, [float(detalle['valorAceptableInicial']),
                                                                        float(detalle['valorAceptableInicial']),
                                                                        float(detalle['valorAceptableFinal']),
                                                                        float(detalle['valorAceptableFinal'])])
            elif datosMateria['operador2'] == 'Mayor':
                calificacion['Aceptable'] = fuzz.trapmf(calificacion.universe, [float(detalle['valorAceptableFinal']),
                                                                        0,
                                                                        5,
                                                                        1])
            elif datosMateria['operador2'] == 'Menor':
                calificacion['Aceptable'] = fuzz.trapmf(calificacion.universe, [0,
                                                                        0,
                                                                        float(detalle['valorAceptableInicial']),1]),
            
            elif datosMateria['operador2'] == 'Igual':
                calificacion['Aceptable'] = fuzz.trapmf(calificacion.universe, [float(detalle['valorAceptableInicial']),
                                                                        1,
                                                                        float(detalle['valorAceptableInicial']),1])        
            elif datosMateria['operador2'] == 'Menor o Igual':
                calificacion['Aceptable'] = fuzz.trapmf(calificacion.universe, [0,
                                                                        0,
                                                                        float(detalle['valorAceptableInicial']),1])
            
            elif datosMateria['operador2'] == 'Mayor o Igual':
                calificacion['Aceptable'] = fuzz.trapmf(calificacion.universe, [float(detalle['valorAceptableInicial']),
                                                                    0,
                                                                    5,
                                                                    1])
            if datosMateria['operador3'] == 'Entre':
                detalle = materia['datosMateria']
                calificacion['Media'] = fuzz.trapmf(calificacion.universe, [float(detalle['valorMedioInicial']),
                                                                        float(detalle['valorMedioInicial']),
                                                                        float(detalle['valorMedioFinal']),
                                                                        float(detalle['valorMedioFinal'])])
            elif datosMateria['operador3'] == 'Mayor':
                calificacion['Media'] = fuzz.trapmf(calificacion.universe, [float(detalle['valorMedioFinal']),
                                                                        0,
                                                                        5,
                                                                        1])
            elif datosMateria['operador3'] == 'Menor':
                calificacion['Media'] = fuzz.trapmf(calificacion.universe, [0,
                                                                        0,
                                                                        float(detalle['valorMedioInicial']),1]),
            
            elif datosMateria['operador3'] == 'Igual':
                calificacion['Media'] = fuzz.trapmf(calificacion.universe, [float(detalle['valorMedioInicial']),
                                                                        1,
                                                                        float(detalle['valorMedioInicial']),1])        
            elif datosMateria['operador3'] == 'Menor o Igual':
                calificacion['Media'] = fuzz.trapmf(calificacion.universe, [0,
                                                                        0,
                                                                        float(detalle['valorMedioInicial']),1])
            
            elif datosMateria['operador3'] == 'Mayor o Igual':
                calificacion['Media'] = fuzz.trapmf(calificacion.universe, [float(detalle['valorMedioInicial']),
                                                                    0,
                                                                    5,
                                                                    1])
                
            if datosMateria['operador4'] == 'Entre':
                detalle = materia['datosMateria']
                calificacion['Alta'] = fuzz.trapmf(calificacion.universe, [float(detalle['valorAltoInicial']),
                                                                        float(detalle['valorAltoInicial']),
                                                                        float(detalle['valorAltoFinal']),
                                                                        float(detalle['valorAltoFinal'])])
            elif datosMateria['operador4'] == 'Mayor':
                calificacion['Alta'] = fuzz.trapmf(calificacion.universe, [float(detalle['valorAltoFinal']),
                                                                        0,
                                                                        5,
                                                                        1])
            elif datosMateria['operador4'] == 'Menor':
                calificacion['Alta'] = fuzz.trapmf(calificacion.universe, [0,
                                                                        0,
                                                                        float(detalle['valorAltoInicial']),1]),
            
            elif datosMateria['operador4'] == 'Igual':
                calificacion['Alta'] = fuzz.trapmf(calificacion.universe, [float(detalle['valorAltoInicial']),
                                                                        0,
                                                                        float(detalle['valorAltoInicial']),1])        
            elif datosMateria['operador4'] == 'Menor o Igual':
                calificacion['Alta'] = fuzz.trapmf(calificacion.universe, [0,
                                                                        0,
                                                                        float(detalle['valorAltoInicial']),1])
            
            elif datosMateria['operador4'] == 'Mayor o Igual':
                calificacion['Alta'] = fuzz.trapmf(calificacion.universe, [float(detalle['valorAltoInicial']),0,5,1])
            calificaciones.append(calificacion)

    reglas = []

    # Crear reglas dinámicamente
    for calificacion_materia in calificaciones:
        regla1 = (ctrl.Rule(calificacion_materia['Baja'], calificacion_general['Baja']))
        regla2 = (ctrl.Rule(calificacion_materia['Aceptable'], calificacion_general['Aceptable']))
        regla3 = (ctrl.Rule(calificacion_materia['Media'], calificacion_general['Media']))
        regla4 = (ctrl.Rule(calificacion_materia['Alta'], calificacion_general['Alta']))
        reglas.append([regla1,regla2,regla3,regla4])

    # Crear un sistema de control
    regla1 = (ctrl.Rule(calificaciones[0]['Baja'], calificacion_general['Baja']))
    regla2 = (ctrl.Rule(calificaciones[0]['Aceptable'], calificacion_general['Aceptable']))
    regla3 = (ctrl.Rule(calificaciones[0]['Media'], calificacion_general['Media']))
    regla4 = (ctrl.Rule(calificaciones[0]['Alta'], calificacion_general['Alta']))
    
    sistema_control = ctrl.ControlSystem([regla1,regla2,regla3,regla4])
    
    sistema = ctrl.ControlSystemSimulation(sistema_control)

    # Configurar las entradas (por ejemplo, establecer la calificación en una materia)
    # Aquí debes ajustar según tus datos específicos
    
    sistema.input['Matematicas'] = float(calificacionMateria)

    # Evaluar el sistema
    sistema.compute()

    # Obtener el resultado
    resultado = sistema.output['calificacionGeneral']
    print(f'Calificación General: {resultado}')
    return resultado

    
    
    '''
    for calificacion_materia in calificaciones:
        plt.plot(calificacion_materia.universe, fuzz.interp_membership(calificacion_materia.universe,
                                                                      calificacion_materia['Baja'].mf, 6),
                 'r', linestyle='dashed', linewidth=1.5)
        plt.plot(calificacion_materia.universe, fuzz.interp_membership(calificacion_materia.universe,
                                                                      calificacion_materia['Media'].mf, 6),
                 'g', linestyle='dashed', linewidth=1.5)
        plt.plot(calificacion_materia.universe, fuzz.interp_membership(calificacion_materia.universe,
                                                                      calificacion_materia['Alta'].mf, 6),
                 'b', linestyle='dashed', linewidth=1.5)

    plt.title('Funciones de membresía para las calificaciones en Matemáticas')
    plt.xlabel('Calificación')
    plt.ylabel('Membresía')
    plt.legend(['Baja', 'Media', 'Alta'])
    plt.show()'''


 
def validarNumero(entries):
    for entrie in entries:
        print(entrie)
        try :
            float(entrie)
            print(float(entrie))
        except:
            return True
    return False

def upload_file():
    # Open file selection dialog
    filename = filedialog.askopenfilename(
        title="Select File",
        filetypes=[("Text files", "*.txt")],
    )

    # Check if file selected
    file_path = 'respuesta.txt'  # Replace with the path to your file
    if filename:
        with open(filename, 'r') as f:
            # Read lines one by one
            for line in f:
               split_parts = line.split("|")
               with open(file_path, 'w') as archivo:
                archivo.write(split_parts[0]+"|"+split_parts[1]+"|"+str(procesar_datos(split_parts[0],split_parts[1])))
            
    
    

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

cargar_button = tk.Button(root, text="Cargar calificaciones",width=15, height=2,cursor="hand2", command=upload_file)
cargar_button.place(rely=0.5, relx=0.65)

cargar_button = tk.Button(root, text="Procesar",width=15, height=2,cursor="hand2", command=procesar_datos)
cargar_button.place(rely=0.8, relx=0.42)


root.mainloop()
