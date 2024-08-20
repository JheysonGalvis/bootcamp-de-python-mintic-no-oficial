#El primer tipo de dato compuesto que veremos será la lista
lista = ["Jheyson Galvis", "tecnotutoriales Jheyson Galvis", True, 1.69]
#En el mundo de la programación no contamos del 1 al 10, contamos del 0 al 9
print(lista[1])
lista[3] = "Jheysonsaurio"
print(lista[3])

#La tupla es una lista que no se puede modificar
tupla = ("Jheyson Galvis", "tecnotutoriales Jheyson Galvis", True, 1.69)
#En el mundo de la programación no contamos del 1 al 10, contamos del 0 al 9
print(tupla[1])
#tupla[1] = "Tips TIC al paso"
#print(tupla[1])

#Creando un conjunto set
#Un conjunto no admite elementos duplicados
conjunto = {"Jheyson Galvis", "tecnotutoriales Jheyson Galvis", True, 1.69, "Jheyson Galvis"}
print(conjunto)

#Creando un diccionario
diccionario = {
    "nombre": "Jheyson Galvis",
    "canal de youtube": "tecnotutoriales Jheyson Galvis",
    "esta_feliz": True,
    "estatura": 1.69,
    "dato_duplicado": "Jheyson Galvis"
}
print(diccionario["nombre"]) #Diccionario muestra por el nombre asociado, es decir, muestrame lo que tienes en el valor nombre
print(diccionario["canal de youtube"])
print(diccionario["estatura"])
#La estructura del diccionario es clave:valor o en ingles key:value
print(diccionario["estatura"] + 2)
