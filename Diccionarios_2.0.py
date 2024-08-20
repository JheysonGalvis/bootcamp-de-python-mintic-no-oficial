numbers = {1:"uno", 2:"dos", 3:"tres"} #creando un diccionario
print(numbers)
print(numbers[1]) #imprime el valor de la llave 1
print(numbers[2]) #imprime el valor de la llave 2
information = {"nombre": "Jheyson",
               "apellidos": "Galvis",
               "estatura": 1.69,
               "esta_feliz": True}
print(information)
del information["apellidos"]
print(information)
claves = information.keys()
print(claves)
#print(type(claves))
values = information.values()
print(values)
pairs = information.items()
print(pairs)
contacts = {"Jheyson": {"Apellido:": "Galvis",
                        "Altura:": 1.69,
                        "Edad": 29},
            "Aurelio": {"Apellido:":"Cheveroni",
                        "Altura:": 1.75,
                        "Edad": 30}}
print(contacts["Aurelio"])