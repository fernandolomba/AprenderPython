
import numpy as np

# Listas

# Las listas son mutables (podemos añadir, eleminar o modificar sus elementos).
# Contienen datos de tipo heterogeneos.


languages = ['Python', 'Java', 'Ruby', 'Javascript', 'Rust']
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13]
data = ['Tenerife', {'cielo': 'limpio', 'temp': 24}, 3718, (28.2933947, -16.5226597)]

# Convertir una cadena de texto a una lista con la función list()
print(list('Python'))

# Formas de crear una lista vacia
empty_list = []
print(list())

# Obtener elementos de una lista
# language[0:4:2] -> [star,stop,step]
print(languages[0])
print(languages[:3])
print(languages[-1])
print(languages[2:])
print(languages[0::2])
print(languages[::2])
print(languages[::-1])  # equivale a invertir la lista

# No pasa nada por usar límites invalidos porque Python los restringe a los límites de la lista
print(languages[-100:30])
print(languages[:30])
print(languages[-100:])

# Invertir lista conservando el orden inicial
print(languages[::-1])
print(list(reversed(languages)))
# Invertir lista modificando el orden original
languages.reverse()
print(languages)

# Añadir al final de la lista
lista1 = []
for i in range(20):
    if i % 2 == 0:
        lista1.append(i)
print(lista1)
lista1.insert(len(lista1), 20)
# Cuidado con esto porque añade la segunda lista como un dato de la primera lista
fibonacci.append(data)

# Añadir en una posición en concreto
lista2 = []
lista2.insert(1, 'Hola mundo')
lista2.insert(100, 'Adios mundo')  # No obtenemos error con los indices
lista2.insert(-11, 'hey wey')
lista2.insert(len(lista2), 20)
print(lista2)

# Repetir elementos
print(lista2 * 3)

# Unir 2 listas
print(lista1 + lista2)

lista1.extend(lista2)
print(lista1)

# Modificar un elemento de la lista
lista4 = ['agua', 'leche', 'zumo']
lista4[0] = 'leche de almendras'
print(lista4)
# Modificar un troceado de lista
lista4[0:2] = ['lima']
print(lista4)

print(list(lista4))

# Buscar y contar elementos de una lista
numbers = [0, 1, 1, 2, 2, 2, 3, 3, 3, 3]

counted = []
for element in numbers:
    if element not in counted:
        counted.append(element)
        print("El elemento {} aparece {} veces".format(element, numbers.count(element)))

# list.pop() elimina el último elemento de la lista

lista5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista5)
for i in range(5):
    print(lista5.pop())
    print(lista5)

print(lista5.pop(0))
print(lista5)

# list.remove() recibe un elemento por parámetro y lo elimina de la lista
lista5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista5)
lista5.remove(3)
print(lista5)

# list.reverse() devuelve la lista en orden inverso
lista5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(lista5[::-1])  # No hace un cambio permanente
print(lista5)
lista5.reverse()  # Realiza un cambio permanente
print(lista5)

# Ordenar de menor a mayor
# Ordenar de mayor a menor
print()
print('Ordenar de menor a mayor y de mayor a menor')
lista6 = [3, 5, 8, 9, 1, 4, 2, 6, 7]
print(lista6)
lista6.sort()
print(lista6)
lista6.reverse()
print(lista6)

print()
print('Ordenar de mayor a menor')
lista6 = [3, 5, 8, 9, 1, 4, 2, 6, 7]
print(lista6)
lista6.sort(reverse=True)
print(lista6)

# Convertir a listas
print('\n>>> Convertir a listas')
lista7 = list(range(0, 11, 2))
print(type(lista7))
print(lista7)

lista8 = list(['Fernando'])
lista8.append('Juan')
print(type(lista8))
print(lista8)



# Listas anidadas.
print('\n>>> Listas anidadas')
l = [["María", "Santos", "Fernández"],
     ["Juan", [1, 2, 3, 4, 5], 32],
     2]
print(l[0][2])  # Fernández
print(l[1][1][4])  # 5

# Matrices
print('\n>>>Matrices')
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz)
# puedes llamar como quieras a las variables
# porque la primera será la fila y la segunda la columna
for j in matriz:
    print(j)

for i in matriz:
    for j in i:
        print(j, end=" ")
    print("")
print()
for row in matriz:
    for element in row:
        print(element, end=" ")
    print()

# Matrices con numpy
print('\n>>> Matrices con numpy')



# Matriz vacia
A = np.empty((2,3))
print(A)
