import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd

model = pd.read_csv('marvin.blocks', sep=' ')
model = model[model['cu'] > 0.2]

# Datos aleatorios de ejemplo
x = model['XC']
y = model['YC']
z = model['ZC']
g = model['cu']

# Crear la figura y el eje 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Crear el scatter 3D
scatter = ax.scatter(x, y, z, c=g, marker='o')

# Etiquetas
ax.set_title('Gráfico de Dispersión 3D')
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

# Mostrar el gráfico
plt.show()