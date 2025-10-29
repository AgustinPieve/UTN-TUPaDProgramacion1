# #1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea

for i in range(101):
    print(i)

# #2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

numero = int(input('Ingrese un número entero: '))

cantidad_digitos = 0

for i in range(2):
    
    print(cantidad_digitos)

# #3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

num1 = int(input('Ingrese un numero entero: '))
num2 = int(input('Ingrese otro numero entero: '))

for i in range(num1 + 1, num2):
    print(i)

# #4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

numeros = 5
suma = 0

for cont in range(1, numeros + 1):
    print('Ingrese un numero: ', cont)
    num = int(input())
    suma = suma + num

print(suma)

# #5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

contador = 0

num_ingresado = int(input('Adivina el numero del 0 al 9: '))

while num_ingresado != 7:
    print('Incorrecto, ingresa otro número: ')
    num_ingresado = int(input())
    contador = contador + 1

print(f'Correcto, el número era {num_ingresado}! Tus intentos fueron {contador}')

# #6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for i in range(100, 0, -2):
    print(i)

# #7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

num_ingresado = int(input('Ingrese un número entero: '))

suma = 0

for i in range(0, num_ingresado):
    suma = suma + i + 1

print(suma)

# #8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

num_ingresados = 0

pares = 0
impares = 0
positivos = 0
negativos = 0

while num_ingresados < 5:
    print('Ingrese un número: ')
    num_actual = int(input())
    num_ingresados = num_ingresados + 1
    if num_actual > 0:
        positivos = positivos + 1
    else: negativos = negativos + 1
    if num_actual % 2 == 0:
        pares = pares + 1
    else: impares = impares + 1

print(f'Ha ingresado {pares} números pares')
print(f'Ha ingresado {impares} números impares')
print(f'Ha ingresado {positivos} números positivos')
print(f'Ha ingresado {negativos} números negativos')

# #9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

num_ingresados = 0

suma = 0

while num_ingresados < 5:
    print('Ingrese un número entero: ')
    num_actual = int(input())
    num_ingresados = num_ingresados + 1
    suma = suma + num_actual

media = suma / num_ingresados

print(f'La media entre los números ingresados es de {media}')

# #10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = int(input('Ingrese un número entero: '))

invertido = 0

cant_digitos = len(str(numero))

for i in range(cant_digitos):
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero = numero // 10

print(f'El número invertido es {invertido}')
