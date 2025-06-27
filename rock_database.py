# Construcción de interfaces gráficas:
import tkinter as tk
<<<<<<< HEAD
from label_entry import LabelEntry
from tkinter import messagebox
=======
from tkinter.ttk import Treeview
from tkinter import messagebox

# Elementos gráficos personalizados:
from widgets.label_entry import LabelEntry

# Importar/exportar variables de Python:
import json

>>>>>>> 7132ddb5644a04514823ebd82408bc7298c545db

class RockDatabase(tk.Toplevel):
    '''Ventana para base de datos de la roca'''

    def __init__(self, parent):
        super().__init__(parent)

        # Configurar la ventana:
        self.title('Base de Datos - Roca')

<<<<<<< HEAD
        # crear variables de control
=======
        # Crear variables de la ventana:
>>>>>>> 7132ddb5644a04514823ebd82408bc7298c545db
        self.create_variables()

        # Crear y colocar elementos gráficos:
        self.create_widgets()
        self.widgets_layout()

<<<<<<< HEAD
    def create_variables(self): 
        ''' Esta funcion crea las variables de control de la ventana
        '''
        self.var_name = tk.StringVar()
        self.var_density = tk.DoubleVar(value=2.6)
        self.var_compres = tk.DoubleVar()
        self.var_tracc = tk.DoubleVar()
        self.var_young = tk.DoubleVar()
        self.var_poisson = tk.DoubleVar()







=======
        # Cargar base de datos:
        self.open_database('databases/rock_database.json')
    
    
    def create_variables(self):
        '''Crea las variables de control de la ventana'''

        # 1. Variable para la base de datos:
        self.database = {}

        # 2. Propiedades geológicas de la roca:
        self.var_name = tk.StringVar()
        self.var_density = tk.DoubleVar(value=2.6)
        self.var_compressive = tk.DoubleVar(value=100)
        self.var_tensile = tk.DoubleVar(value=15)
        self.var_young = tk.DoubleVar(value=70)
        self.var_poisson = tk.DoubleVar(value=0.21)
        self.var_velocity = tk.DoubleVar(value=3000)

        # 3. Condiciones geotécnicas:
        self.var_rmr = tk.DoubleVar(value=50)
        self.var_rqd = tk.DoubleVar(value=50)

    
>>>>>>> 7132ddb5644a04514823ebd82408bc7298c545db
    def create_widgets(self):
        '''Crear los elementos gráficos'''

        # 1. Crear el marco para la tabla:
<<<<<<< HEAD
        self.frame_table = tk.Frame(self)
        self.table_rocks = tk.Frame(self)
        # 2. Crear un marco para los parámetros:
        # self.frame_params = tk.Frame(self)
        self.frame_params = tk.LabelFrame(self, text = 'Propiedades geologicas:') #eso es un label frame
=======
        self.frame_table = tk.LabelFrame(self, text='Seleccionar roca:')
        self.table_rocks = Treeview(self.frame_table, columns=('name', 'density'))

        self.table_rocks.heading('name', text='Nombre')
        self.table_rocks.heading('density', text='Density')

        self.table_rocks.column('#0', width=0, stretch='no')
        self.table_rocks.column('name', width=150)
        self.table_rocks.column('density', width=70)

        self.table_rocks.bind('<Button-1>', self.complete_fields)

        # 2. Crear un marco para los parámetros:
        self.frame_params = tk.LabelFrame(self, text='Propiedades geológicas:')
>>>>>>> 7132ddb5644a04514823ebd82408bc7298c545db
        
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
<<<<<<< HEAD
            textvariable=self.var_compres
=======
            textvariable=self.var_compressive
>>>>>>> 7132ddb5644a04514823ebd82408bc7298c545db
        )

        self.entry_tensile = LabelEntry(
            self.frame_params,
            label='Resist. tracción',
            units='Mpa',
<<<<<<< HEAD
            textvariable=self.var_tracc
=======
            textvariable=self.var_tensile
>>>>>>> 7132ddb5644a04514823ebd82408bc7298c545db
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

<<<<<<< HEAD
        self.entry_velocity = LabelEntry
        self.frame_params
        # 3. Marco para los botones:
=======
        self.entry_velocity = LabelEntry(
            self.frame_params,
            label='Velocidad onda P',
            units='m/s',
            textvariable=self.var_velocity
        )

        # 3. Propiedades geotécnicas:
        self.frame_geot = tk.LabelFrame(self, text='Condiciones geotécnicas:')
        
        self.entry_rmr = LabelEntry(
            self.frame_geot,
            label='Rock Mass Rating',
            units='%',
            textvariable=self.var_rmr
        )

        self.entry_rqd = LabelEntry(
            self.frame_geot,
            label='Rock Quality Designation ',
            units='%',
            textvariable=self.var_rqd
        )

        # 4. Marco para los botones:
>>>>>>> 7132ddb5644a04514823ebd82408bc7298c545db
        self.frame_buttons = tk.Frame(self)

        self.button_add = tk.Button(
            self.frame_buttons,
            text='Añadir',
            command=self.add_rock
        )

        self.button_update = tk.Button(
            self.frame_buttons,
            text='Actualizar'
        )


    def widgets_layout(self):
        '''Colocar los elementos gráficos'''

        # 1. Crear el marco para la tabla:
<<<<<<< HEAD
        self.frame_table.pack(side='left', fill='both',padx=5, pady=5)
=======
        self.frame_table.pack(side='left', fill='both', padx=5, pady=5)
>>>>>>> 7132ddb5644a04514823ebd82408bc7298c545db
        self.table_rocks.pack(padx=5, pady=5)

        # 2. Crear un marco para los parámetros:
        self.frame_params.pack(fill='x', padx=5, pady=5)
        self.entry_name.grid()
        self.entry_density.grid()
        self.entry_compressive.grid()
        self.entry_tensile.grid()
        self.entry_young.grid()
        self.entry_poisson.grid()
<<<<<<< HEAD
        
        #Propiedades geotecnicas:
        self.frame_geot = tk.LabelFrame(self, text = 'Condiciones geotecnicas')
=======
        self.entry_velocity.grid()

        # 4. Propiedades geotécnicas:
        self.frame_geot.pack(fill='x', padx=5, pady=5)
        self.entry_rmr.grid()
        self.entry_rqd.grid()

>>>>>>> 7132ddb5644a04514823ebd82408bc7298c545db
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

<<<<<<< HEAD
        self.table_rocks



=======
    def valid_entries(self):
        '''
        Comprueba que se ingresan valores correctos. Por conveniencia,
        guardaremos todos los parámetros inmediantamente con un
        diccionario.

        Si los datos son válidos, me devuelve un diccionario con todos
        los valores. Si no son válidos, me devuelve un diccionario vacío.
        '''

        # Recuperar los parámetros de la roca:
        try:
            values = {
                'name': self.var_name.get(),
                'density': self.var_density.get(),
                'compressive': self.var_compressive.get(),
                'tensile': self.var_tensile.get(),
                'young': self.var_young.get(),
                'poisson': self.var_poisson.get(),
                'velocity': self.var_velocity.get(),
                'rmr': self.var_rmr.get(),
                'rqd': self.var_rqd.get()
            }
        except:
            messagebox.showerror(
                'Añadir roca',
                'Complete todos los campos con valores numéricos.'
            )
            return {}
        
        # Comprobar que todos los valores sean positivos:
        if values['density'] < 0:
            messagebox.showerror('Añadir roca', 'La densidad debe ser positiva.')   
            return {}
        
        if values['compressive'] < 0:
            messagebox.showerror('Añadir roca', 'La densidad debe ser positiva.')   
            return {}
        
        # SEGUIR COMPLETANDO...

        # Devolver el diccionario de valores:
        return values


    def add_rock(self):
        '''Añade una roca a la base de datos'''

        # Comprobar que definió un nombre válido:
        name = self.var_name.get()

        if name == '':
            messagebox.showerror('Añadir roca', 'Ingrese un nombre para la roca.')
            return
        
        if name in self.database.keys():
            messagebox.showerror('Añadir roca', 'El nombre ingresado ya existe.')
            return
        
        # Comprobar que los valores sean válidos:
        values = self.valid_entries()
        if not values:
            return
        
        # Añadir el nombre de la roca a la tabla:
        self.table_rocks.insert('', 'end', iid=name, values=(name, values['density']))

        # Añadir la roca a la base de datos:
        self.database[name] = values
        
        # Exportar el archivo de base de datos:
        with open('databases/rock_database.json', 'w') as output:
            json.dump(self.database, output, indent=4)


    def open_database(self, path):
        '''Abre una base de datos guardada'''
        
        # Cargar el archivo de la ruta indicada:
        try:
            with open(path, 'r') as infile:
                self.database = json.load(infile)
        except:
            return

        # Recuperar el nombre de los archivos:
        rocks = self.database.keys()

        # Añadir cada roca a la tabla:
        for name in rocks:
            density = self.database[name]['density']
            self.table_rocks.insert('', 'end', iid=name, values=(name, density))


    def complete_fields(self, event):
        '''Completa las entradas de texto para una roca seleccionada'''

        # Identificar la roca cliqueada:
        item = self.table_rocks.identify_row(event.y)

        # Ignorar si no se ha cliqueado un elemento:
        if item == '':
            return
        
        # Establecer los valores de las entradas:
        self.var_name.set(item)
        self.var_density.set(self.database[item]['density'])
        self.var_compressive.set(self.database[item]['compressive'])
        self.var_tensile.set(self.database[item]['tensile'])
        self.var_young.set(self.database[item]['young'])
        self.var_poisson.set(self.database[item]['poisson'])
        self.var_velocity.set(self.database[item]['velocity'])
        self.var_rmr.set(self.database[item]['rmr'])
        self.var_rqd.set(self.database[item]['rqd'])
>>>>>>> 7132ddb5644a04514823ebd82408bc7298c545db


if __name__ == '__main__':
    root = tk.Tk()
    win = RockDatabase(root)
    root.mainloop()
<<<<<<< HEAD

#EN EL PUNTO DONDE SE RECUPERAN LOS VALORES SE DEBEN METER LAS RESTRICCIONES 
#DEPURACION(DEBAGIN)
=======
>>>>>>> 7132ddb5644a04514823ebd82408bc7298c545db
