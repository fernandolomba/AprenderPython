plus10 = lambda x: x+10
print(plus10(5))

producto = lambda x,y: x*y
print(producto(20,2))

discriminante = lambda a,b,c: b**2 - 4*a*c
print(discriminante(1,2,1))

nums = [49, 57, 62, 147, 2101, 22]
print(list(filter(lambda x: x%7==0, nums)))


# A filter se le puede pasar una lambda o una función
def tercera_letra_s(word):
    return word[2]=='s'

words = ["castaña", "astronomía", "masa", "bolígrafo", "mando", "tostada"]
print(list(filter(tercera_letra_s,words)))
print(list(filter(lambda x: x[2]=='s', words)))



# Reduce
from functools import reduce

nums = [1,2,3,4,5,6]
print(reduce(lambda x,y: x+y, nums))

def mayor_que(a, b):
    if a>b:
        return a
    else:
        return b
print(mayor_que(10,3))

nums = [-10, 5, 7, -3, 16, 60, 2, 33]
print(reduce(mayor_que, nums))


# map
words = ["zapato", "amigo", "yoyo", "barco", "xilófono", "césped"]
print(list(map(lambda x: len(x), words)))
print(reduce(mayor_que, map(lambda x: len(x), words)))

# sorted()







# Numeros equiprobables entre el 0 y el 100, diez numeros
from numpy import random
print(random.randint(0,101, size= 10))


























