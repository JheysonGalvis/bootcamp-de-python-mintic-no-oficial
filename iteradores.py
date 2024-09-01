# Ejemplo de cómo funcionan los iteradores en Python

# Crear una lista con algunos números
my_list = [1, 2, 3, 4]

# Obtener el iterador de la lista
# Un iterador es un objeto que nos permite recorrer una colección (como una lista) uno por uno.
my_iter = iter(my_list)

# Usar el iterador para acceder a los elementos de la lista
# La función next() nos da el siguiente elemento en la colección cada vez que se llama.
print(next(my_iter))  # Esto imprimirá el primer elemento de la lista: 1
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
#print(next(my_iter))
# Iterar en cadenas de texto usando un iterador
# Creando una cadena de texto
text = "Hola mundo"
# Creando un iterador para la cadena
# Un iterador nos permite recorrer cada carácter de la cadena uno por uno.
iter_text = iter(text)
# Iterar sobre cada carácter de la cadena usando un bucle for
for char in iter_text:
    print(char)  # Esto imprimirá cada carácter de la cadena en una nueva línea
# Crear un iterador para generar y recorrer números impares

# Definir un límite superior (sin incluir)
limit = 10

# Crear un iterador que genere números impares desde 1 hasta el límite
# range(1, limit+1, 2) genera números comenzando en 1, con saltos de 2, hasta llegar a 9 (el límite no se incluye).
odd_iter = iter(range(1, limit+1, 2))

# Usar el iterador para recorrer y mostrar cada número impar generado
for num in odd_iter:
    print(num)  # Imprime cada número impar en una nueva línea

# Definir una función generadora
def my_generator():
    # La palabra clave 'yield' permite devolver un valor y pausar la función en ese punto
    yield 1  # Primer valor que se devuelve cuando se llama a la función
    yield 2  # Segundo valor que se devuelve
    yield 3  # Tercer valor que se devuelve
# Usar un bucle 'for' para iterar sobre los valores generados
for value in my_generator():
    print(value)  # Imprime cada valor que la función generadora produce
#Fibonacci
#La serie de Fibonacci hace referencia a que vamos a obtener un valor sumando 
#los dos anteriores, en este caso, el resultado de 21 es igual a 8 + 13, el resultado de 1 
#es igual a 0 + 1, el resultado de 2 es igual a 1 + 1, etc.
# 0 1 1 2 3 5 8 13 21 ..
# Definir una función generadora para la secuencia de Fibonacci
def fibonacci(limit):
    # Inicializar los dos primeros números de la secuencia de Fibonacci
    a, b = 0, 1
    
    # Continuar generando números mientras 'a' sea menor que el límite
    while a < limit:
        yield a  # Devolver el valor actual de 'a' y pausar la ejecución de la función
        a, b = b, a + b  # Actualizar 'a' y 'b' para el siguiente número en la secuencia

# Usar un bucle 'for' para imprimir los números de la secuencia de Fibonacci hasta el límite
for num in fibonacci(10):
    print(num)  # Imprime cada número generado por la función
