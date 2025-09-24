# Ejercicio 1

print('Hola mundo')

##################################################################

# Ejercicio 2

nombre = input('Ingrese su nombre: ')

print(f'Hola {nombre}!')

#################################################################

# Ejercicio 3

nombre = input('Ingrese su nombre: ')

apellido = input('Ingrese su apellido: ')

edad = int(input('Ingrese su edad: '))

residencia = input('Ingrese su pais de residencia: ')

print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}')

##################################################################

# Ejercicio 4

radio = int(input('Ingrese el radio del circulo: '))

pi = 3.1416

area = pi * radio ** 2

perimetro = 2 * pi * radio

print(f'El area del circulo es {area: 2f} y el perimetro es de {perimetro: 2f}')

# Ejercicio 5

segundos = int(input('Ingrese una cantidad de segundos: '))

horas = segundos / 3600

print(f'Los segundos ingresados equivaldrían a {horas} horas.')

# Ejercicio 6

numero = int(input('Ingrese un numero del 1 al 9: '))

print(f"Tabla de multiplicar del {numero}: ")
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

# Ejercicio 7

num1 = int(input('Ingrese un numero entero diferente a 0: '))

num2 = int(input('Ingrese otro numero entero diferente a 0: '))

suma = num1 + num2

resta = num1 - num2

multi = num1 * num2

division = num1 / num2

print(f'La suma de los numeros ingresados es {suma}.\n La resta de los numeros ingresados es {resta}.\n La multiplicación es {multi}.\n La division es {division}')


# Ejercicio 8

peso = float(input("Ingrese su peso en kilogramos: "))

altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura ** 2)

print(f'Su Índice de Masa Corporal (IMC) es: {imc:.2f}')


# Ejercicio 9

celsius = float(input("Ingrese la temperatura en grados Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius} °C equivalen a {fahrenheit:.2f} °F")


# Ejercicio 10

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

promedio = (num1 + num2 + num3) / 3

print(f"\nEl promedio de {num1}, {num2} y {num3} es: {promedio:.2f}")

a = 10
b = 3.0
c = a * b
d = a + b

print(f'c = {c}, d = {d}')