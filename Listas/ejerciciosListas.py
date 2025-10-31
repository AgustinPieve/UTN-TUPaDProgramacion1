#1

# notas = [6, 8, 3, 7, 9, 10, 5, 4, 6, 1]

# cantidad_notas = len(notas)

# nota_mayor = notas[0]
# nota_menor = notas[0]

# promedio = 0

# for i in range(cantidad_notas):
#     promedio = promedio + notas[i]

#     if notas[i] > nota_mayor:
#         nota_mayor = notas[i]
#     if notas[i] < nota_menor:
#         nota_menor = notas[i]    

# promedio = promedio / cantidad_notas

# print(f'Las notas obtenidas son {notas}')
# print(f'La mayor nota obtenida es {nota_mayor}')
# print(f'La menor nota obtenida es {nota_menor}')
# print(f'El promedio de todas las notas es {promedio}')

#2

# productos = []

# for i in range(5):
#     producto = input('Ingrese un producto: ')
#     productos.append(producto)

# print(sorted(productos))

# eliminar = input('Ingrese un producto a eliminar: ')

# if eliminar in productos:
#     productos.remove(eliminar)

# print(productos)

#3

# lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# pares = []
# impares = []

# for numero in lista:
#     if numero % 2 == 0:
#         pares.append(numero)
#     else: impares.append(numero)    

# print(pares)
# print(impares)

#4

# datos = [1,3,5,3,7,1,9,5,3]

# datos_nueva = []

# for dato in datos:
#     if dato not in datos_nueva:
#         datos_nueva.append(dato)

# print(datos)
# print(datos_nueva)

#5

# estudiantes = ['Juan', 'Pedro', 'Agus', 'Lucho', 'Gabi', 'Nacho', 'Dami', 'Santi']

# print(estudiantes)

# decision = input('Quiere eliminar o agregar un estudiante? \n .Agregar \n .Eliminar \n')

# if decision == 'Eliminar':
#     eliminar = input('Ingrese el estudiante a eliminar: ')
#     if eliminar in estudiantes:
#         estudiantes.remove(eliminar)
# elif decision == 'Agregar':
#     agregar = input('Ingrese el nombre del estudiante a agregar: ')
#     estudiantes.append(agregar)

# print(estudiantes)

#6

lista = [2,5,6,7,3,8,9]


