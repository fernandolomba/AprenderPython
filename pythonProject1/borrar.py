
import pandas as pd

datos1 = {"x": [1, 2, 3, 4, 5], "y": [2, 4, 6, 8, 10], "z": [2, 3, 4, 5, 6]}

print('\nMostrar claves y valores de un diccionario')
print(datos1.keys())
print(datos1.values())

print('\nrecorrer un diccionario, solo claves')
for i in datos1:
    print(i)

print('\nrecorrer un diccionario, claves y valores')
for k,v in datos1.items():
    print(f'{k} : {v}')
    for i in v:
        print(i, end=' ')
    print('')

print('\nMostrar un elemento del diccionario')
print(datos1['x'])
print(datos1['x'][0])
print(datos1.get('x'))
print(datos1.setdefault('x')) # Muestra una columna. Similar a get

print('\nAñadir una entrada a un diccionario')
datos1['e'] = [1,3,5,7,9]
print(datos1.setdefault('d', [6, 7, 8, 9, 0])) # añade una entrada al dict


print('\nModificar una entrada de una diccionario')
datos1['x'] = [1,1,1,1,1]




df1 = pd.DataFrame(data=datos1)
print(df1)
df1 = pd.DataFrame(data=datos1, index=['ob1', 'ob2', 'ob3', 'ob4', 'ob5'])
print(df1)
df1 = pd.DataFrame(data=datos1, index=['ob1', 'ob2', 'ob3', 'ob4', 'ob5'], columns=['x', 'y'])
print(df1)