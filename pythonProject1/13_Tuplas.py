# Tuplas
# Son heterogeneas
# Son inmutables. Una vez definidas no se pueden modificar.

tupla1 = ("juan", 32, True, [1, 2, 3, 4])
# No necesitamos los parentesis para definir la tupla
tupla2 = 'pepe', 'juan', 34, 59
# Podemos declarar tuplas con la funcion tuple()
tupla3 = tuple(('juan', 32, True))
tupla4 = tuple([1, 2, 3, 4, 5])
# tuplas de un solo elemento
tupla5 = ('pera', )
tupla6 = tuple('pera')
tipoStr = ('pera')

print(type(tupla5))
print(type(tupla6))
print(type(tipoStr))

print(tupla1[0])
print(tupla1[:3])
print(tupla1[-4:-2])

print(32 in tupla1)

# Las tuplas son inmutables
# produce un error
# tupla1[0]='pepe'
# Como solucion la podemos convertir en lista, modificarla y convertir en tupla
lista1 = list(tupla1)
lista1[0]='pepe'
tupla1 = tuple(lista1)
print(tupla1)
































