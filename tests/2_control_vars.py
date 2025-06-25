# Crear interfaces gráficas de usuario:
import tkinter as tk

# Cuadros de mensaje:
from tkinter import messagebox


# Ventana principal:
root = tk.Tk()

# Variables de control:
var_1 = tk.DoubleVar()
var_2 = tk.IntVar()
var_3 = tk.StringVar()
var_4 = tk.BooleanVar()

# Crear elemento gráfico:
entry = tk.Entry(root, textvariable=var_1)
entry.pack(padx=20, pady=20)

def get_value():
    try:
        value = var_1.get()
    except:
        messagebox.showerror(
            'Ingreso de valor',
            'Asegúrese que la entrada sea un número real.'
        )
        return
    print(value)

# Botón para recupera texto:
button = tk.Button(root, text='Recuperar', command=get_value)
button.pack()

# Ciclo de la ventana principal:
root.mainloop()