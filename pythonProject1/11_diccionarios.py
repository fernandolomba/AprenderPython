# Diccionarios
# Los diccionarios tienen una clave y valor.
# Los diccionarios son heterogeneos y mutables

dic1 = {"Jose":32, "Marta":40, "Miguel":59}

print(dic1.keys())
print(dic1.values())

print(dic1['Jose'])
print(dic1.get('Jose'))

# Nos muestra la llave
for k in dic1:
    print(k)
# Aprovechamos la llave para mostrar el valor
for k in dic1:
    print(dic1[k])
# De una obtenemos la clave y el valor
for k,v in dic1.items():
    print(f'{k} : {v}')

# Un programita mas complejo
dic5 = {}
name = "fernando"
apellido = "lomba"
edad = 45
genero = "masculino"

print(dic5)
# ficha['nombre']: input("Introduce tu nombre: ")
# ficha['apellidos'] = input("Introduce tus apellidos: ")
# ficha['edad'] = int(input("Introduce tu edad: "))
# ficha['genero'] = 'masculino' if input("Tu genero f/m: ") == 'm' else 'femenino'

dic5["nombre"] = str(name)
dic5["apellidos"] = str(apellido)
dic5["edad"] = int(edad)
dic5["genero"] = str(genero)

for k,v in dic5.items():
    print(f'{k} : {v}')

# Diccionarios heterogeneos
dic2 = {'nombre': 'fer',
          'edad':45,
          'acceso':['user1', 'password']}

user = dic2['acceso'][0]
password = dic2['acceso'][1]
print(f'usuario: {user} \ncontraseña: {password}')

# list.copy() devuelve una copia de una lista
dic8_copia = dic2.copy()
print(dic8_copia)

# list.fromkeys()
# le pasamos un iterable y valor
# con el iterable crea las key y les asigna el valor
print('\n>>> list.fromkeys()')
dic3 = {}
dic3 = dict.fromkeys([1,2,3,4,5,6],['a'])
print(dic3)

# dic.setdefault()
# funciona con dic.setdefault(k)
print('\n>>> funciona con dic.setdefault(k)')
print(dic3.setdefault(1))
# sirve para añadir pares al diccionario dic.setdefault(k,v)
print('\n>>> sirve para añadir pares al diccionario dic.setdefault(k,v)')
dic3.setdefault('nombre','fer')
print(dic3)

# Hacer diccionarios con dict()
dic10 = dict(x=0, y=1, z=3)
print(dic10)

dic11 = dict([['x',1],['y',2],['z',3]])
print(dic11)

dic12 = dict({'x':1}, y=1, z=2)
print(dic12)


# A modo de resumen
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

