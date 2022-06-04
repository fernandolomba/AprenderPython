# Necesitamos la version 3.10 para poder usar el match

color = 'azul'
match color:
    case 'azul':
        print('El color es azul')
    case 'rojo':
        print('El color es rojo')
    case 'verde':
        print('El color es verde')


color = 1
match color:
    case 1:
        print('El color es azul')
    case 2:
        print('El color es rojo')
    case 3:
        print('El color es verde')

point = ('8',2)

match point:
    case (x, y):
        print(f'({x},{y}) está en el plano')
        print(f'{point} está en el plano')
    case (x, y, z):
        print(f'({x}{y}{z}) está en el espacio')

match point:
    case (int(), int()):
        print(f'{point} está en el plano')
    case (str(), int()):
        print(f'{point} no es un punto')
    case (int(), int(), int()):
        print(f'{point} está en el espacio')
    case _:
        print('Me da los mismo lo que sea')

age = 20

match age:
    case 0 | None:
        print('No es una persona')
    case age if age < 17:
        print('Eres menor')
    case n if n < 21:
        print('En US no puedes')
    case _:
        print('A emborracharse!!!')
