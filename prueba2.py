import tkinter as tk

def add_input():
    entry = tk.Entry(frame)
    entry.grid(row=len(input_entries) + 1, column=0)
    input_entries.append(entry)

def delete_input():
    if input_entries:
        entry = input_entries.pop()
        entry.grid_forget()  # Remove the entry widget

def add_label():
    label = tk.Label(frame, text=f"Label {len(label_entries) + 1}")
    label.grid(row=len(label_entries) + 1, column=1)
    label_entries.append(label)

def delete_label():
    if label_entries:
        label = label_entries.pop()
        label.grid_forget()  # Remove the label widget

root = tk.Tk()
root.title("Dynamic Inputs and Labels")

frame = tk.Frame(root)
frame.grid(row=0, column=0)

input_entries = []  # To keep track of dynamic input fields
label_entries = []  # To keep track of dynamic labels

add_input_button = tk.Button(root, text="Add Input", command=add_input)
add_input_button.grid(row=1, column=0)

delete_input_button = tk.Button(root, text="Delete Input", command=delete_input)
delete_input_button.grid(row=2, column=0)

add_label_button = tk.Button(root, text="Add Label", command=add_label)
add_label_button.grid(row=1, column=1)

delete_label_button = tk.Button(root, text="Delete Label", command=delete_label)
delete_label_button.grid(row=2, column=1)

root.mainloop()
