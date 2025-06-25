# Importar/exportar variables de Python:
import json

# Diccionario como base de datos:
database = {
    'Andesita': {
        'density': 2.6,
        'compressive': 100,
        'tensile': 15,
        'young': 70,
        'poisson': 0.21,
        'velocity': 3000
    },
    'Granito': {
        'density': 2.8,
        'compressive': 130,
        'tensile': 20,
        'young': 75,
        'poisson': 0.21,
        'velocity': 4000
    }
}

# Exportar la base de datos:
with open('tests/database.json', 'w') as outfile:
    json.dump(database, outfile, indent=4)

# Importar la base de datos:
with open('tests/database.json', 'r') as infile:
    database = json.load(infile)
print(database)
