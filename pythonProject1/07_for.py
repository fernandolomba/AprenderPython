# Bucles for

# Muestra las letras de la palabra
word = 'Python'
for letter in word:
    print(letter)

# Hacemos que termine el bucle si encuentra una letra t
for letter in word:
    if letter == 't':
        break
    print(letter)

# Podemos recorrer un str
for i in word[:]:
    print(i)

#  range(star,stop, step)
#  range(star, stop)
#  range(stop)
for i in range(0, 10, 2):
    print(i)

for i in range(5, -1, -2):
    print(i)

# Si no necesitamos la variable i
# porque solo queremos repetir un numero de veces
# usamos _
for _ in range(10):
    print("No volvere a hablar en clase")

# Bucles anidados
for i in range(0, 10):
    print(f'''
    Tabla del {i}
    ''')
    for j in range(0, 10):
        print(f'{i} x {j} = {i * j}')
