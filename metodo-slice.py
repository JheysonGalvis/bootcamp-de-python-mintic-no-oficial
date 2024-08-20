a = [1,2,3,4,5]
b = a
print(a)
print(b)
del a[0]
print(id(a)) #id de la lista a
print(id(b)) #id de la lista b
#id de la lista b es igual a id de la lista a
c = a [:] #slice de la lista a la lista c
print(id(a))
print(id(b))
print(id(c)) # ya estamos accediendo a lugares diferentes en memoria
a.append(6)
print(a)
print(b)
print(c)
