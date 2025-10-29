# #1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”

# edadUsuario = int(input('Ingrese su edad: '))

# if(edadUsuario >= 18):  
#     print('Es mayor de edad')


# # #2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

# notaUsuario = int(input('Ingrese la nota de su exámen: '))

# if(notaUsuario >= 6):
#     print('Aprobado')
# else: 
#     print('Desaprobado')

# # #3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

# numeroIngresado = int(input('Ingrese un número par: '))

# if(numeroIngresado % 2 == 0):
#     print('Ha ingresado un número par')
# else: 
#     print('Por favor, ingrese un número par')    

# #4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# # siguientes categorías pertenece:
# # ● Niño/a: menor de 12 años.
# # ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# # ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# # ● Adulto/a: mayor o igual que 30 años.

# edadUsuario = int(input('Ingrese su edad: '))

# if(edadUsuario < 12):
#     print('Niño/a')
# elif(edadUsuario >= 12 and edadUsuario < 18):
#     print('Adolescente')
# elif(edadUsuario >= 18 and edadUsuario < 30):
#     print('Adulto/a joven')
# elif(edadUsuario >= 30):
#     print('Adulto')

# #5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# # (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# # pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# # pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# # de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# # como una lista o un string.

# contrasena = input('Ingrese una nueva contraseña: ')

# if(8 <= len(contrasena) <= 14):
#     print("Ha ingresado una contraseña correcta")
# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# #6) escribir un programa que tome la lista
# # numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# # hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

# from statistics import mode, median, mean
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# media = mean(numeros_aleatorios)
# moda = mode(numeros_aleatorios)
# mediana = median(numeros_aleatorios)

# print(media)
# print(moda)
# print(mediana)

# if(media > mediana > moda):
#     print("Distribución con sesgo positivo (a la derecha)")
# elif(media < mediana < moda):
#     print("Distribución con sesgo negativo (a la izquierda)")
# elif(media == mediana == moda):
#     print("Distribución sin sesgo")

# #7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# # termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# # pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# # pantalla.

# textoIngresado = input('Ingrese una palabra o frase:')

# vocales = 'aeiou'

# ultimoCaracter = textoIngresado[-1]

# if(ultimoCaracter in vocales):
#     print(textoIngresado + '!')
# else: 
#     print(textoIngresado) 

# #8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# # dependiendo de la opción que desee:
# # 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# # 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# # 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# # El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# # usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# # lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# nombre = input('Ingrese su nombre: ')

# opcion = int(input('Ingrese el número de la opción deseada: \n1. Si quiere su nombre en mayúsculas. \n2. Si quiere su nombre en minúsculas. \n3. Si quiere su nombre con la primera letra mayúscula.\n'))

# if(opcion == 1):
#     print(nombre.upper())
# elif(opcion == 2):
#     print(nombre.lower())
# elif(opcion == 3):
#     print(nombre.title())    

# #9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# # magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# # por pantalla:
# # ● Menor que 3: "Muy leve" (imperceptible).
# # ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# # ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# # generalmente no causa daños).
# # ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# # débiles).
# # ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# # ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

# magnitud = float(input("Ingrese la magnitud del terremoto según la escala de Richter: "))

# if magnitud < 3:
#     print("Muy leve (imperceptible)")
# elif magnitud < 4:
#     print("Leve (ligeramente perceptible)")
# elif magnitud < 5:
#     print("Moderado (sentido por personas, pero generalmente no causa daños)")
# elif magnitud < 6:
#     print("Fuerte (puede causar daños en estructuras débiles)")
# elif magnitud < 7:
#     print("Muy Fuerte (puede causar daños significativos)")
# else:
#     print("Extremo (puede causar graves daños a gran escala)")

# #10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# # del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# # si el usuario se encuentra en otoño, invierno, primavera o verano.

# hemisferio = input('En que hemisferio se encuentra? N o S: ')
# mes = int(input('Ingrese el número de mes en el que se encuentra: '))
# dia = int(input('Ingrese el número de día en el que se encuentra: '))

# estacion = ''

# if(hemisferio == 'N'):
#     if(mes == 12 and dia >= 21) or (mes in (1, 2)) or (mes == 3 and dia <= 20):
#         estacion = 'Invierno'
#     elif (mes == 3 and dia >= 21) or (mes in (4, 5)) or (mes == 6 and dia <= 20):
#         estacion = "Primavera"
#     elif (mes == 6 and dia >= 21) or (mes in (7, 8)) or (mes == 9 and dia <= 20):
#         estacion = "Verano"
#     elif (mes == 9 and dia >= 21) or (mes in (10, 11)) or (mes == 12 and dia <= 20):
#         estacion = "Otoño"
# elif(hemisferio == 'S'):
#     if (mes == 12 and dia >= 21) or (mes in (1, 2)) or (mes == 3 and dia <= 20):
#         estacion = "Verano"
#     elif (mes == 3 and dia >= 21) or (mes in (4, 5)) or (mes == 6 and dia <= 20):
#         estacion = "Otoño"
#     elif (mes == 6 and dia >= 21) or (mes in (7, 8)) or (mes == 9 and dia <= 20):
#         estacion = "Invierno"
#     elif (mes == 9 and dia >= 21) or (mes in (10, 11)) or (mes == 12 and dia <= 20):
#         estacion = "Primavera"

# print(f'Según lo ingresado, estas en la estación {estacion}')

edad = int(input('ingrse e: '))

if(edad > 18):
    print('es mayor a 65')
else:
    print('asdasd')