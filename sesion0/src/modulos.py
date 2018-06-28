import csv
import json


class Persona(object):
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre.lower()
        self.apellido = apellido.lower()
        self.edad = int(edad)

def load_from_csv(archivo):
    personas = []
    with open(archivo) as f:
        nombres = csv.reader(f)
        for nombre in nombres:
            persona = Persona(nombre[0], nombre[1], nombre[2])
            personas.append(persona)
    return personas

def write_to_csv(personas, archivo):
    with open(archivo, "w") as f:
        nombres = csv.writer(f)
        for persona in personas:
            fila = [persona.nombre.upper(), persona.apellido.upper(), persona.edad]
            nombres.writerow(fila)

def load_from_json(archivo):
    personas = []
    with open(archivo) as f:
        nombres = json.load(f)
        for nombre in nombres:
            persona = Persona(nombre["nombre"], nombre["apellido"], nombre["edad"])
            personas.append(persona)
    return personas

def write_to_json(personas, archivo):
    with open(archivo, "w") as f:
        filas = []
        for persona in personas:
            fila = {"nombre": persona.nombre.upper(), "apellido": persona.apellido.upper(), "edad": persona.edad}
            filas.append(fila)
        json.dump(filas, f)
    


personas_csv = load_from_csv("nombres.csv")
write_to_csv(personas_csv, "nombres2.csv")
write_to_json(personas_csv, "nombres.json")
personas_json = load_from_json("nombres.json")


