import tkinter as tk

def insert_row():
    entry1 = tk.Entry(frame)
    entry2 = tk.Entry(frame)
    entry3 = tk.Entry(frame)
    label1 = tk.Label(frame,text="Rubrica")
    label2 = tk.Label(frame,text="Rubrica")
    label3 = tk.Label(frame,text="Rubrica")
    
    row = len(input_rows)
    label1.grid(row=row, column=0)
    entry1.grid(row=row, column=1)
    label2.grid(row=row, column=2)
    entry2.grid(row=row, column=3)
    label3.grid(row=row, column=4)
    entry3.grid(row=row, column=5)
    
    label_rows.append((label1,label2,label3))
    input_rows.append((entry1, entry2, entry3))

def delete_row():
    if input_rows:
        row = input_rows.pop()
        rowL = label_rows.pop()
        for widget in row:
            widget.grid_remove()
        for widget in rowL:
            widget.grid_remove()

root = tk.Tk()
root.title("CREAR NUEVA RUBRICA")
root.geometry("720x480")

frame = tk.Frame(root)
frame.grid(row=0, column=0)

input_rows = []  # To keep track of rows of input fields
label_rows = []

# Create the initial row of input fields
insert_row()

insert_button = tk.Button(frame, text="Agregar Rubrica", command=insert_row)
insert_button.grid(row=1, column=6)

delete_button = tk.Button(frame, text="Eliminar Rubrica", command=delete_row)
delete_button.grid(row=1, column=7)

root.mainloop()
