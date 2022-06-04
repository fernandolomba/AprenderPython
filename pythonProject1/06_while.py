#Bucle con continue
value = 0

while value <= 40:
    if (value % 2) == 0:
        value += 1
        continue
    else:
        print(value)
        value += 1

# Un bucle con break
contador =0
num = 1000
while num >=1:
    if num % 9 == 0:
        print(f'{num} es multiplo de 9')
        contador+=1
        if contador == 100:
            break
    num-=1
print(f'Hay {contador} multiplos de 9')

