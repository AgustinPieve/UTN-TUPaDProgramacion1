# Ejercicio 1

def imprimir_hola_mundo():
    print ("Hola Mundo!")

# Programa principal
imprimir_hola_mundo()

# Ejercicio 2

def saludar_usuario(nombre):
    print (f"Hola {nombre}!")

# Programa principal
nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Programa Principal
print("Bienvenido, por favor complete los siguientes datos.")
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

# Ejercicio 4

import math # Para poder usar pi

def calcular_area_circulo(radio):
    area = math.pi * (radio**2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

# Programa principal
radio = float(input("Ingrese el radio de un circulo para calcular su area y su perimetro: "))

#(:.2f) es una alternativa para mostrar los decimales que queramos, esta nos deja personalizar y mostrar el decimal exacto, otra puede ser round (redondea los decimales)
print(f"El area es de {calcular_area_circulo(radio):.2f} y su perimetro es de {calcular_perimetro_circulo(radio):.2f}") 

# Ejercicio 5

def segundos_a_horas(segundos):
    horas = segundos/3600
    return horas

# Programa principal
segundos = int(input("Ingrese la cantidad de segundos para pasar a horas: "))

print(f"{segundos} es equivalente a {segundos_a_horas(segundos):.2f} hora/s")

def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{i} X {numero} = {i * numero}")

# Programa principal
numero = int(input("Ingrese un numero el cual quiera ver su tabla de multiplicar: "))

tabla_multiplicar(numero)

# Ejercicio 7

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = None # None con N mayuscula

    return (suma, resta, multiplicacion, division)

# Programa principal
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

# descomprimir tupla
suma, resta, multiplicacion, division = operaciones_basicas(a, b)
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
if division != None:
    print(f"división: {division}") 
else:
    print("No se puede dividi por cero.")
    
# Ejercicio 8

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc


# Programa principal    
print("Calculemos su IMC")
peso = int(input("Ingrese su peso(Kg): "))
altura = float(input("Ingrese su altura(m): "))

print(f"Su indice de masa corporal es: {calcular_imc(peso, altura):.2f}")

# Ejercicio 9

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32 # Formula para calcular cel a far
    return fahrenheit

# Programa principal
celsius = float(input("Ingrese una temperatura en °C para convertirla a °F"))
print(f"{celsius}°C es igual a {celsius_a_fahrenheit(celsius)}°F")

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

# Programa principal
print("Ingrese 3 numeros para calcular su promedio")
a = float(input("Ingrese el primero: "))
b = float(input("Ingrese el segundoo: "))
c = float(input("Ingrese el tercero: "))

print(f"El promedio de {a, b ,c} es {calcular_promedio(a, b ,c)}")