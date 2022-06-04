
a = 200
b = 33
c = 500
if b>a:
    print("b es mayor que a")
elif b==a:
    print("b y a son iguales")
else:
    print("a es mayor que b")

# Forma corta
if a>b: print("a es mayor que b")

# Forma corta con if-else
print("a es mayor que b") if a>b else print("b es mayor que a")

#Forma operadores ternarios
print("a es mayor que b") if a>b else print("b es mayor que a") if b>a else print("a y b son iguales")

# Operadores lógicos
if a>b and c>a: print("ambas condiciones se cumplen")
if a>b or c>a: print("al menos una condicion se cumple")

# if anidados
z = 16

if z>10:
    print("Es mayor de 10 años")
    if z>18:
        print("y mayor de edad")
    else:
        print("pero menor de edad")
else:
    print("Es menor de 10 años.")

# las declaraciones no pueden estar vacias porque darían error, usamos pass
if a>b:
    pass
