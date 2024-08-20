import numpy as np
#Definamos números aleatorios del 1 al 20 en un vector
arr = np.random.randint(1, 20, 10)
print(arr)
#Ahora lo llevaremos a una estructura matricial
matriz = arr.reshape(2, 5)
print(matriz)
#Con max voy a traer el número más grande que tenga nuestro arr
maximo = arr.max()
print(maximo)
maximo = matriz.max()
print(maximo)
#Crearemos un array de dos dimensiones:
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
#¿Qué pasa cuando quieres unir el array b con el array a?
#Con el comando concatenate se hará la union de ambos arrays por el eje 0 axis
c = np.concatenate((a, b), axis=0)
print(c)
