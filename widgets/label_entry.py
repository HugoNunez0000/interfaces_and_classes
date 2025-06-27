'''
En el siguiente código se crea un elemento gráfico (widget) personalizado
llamado "LabelEntry" y que consiste en una entrada de texto y etiquetas
para el nombre de la entrada y su unidad de medida.


TRABAJO PERSONAL: Si se da cuenta, la clase "LabelEntry" no es una entrada
de texto (Entry), es un marco (Frame) que contiene una entrada y  etiquetas.
Por lo tanto, no tiene ningún método llamado "get" que le permita recuperar
el contenido de la entrada de texto. Defina un método "get" que le permita
recuperar el contenido escrito dentro de la entrada de texto.
'''

import tkinter as tk


class LabelEntry(tk.Frame):
    '''Entrada de texto con etiquetas'''

<<<<<<< HEAD:label_entry.py
    def __init__(self, parent, label='', units='', label_width=20, textvariable=None):
=======
    def __init__(self, parent, label='', units='', label_width=20,
                 textvariable=None):
>>>>>>> 7132ddb5644a04514823ebd82408bc7298c545db:widgets/label_entry.py

        # Configurar el frame:
        super().__init__(parent)

        # Crear la etiqueta del nombre:
        self.label = tk.Label(self, text=label, width=label_width, anchor='w')
        self.label.grid(row=0, column=0, sticky='w')

        # Crear la entrada de texto:
<<<<<<< HEAD:label_entry.py
        self.entry = tk.Entry(self,textvariable=textvariable)
=======
        self.entry = tk.Entry(self, textvariable=textvariable)
>>>>>>> 7132ddb5644a04514823ebd82408bc7298c545db:widgets/label_entry.py
        self.entry.grid(row=0, column=1)

        # Crear la unidad de medida:
        self.units = tk.Label(self, text=units)
        self.units.grid(row=0, column=2)


    def grid(self, sticky='w', padx=10):
        '''sobreescribir función grid original'''
        super().grid(sticky=sticky, padx=padx)


    def get(self):
        '''Recupera el contenido de la entrada de texto'''
        return self.entry.get()

if __name__ == '__main__':
    
    # Ventana principal de la aplicación:
    root = tk.Tk()

    # Crear y colocar la entrada:
    entry = LabelEntry(root, label='Densidad de roca', units='g/cm3')
    entry.pack()

    # Ciclo de la ventana principal:
    root.mainloop()
    