# Dataframes con pandas

import pandas as pd

# Consultar resumen de 11_diccionarios.py
# DF a partir de un diccionario con listas
datos1 = {"x": [1, 2, 3, 4, 5], "y": [2, 4, 6, 8, 10], "z": [2, 3, 4, 5, 6]}
df1 = pd.DataFrame(data=datos1)
print(df1)
df1 = pd.DataFrame(data=datos1, index=['obs1', 'obs2', 'obs3', 'obs4', 'obs5'])
print(df1)
# Con diccionarios columns sirve para seleccionar columnas
df3 = pd.DataFrame(data=datos1, columns=["x", "z"])
print(df3)
df3 = pd.DataFrame(data=datos1, columns=["x", "z", 'd'])
print(df3)
# Hacer un df con .from_dict() NOS PERMITE PASAR COLUMNAS A FILAS
d = {"a": [1, 2, 3],
     "b": [4, 5, 6],
     "b1": [7, 8, 9]}

df = pd.DataFrame.from_dict(d)
print(df)
df = pd.DataFrame.from_dict(d, orient="index", columns=['A', 'B', 'C'])
print(df)

# DF a partir de una lista de listas
datos2 = [[1, 2, 2], [2, 4, 3], [3, 6, 4], [4, 8, 5], [5, 10, 6]]
df2 = pd.DataFrame(data=datos2)
print(df2)
df2 = pd.DataFrame(data=datos2, columns=["x", "y", "z"])
print(df2)
# Con listas columns sirve para darle nombre a las columnas
df2 = pd.DataFrame(data=datos2, columns=["x", "y", "z"], index=['obs1', 'obs2', 'obs3', 'obs4', 'obs5'])
print(df2)

# DF a partir de una Lista de diccionarios
data = [{"x": 1, "y": 2},
        {"x": 2, "y": 4},
        {"x": 3, "y": 6},
        {"x": 4, "y": 8},
        {"x": 5, "y": 10}]
df4 = pd.DataFrame(data=data)
print(df4)

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

datos3 = zip(x, y)
print(datos3)
datos3 = list(zip(x, y))
print(datos3)

a, b = zip(*datos3)

print(list(a))
print(type(a))
print(b)
print(list(zip(a, b)))
df5 = pd.DataFrame(datos3, columns=['x', 'y'])
print(df5)

# https://ellibrodepython.com/list-comprehension-python

# Tamaño del dataframe
print(df5.shape)
print('numero de filas:', df5.shape[0])
print('numero de columnas:', df5.shape[1])

# Dado un dataframe, podemos seleccionar una columna en particular de diversas formas:
#
# Indicando el nombre de la columna entre claudators, []
# Con el método .columns[]
# Con el método .loc[] (por nombre o etiqueta)
# Con el método .iloc[] (por posición)

fdata = {"Name": ["Alicia", "Bill", "Carlos", "Diana"],
         "Age": [22, 28, 19, 34],
         "Pet": [True, False, False, True],
         "Height": [157, 190, 175, 164],
         "Birthday": ["Mayo", "Junio", "Agosto", "Diciembre"]}
df = pd.DataFrame(data=fdata, index=["obs1", "obs2", "obs3", "obs4"])
print(df)


#MOSTRAR UN DF POR COLUMNAS
print('\n\n>>> Mostrar un df por columnas\n')

print(df['Birthday'])
print(df['Age':'Birthday']) # Este no funciona
print(df[['Birthday', 'Age']])

print(df[df.columns[4]])
print(df[df.columns[0:2]])
print(df[df.columns[[0, 2, 3]]])

print(df.loc[:, "Birthday"])
print(df.loc[:, "Age":"Birthday"])
print(df.loc[:, ["Birthday", "Age"]])

print(df.iloc[:, 4])
print(df.iloc[:, -1])
print(df.iloc[:, 0:2])
print(df.iloc[:, [0, 3, 2]])

#MOSTRAR UN DF POR FILAS
# Dado un dataframe, podemos seleccionar una fila en particular de diversas formas:
#
# Con el método .loc[] (por nombre o etiqueta)
# Con el método .iloc[] (por posición)

print('\n\n>>> Mostrar un df por filas\n')

print(df.loc["obs1"])  # Seleccionamos la primera observación (obs1) con el método .loc[]
print(df.loc[["obs2", "obs3"]])  # Seleccionamos la segunda y tercera observación con el método .loc[]
print(df.loc["obs2":"obs3"])  # Seleccionamos un rango


print(df.iloc[-1])  # Seleccionamos la última observación con el método .iloc[]
print(df.iloc[1:3])
#
# Filas y columnas
# Para seleccionar un elemento en concreto, hay que indicar la fila y la columna y lo podemos hacer de dos formas:
#
# Con el método .loc[] (por nombre o etiqueta)
# Con el método .iloc[] (por índice)

print(df.loc["obs2", "Age"])
print(df.loc["obs2":"obs3", ["Name", "Birthday"]])

print(df.iloc[1, 1])
print(df.iloc[1:3, [0, 4]])
