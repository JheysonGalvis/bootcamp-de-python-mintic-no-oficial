#Nos devuelve la cantidad de elementos de la lista
lista = list([1992,14,3,True]) 
resultado = len(lista)
#Agregando un elemento a la lista
lista.append(4)
#agregando un elemento a la lista en una posicion especifica
lista.insert(2, False)
#agregando varios elementos a la lista
lista.extend([2011])
#eliminando un elemento de la lista (por su índice)
lista.pop(-1) #-1 para eliminar el último vaor, -2 para eliminar el anteultimo, y así sucesivamente
#Removiendo un elemento de la lista por su valor
lista.remove(4)
#Ordena los elementos de la lista mientras la lista tenga números y boleans
#lista.sort()
#invirtiendo los elementos de una lista
lista.reverse()
#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(1992)
print(elemento_encontrado)