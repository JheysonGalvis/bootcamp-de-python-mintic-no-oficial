diccionario = {
    "nombre": "Jheyson",
    "apellidos": "Galvis",
    "telefono": 3167417556
}
#nos devuelve un objeto dict_item
claves = diccionario.keys()
#obteniendo un elemento con get () (si no encuentra nada el programa continua)
valor_de_kasdks = diccionario.get("kasdks")
#eliminando todo el diccionario
#diccionario.clear()
#eliminando un elemento del diccionario
diccionario.pop("apellidos")
#obteniendo un elemento del dict_items iterable
diccionario_iterable = diccionario.items()
print(diccionario)
print(diccionario_iterable) #iterar es recorrer el elemento