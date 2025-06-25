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