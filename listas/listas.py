to_do = ["Dirigirnos al hotel",
         "ir a almorzar",
         "visitar un museo",
         "volver al hotel"] #la sintaxis de listas es []

print(to_do)
numbers = [1, 2, 3, 4, "cinco"]
print(numbers)
print(type(numbers)) #Python conoce a este tipo de dato como la clase list
mix = ["uno", 2, 3.14, True, [1,2,3]] #listas dentro de listas
print(mix) #imprime la lista mix de datos
print(len(mix))
print("Primer elemento:", mix[0]) # imprime el primer elemento de la lista mix
print("Segundo elemento:", mix[1])
print("Ultimo elemento:", mix[-1])
string = "Hola mundo"
print("Primer elemento:", string[0]) 
print("Segundo elemento:", string[1])
print("Ultimo elemento:", string[-1])
print(mix[2:-2]) #imprime desde el elemento 2 hasta el elemento -2
print(mix)
mix.append(False) #agrega un elemento a la lista mix
print(mix)
mix.append(["a","b"])
print(mix)
mix.insert(1,["a","b"])
print(mix)
print(mix.index(["a","b"])) #imprime el indice donde se encuentra el elemento ["a","b"]
numbers = [1, 2, 100, 90.45, 3, 4, 5]
print(numbers)
print("Mayor:", max(numbers))
print("Menor:", min(numbers))
del numbers [-1]
print(numbers)
del numbers [:2] #elimina desde el indice 0 hasta el indice 2 (2 no se incluye)
print(numbers)
del numbers
#print(numbers)
