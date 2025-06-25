# Lista de valores:
my_values = [2, 3, -1, 4, -2]

# Comprobar si alguno es negativo:
if any(value < 0 for value in my_values):
    print('Existe un valor negativo')
else:
    print('Todos los valores son positivos')


# Lista de valores:
my_values = [2, 3, 1, 4, 2]

# Comprobar si todos son positivos:
if all(value > 0 for value in my_values):
    print('Todos los valores son positivos')
else:
    print('Existe un valor negativo')