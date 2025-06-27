<<<<<<< HEAD
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
=======
# Creación de interfaces gráficas:
import tkinter as tk

# Ventana de la base de datos para rocas:
from rock_database import RockDatabase


class MainWindow(tk.Tk):
    '''Ventana principal de la aplicación'''

    def __init__(self):
        super().__init__()

        # Crear y colocar elementos gráficos:
        self.create_widgets()
        self.widgets_layout()

    
    def create_widgets(self):
        '''Crear los elementos gráficos de la ventana'''

        # Botones para abrir las bases de datos:
        self.button_rock = tk.Button(self, text='Roca', width=20,
                                     command=self.rock_database)
        self.button_explosive = tk.Button(self, text='Explosivo', width=20)        
        self.button_equipment = tk.Button(self, text='Equipos', width=20)

        # Enlazar funciones con teclado
        self.bind('<Control-r>', self.rock_database)
        self.button_rock.bind('<Return>', self.rock_database)

        
    def widgets_layout(self):
        '''Colocar los elementos gráficos de la ventana'''
        
        self.button_rock.pack(padx=10, pady=5)
        self.button_explosive.pack(padx=10, pady=5)
        self.button_equipment.pack(padx=10, pady=5)

    
    def rock_database(self, *event):
        win = RockDatabase(self)


if __name__ == '__main__':
    root = MainWindow()
    root.mainloop()
>>>>>>> 7132ddb5644a04514823ebd82408bc7298c545db
