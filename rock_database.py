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
from tkinter import messagebox

class RockDatabase(tk.Toplevel):
    '''Ventana para base de datos de la roca'''

    def __init__(self, parent):
        super().__init__(parent)

        # Configurar la ventana:
        self.title('Base de Datos - Roca')

        # crear variables de control
        self.create_variables()

        # Crear y colocar elementos gráficos:
        self.create_widgets()
        self.widgets_layout()

    def create_variables(self): 
        ''' Esta funcion crea las variables de control de la ventana
        '''
        self.var_name = tk.StringVar()
        self.var_density = tk.DoubleVar(value=2.6)
        self.var_compres = tk.DoubleVar()
        self.var_tracc = tk.DoubleVar()
        self.var_young = tk.DoubleVar()
        self.var_poisson = tk.DoubleVar()







    def create_widgets(self):
        '''Crear los elementos gráficos'''

        # 1. Crear el marco para la tabla:
        self.frame_table = tk.Frame(self)
        self.table_rocks = tk.Frame(self)
        # 2. Crear un marco para los parámetros:
        # self.frame_params = tk.Frame(self)
        self.frame_params = tk.LabelFrame(self, text = 'Propiedades geologicas:') #eso es un label frame
        
        self.entry_name = LabelEntry(
            self.frame_params,
            label='Nombre de la roca',
            textvariable=self.var_name
        )

        self.entry_density = LabelEntry(
            self.frame_params,
            label='Densidad de roca',
            units='g/cm3',
            textvariable=self.var_density
        )

        self.entry_compressive = LabelEntry(
            self.frame_params,
            label='Resist. compresión',
            units='MPa',
            textvariable=self.var_compres
        )

        self.entry_tensile = LabelEntry(
            self.frame_params,
            label='Resist. tracción',
            units='Mpa',
            textvariable=self.var_tracc
        )

        self.entry_young = LabelEntry(
            self.frame_params,
            label='Módulo de Young',
            units='GPa',
            textvariable=self.var_young
        )

        self.entry_poisson = LabelEntry(
            self.frame_params,
            label='Razón de Poisson',
            textvariable=self.var_poisson
        )

        self.entry_velocity = LabelEntry
        self.frame_params
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
        self.frame_table.pack(side='left', fill='both',padx=5, pady=5)
        self.table_rocks.pack(padx=5, pady=5)

        # 2. Crear un marco para los parámetros:
        self.frame_params.pack()
        self.entry_name.grid()
        self.entry_density.grid()
        self.entry_compressive.grid()
        self.entry_tensile.grid()
        self.entry_young.grid()
        self.entry_poisson.grid()
        
        #Propiedades geotecnicas:
        self.frame_geot = tk.LabelFrame(self, text = 'Condiciones geotecnicas')
        # 3. Marco para los botones:
        self.frame_buttons.pack()
        self.button_add.pack(side='left', padx=10, pady=10)
        self.button_update.pack(side='left', padx=10, pady=10)

    def add_rock(self):
        '''Añade una roca a la base de datos'''
        #recuperar los parametros de la roca
        try:
            name =self.var_name.get()
            density = self.var_density.get()
            compress =self.var_compres.get() 
            tracc = self.var_tracc.get()
            young = self.var_young.get()
            poisson = self.var_poisson.get()
        except:
            messagebox.showerror(
                'Añadir roca',
                'Completa todos los campos con valores numericos'
            )
            return
        
        print('Resistencia a la compresiòn =', compress)

        self.table_rocks





if __name__ == '__main__':
    root = tk.Tk()
    win = RockDatabase(root)
    root.mainloop()

#EN EL PUNTO DONDE SE RECUPERAN LOS VALORES SE DEBEN METER LAS RESTRICCIONES 
#DEPURACION(DEBAGIN)