import pandas as pd

import tkinter as tk

from tkinter import filedialog, messagebox

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.art3d import Poly3DCollection

df = None

puntajes = {

    'Cielo Abierto': 0,

    'Block Caving': 0,

    'Sublevel Stoping': 0,

    'Sublevel Caving': 0,

    'Longwall': 0,

    'Room and Pillar': 0,

    'Shrinkage': 0,

    'Cut and Fill': 0,

    'Top Slicing': 0,

    'Square Set': 0

}

metodos = list(puntajes.keys())

# Puntajes por categoría y opción

puntajes_dict = {

    'geometria': {

        'Masivo': [3, 4, 2, 3, -49, 0, 2, 0, 3, 0],

        'Tabular': [2, 2, 2, 4, 4, 4, 2, 4, 3, 2],

        'Irregular': [3, 0, 1, 1, -49, 2, 1, 2, 0, 4],

    },

    'potencia': {

        'Baja (0-10m)': [2, -49, 1, -49, 4, 4, 1, 4, -49, 4],

        'Intermedia (10-30m)': [3, 0, 2, 0, 0, 2, 2, 4, 0, 4],

        'Potente (30-100m)': [4, 2, 4, 4, -49, -49, 4, 0, 3, 1],

        'Muy potente (>100m)': [4, 4, 3, 4, -49, -49, 3, 0, 4, 1],

    },

    'inclinacion': {

        'Horizontal (0-20°)': [3, 3, 2, 1, 4, 4, 2, 0, 4, 2],

        'Intermedio (20-55°)': [3, 2, 1, 1, 0, 1, 1, 3, 1, 3],

        'Vertical (>55°)': [4, 4, 4, 4, -49, 0, 4, 4, 2, 3],

    },

    'leyes': {

        'Uniforme': [3, 4, 3, 4, 4, 3, 3, 3, 4, 3],

        'Gradual': [3, 2, 3, 2, 2, 3, 2, 3, 2, 3],

        'Errática': [3, 0, 1, 0, 0, 3, 1, 3, 0, 3],

    },

    'competencia_macizo': {

        'Baja (<2)': [3, 4, -49, 0, 4, 0, 1, 3, 2, 4],

        'Media (2-4)': [4, 1, 3, 3, 1, 3, 3, 2, 3, 1],

        'Alta (>4)': [4, 1, 4, 3, 0, 4, 4, 2, 3, 1],

    },

    'espaciado': {

        'Muy cercano (>16 ff/m)': [2, 4, 0, 0, 4, 0, 0, 3, 1, 4],

        'Cercano (10-16 ff/m)': [3, 4, 0, 2, 4, 1, 1, 3, 1, 4],

        'Espaciado (3-10 ff/m)': [4, 3, 1, 4, 0, 2, 3, 2, 2, 2],

        'Muy espaciado (<3 ff/m)': [4, 0, 4, 4, 0, 4, 4, 2, 4, 1],

    },

    'competencia_estructuras': {

        'Baja': [2, 4, 0, 0, 4, 0, 0, 3, 1, 4],

        'Media': [3, 3, 2, 2, 3, 2, 2, 3, 2, 3],

        'Alta': [1, 0, 4, 2, 0, 4, 4, 2, 4, 2],

    },

}


class MainWindow(tk.Tk):

    def __init__(self):

        super().__init__()

        self.window_variables()

        self.window_settings()

        self.create_menu()
        self.create_menu_separator()

        self.create_frames()

        self.show_welcome_message()

        self.selected_options = {}

    def window_variables(self):

        self.WIN_WIDTH = 1000

        self.WIN_HEIGHT = 600

    def window_settings(self):

        self.title("Metodología de Nicholas")

        self.geometry(f"{self.WIN_WIDTH}x{self.WIN_HEIGHT}")

        self.resizable(True, True)

    def create_menu(self):

        menu_bar = tk.Menu(self)

        archivo_menu = tk.Menu(menu_bar, tearoff=0)

        # Cambiado a self.open_file
        archivo_menu.add_command(label="Abrir archivo", command=self.open_file)

        archivo_menu.add_separator()

        archivo_menu.add_command(label="Salir", command=self.quit)

        menu_bar.add_cascade(label="Archivo", menu=archivo_menu)

        self.config(menu=menu_bar)

    def create_menu_separator(self):
        self.separator = tk.Frame(self, height=2, bg="gray")
        self.separator.pack(fill="x")

    def open_file(self):  # Método definido dentro de la clase

        global df
        try:
            ruta_archivo = filedialog.askopenfilename(title="Abrir archivo")

            if ruta_archivo:
                df = pd.read_csv(ruta_archivo, sep=';')
                self.after_read()  # Cambiado a self.after_read()
                messagebox.showinfo(
                    "Archivo cargado",
                    "Se ha cargado el archivo correctamente"
                )

        except:
            messagebox.showerror("Error de carga", "Ingrese un archivo .csv o .txt que represente un modelo de bloques")

    def create_frames(self):

        self.frame_izquierdo = tk.Frame(
            self, width=700, height=600, bg="white")

        self.frame_izquierdo.pack(side="left", fill="both", expand=True)

        # Marco para los parámetros de evaluación:
        self.frame_derecho = tk.Frame(self, width=300, height=600, bg="lightgray")
        self.frame_derecho.pack_propagate(False)
        self.frame_derecho.pack(side="right", fill="both", expand=False)
        
        self.frame_resultados = tk.Frame(self.frame_derecho, bg="lightgray")
        self.frame_resultados.pack(fill="both", expand=True)

    def show_welcome_message(self):

        self.label_bienvenida = tk.Label(

            self.frame_izquierdo,

            text="¡Bienvenido!",

            font=("Arial", 20, "bold"),

            bg="white",

            justify="center"

        )

        self.label_bienvenida.place(relx=0.5, rely=0.4, anchor="center")

        self.label_subtitulo = tk.Label(

            self.frame_izquierdo,

            text="Aquí podrás seleccionar el método de explotación según Nicholas",

            font=("Arial", 16, "bold"),

            bg="white",

            wraplength=600,

            justify="center"

        )

        self.label_subtitulo.place(relx=0.5, rely=0.5, anchor="center")

    def after_read(self):

        if df is None:

            messagebox.showerror("Error", "No se ha cargado ningún archivo")

            return

        # Eliminar el mensaje de bienvenida si existe

        if hasattr(self, 'label_bienvenida') and self.label_bienvenida.winfo_exists():

            self.label_bienvenida.destroy()

        # Limpiar cualquier gráfico anterior

        for widget in self.frame_izquierdo.winfo_children():

            widget.destroy()

        # Crear figura

        fig = plt.figure(figsize=(7, 6))

        ax = fig.add_subplot(111, projection='3d')

        df_plot = df.head(1000)

        # for _, row in df_plot.iterrows():

        xc, yc, zc = df['XC'], df['YC'], df['ZC']
        grade = df['CU']
        scatter = ax.scatter(xc, yc, zc, c=grade, marker='o')
           

           

           

        ax.set_xlabel('X')

        ax.set_ylabel('Y')

        ax.set_zlabel('Z')

        ax.set_title('Modelo de bloques 3D')

        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=self.frame_izquierdo)

        canvas.draw()

        canvas.get_tk_widget().pack(fill="both", expand=True)

        self.create_questionnaire()

    def create_questionnaire(self):

        for categoria, opciones in puntajes_dict.items():

            tk.Label(self.frame_derecho, text=categoria.upper(), bg='gray',
                     fg='white', font=('Arial', 10, 'bold')).pack(pady=5, fill='x')

            # Variable para almacenar la opción seleccionada
            selected_option = tk.StringVar(value="")

            for opcion in opciones:
                tk.Radiobutton(
                    self.frame_derecho,
                    text=opcion,
                    variable=selected_option,
                    bg='light gray',
                    value=opcion,
                    command=lambda c=categoria, v=selected_option: self.aplicar_puntaje(c, v)).pack(anchor='w')

            # Almacenar la opción seleccionada en el diccionario

            self.selected_options[categoria] = selected_option

        tk.Button(self.frame_derecho, text="Finalizar y ver resultados",

                  bg='green', fg='white', command=self.mostrar_resultados).pack(pady=20)

    def aplicar_puntaje(self, categoria, selected_option):

        opcion = selected_option.get()

        if categoria in puntajes_dict and opcion in puntajes_dict[categoria]:

            valores = puntajes_dict[categoria][opcion]

            for i, metodo in enumerate(metodos):

                if valores[i] != -49:

                    puntajes[metodo] += valores[i]

    def mostrar_resultados(self):

        resultados = "\n".join(
            [f"{metodo}: {pts} pts" for metodo, pts in puntajes.items()])

        # Limpiar el frame de resultados antes de mostrar

        for widget in self.frame_resultados.winfo_children():

            widget.destroy()

        tk.Label(self.frame_resultados, text="Resultados Totales",
                 font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(self.frame_resultados, text=resultados,
                 justify='left').pack(pady=5)

# Ejecutamos


if __name__ == "__main__":

    win = MainWindow()

    win.mainloop()