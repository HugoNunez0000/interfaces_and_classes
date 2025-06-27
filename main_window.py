'''
En este archivo deberá crear la ventana principal de la aplicación.
Implemente el diseño de la imagen "main_window.png". Cuando presione
el botón "Roca", se deberá abrir una ventana secundaria con el diseño
del archivo rock_database.py.
'''

import tkinter as tk
from rock_database import RockDatabase


root = tk.Tk()

def rock_database(*event):
    # win = tk.Toplevel()
    win = RockDatabase(root)
button_rock = tk.Button(root, text = 'Roca',width=20, command=rock_database)
button_rock.pack(padx=10, pady=5)

button_rock = tk.Button(root, text = 'Explosivos',width=20)
button_rock.pack(padx=10, pady=5)

button_rock = tk.Button(root, text = 'Equipo',width=20)
button_rock.pack(padx=10, pady=5)

# Binding:
#Widget.bind.(accion, funcion)
root.bind('<Control-r>', rock_database)
button_rock.bind('<Return>', rock_database)


root.mainloop()