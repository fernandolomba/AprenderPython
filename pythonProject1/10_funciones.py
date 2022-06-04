# Funciones


# Funcion sin parametros ni return
def mi_primera_funcion():
    print('Te saluda tu primera función')


mi_primera_funcion()


# Funcion con return sin parametros

def saluda():
    return "Hola"


print(saluda())


# Funcion con parametros sin return
def buenos_dias(name):
    print(f'Buenos dias {name}')


buenos_dias('Don pepito')
buenos_dias('Don Jose')


# Funcion con parametros y con return
def division(x, y):
    q = x // y
    r = x % y
    return q, r


print(division(x=41, y=7))
print(division(41, 7))
print(division(y=7, x=41))


# Ejemplo 1
def nombreCompleto(nombre, apellidos):
    print(f'El nombre completo es: {nombre} {apellidos}')
    return f'El nombre completo es: {nombre} {apellidos}'


print(nombreCompleto('Fernando', 'Lomba'))


# Número arbritario de argumentos
def sumaNumeros(*numeros):
    sum = 0
    for i in numeros:
        sum += i
    return sum


print(sumaNumeros(2, 3, 4, 5))
print(sumaNumeros(3, 5))


# Numero arbitrario de argumentos
def dime_nombre(nombre1, **apellidos1):
    print(f' Tu nombre es: {nombre1}', end= " ")
    for i in apellidos1.items():
        print(f'{i[1]}', end = " ")


dime_nombre(nombre1='fer', apellidos11='lomba',  apellidos12='prieto')






























