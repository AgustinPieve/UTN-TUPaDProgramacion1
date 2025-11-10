#1

notas = [6, 8, 3, 7, 9, 10, 5, 4, 6, 1]

cantidad_notas = len(notas)

nota_mayor = notas[0]
nota_menor = notas[0]

promedio = 0

for i in range(cantidad_notas):
    promedio = promedio + notas[i]

    if notas[i] > nota_mayor:
        nota_mayor = notas[i]
    if notas[i] < nota_menor:
        nota_menor = notas[i]    

promedio = promedio / cantidad_notas

print(f'Las notas obtenidas son {notas}')
print(f'La mayor nota obtenida es {nota_mayor}')
print(f'La menor nota obtenida es {nota_menor}')
print(f'El promedio de todas las notas es {promedio}')

#2

productos = []

for i in range(5):
    producto = input('Ingrese un producto: ')
    productos.append(producto)

print(sorted(productos))

eliminar = input('Ingrese un producto a eliminar: ')

if eliminar in productos:
    productos.remove(eliminar)

print(productos)

#3

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

pares = []
impares = []

for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
    else: impares.append(numero)    

print(pares)
print(impares)

#4

datos = [1,3,5,3,7,1,9,5,3]

datos_nueva = []

for dato in datos:
    if dato not in datos_nueva:
        datos_nueva.append(dato)

print(datos)
print(datos_nueva)

#5

estudiantes = ['Juan', 'Pedro', 'Agus', 'Lucho', 'Gabi', 'Nacho', 'Dami', 'Santi']

print(estudiantes)

decision = input('Quiere eliminar o agregar un estudiante? \n .Agregar \n .Eliminar \n')

if decision == 'Eliminar':
    eliminar = input('Ingrese el estudiante a eliminar: ')
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
elif decision == 'Agregar':
    agregar = input('Ingrese el nombre del estudiante a agregar: ')
    estudiantes.append(agregar)

print(estudiantes)

#6

numeros = [1, 2, 3, 4, 5, 6, 7]

nuevo = [0] * len(numeros)  

for i in range(len(numeros)):
    nuevo[(i + 1) % len(numeros)] = numeros[i]

numeros = nuevo

print(numeros)

#7

temperaturas = [[12, 24], [14, 25], [10, 22], [11, 20], [13, 27], [9,  23], [15, 28]]

suma_min = 0
suma_max = 0

mayor_amplitud = 0
dia_mayor_amplitud = 0

for i in range(7):
    minima = temperaturas[i][0]
    maxima = temperaturas[i][1]
    
    suma_min += minima
    suma_max += maxima

    amplitud = maxima - minima
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = i + 1  

promedio_min = suma_min / 7
promedio_max = suma_max / 7

print("Promedio de temperaturas mínimas:", promedio_min)
print("Promedio de temperaturas máximas:", promedio_max)
print("La mayor amplitud térmica fue de", mayor_amplitud, "y ocurrió el día", dia_mayor_amplitud)

#8
notas = [
    [7, 8, 6],  
    [5, 9, 7],   
    [10, 6, 8], 
    [4, 5, 7],   
    [9, 8, 9]    
]

print('Promedios estudiantes: ')

for i in range(5):
    
    promedio = sum(notas[i]) / len(notas[i])
    print(f'Estudiante {i + 1}: {promedio}')
    
print('\nPromedio de cada materia: ')

for j in range(3):
    suma = 0
    for i in range(5):
        suma = suma + notas[i][j]
    promedio_mat = suma / 5
    print(f'Materia {j + 1}: {promedio_mat}')    
        
#9
tateti = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

print("TA-TE-TI")
for fila in range(len(tateti)):
    for columna in range(len(tateti[0])):
        print(tateti[fila][columna], end=' ')
    print()

for jugada in range(5):
    for jugador in range(2):

        if jugador == 0:
            fila, columna = int(input(f"jugador {jugador +1}º (X): Ingrese un numero para filas, presione enter y agregue otro para columna (1/2/3) ")), int(input()) # dos input para tomar ambas coordenadaas en una linea
            tateti[fila -1][columna -1] = "X"
            
            print("========================")
            for fila in range(len(tateti)):
                for columna in range(len(tateti[0])):
                    print(tateti[fila][columna], end=' ')
                print()
        
        if jugada == 4: # Para cortar la ultima jugada y no sobreescribir casillero
            break

        if jugador == 1:
            fila, columna = int(input(f"jugador {jugador +1}º (O): Ingrese un numero para filas, presione enter y agregue otro para columna (1/2/3) ")), int(input()) # dos input para tomar ambas coordenadaas en una linea
            tateti[fila - 1][columna - 1] = "O"
            
            print("========================")
            for fila in range(len(tateti)):
                for columna in range(len(tateti[0])):
                    print(tateti[fila][columna], end=' ')
                print()
        print()

print("Gracias por jugar!")

# 10

dia_mas_ventas = 0
producto_mas_vendido = 0

ventas = [[10, 20, 15, 26, 9, 20, 18], [5, 10, 9, 8, 11, 7, 12], [15, 10, 12, 14, 13, 11, 16], [10, 14, 9, 11, 10, 13, 17]]


for fila in range(len(ventas)):
    print(f"{fila + 1}º Producto")

    total_ventas = 0

    for columna in range(len(ventas[0])):
        print(ventas[fila][columna], end=' ')
        total_ventas += ventas[fila][columna]
    
    print(f"\nEl total vendido del articulo es: {total_ventas}")
    # registramos cual fue el producto mas vendido
    if total_ventas > producto_mas_vendido:
        producto_mas_vendido = total_ventas
        producto = fila +1
    
    print("====================")

# invierto el doble loop para sumar los datos de cada columna individualmente
for columna in range(len(ventas[0])):
    venta_dia = 0

    for fila in range(len(ventas)):
        venta_dia += ventas[fila][columna]

        if venta_dia > dia_mas_ventas:
            dia_mas_ventas = venta_dia
            num_dia = columna + 1

print(f"El producto mas vendido fue el {producto}º con {producto_mas_vendido} ventas.")
print(f"El día con mas ventas fue el {num_dia}º con {dia_mas_ventas} ventas.")
    
    



