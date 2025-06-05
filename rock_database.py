'''
En el siguiente código tratamos de imitar el diseño mostrado en la imagen
"database_window.png" utilizando clases.

TRABAJO PERSONAL: Complete el diseño de esta ventana para que sea parecido
al diseño de la imagen. Debe añadir una tabla (Treeview) y separar las
entradas en parámetros geológicos y geotécnicos.

Recuerde que RockDatabase no es la ventana principal, es una ventana secundaria
(Toplevel). Tendrá que buscar una forma de abrir esta ventana secundaria en la
ventana principal que se encontrará en "main_window.py".
'''

import tkinter as tk
from label_entry import LabelEntry


class RockDatabase(tk.Toplevel):
    '''Ventana para base de datos de la roca'''

    def __init__(self, parent):
        super().__init__(parent)

        # Configurar la ventana:
        self.title('Base de Datos - Roca')

        # Crear y colocar elementos gráficos:
        self.create_widgets()
        self.widgets_layout()

    
    def create_widgets(self):
        '''Crear los elementos gráficos'''

        # 1. Crear el marco para la tabla:
        self.frame_table = tk.Frame(self)

        # 2. Crear un marco para los parámetros:
        self.frame_params = tk.Frame(self)
        
        self.entry_name = LabelEntry(
            self.frame_params,
            label='Nombre de la roca'
        )

        self.entry_density = LabelEntry(
            self.frame_params,
            label='Densidad de roca',
            units='g/cm3'
        )

        self.entry_compressive = LabelEntry(
            self.frame_params,
            label='Resist. compresión',
            units='MPa'
        )

        self.entry_tensile = LabelEntry(
            self.frame_params,
            label='Resist. tracción',
            units='Mpa'
        )

        self.entry_young = LabelEntry(
            self.frame_params,
            label='Módulo de Young',
            units='GPa'
        )

        self.entry_poisson = LabelEntry(
            self.frame_params,
            label='Razón de Poisson'
        )

        # 3. Marco para los botones:
        self.frame_buttons = tk.Frame(self)

        self.button_add = tk.Button(
            self.frame_buttons,
            text='Añadir'
        )

        self.button_update = tk.Button(
            self.frame_buttons,
            text='Actualizar'
        )


    def widgets_layout(self):
        '''Colocar los elementos gráficos'''

        # 1. Crear el marco para la tabla:
        self.frame_table.pack(side='left')

        # 2. Crear un marco para los parámetros:
        self.frame_params.pack()
        self.entry_name.grid()
        self.entry_density.grid()
        self.entry_compressive.grid()
        self.entry_tensile.grid()
        self.entry_young.grid()
        self.entry_poisson.grid()

        # 3. Marco para los botones:
        self.frame_buttons.pack()
        self.button_add.pack(side='left', padx=10, pady=10)
        self.button_update.pack(side='left', padx=10, pady=10)


root = tk.Tk()
win = RockDatabase(root)
root.mainloop()