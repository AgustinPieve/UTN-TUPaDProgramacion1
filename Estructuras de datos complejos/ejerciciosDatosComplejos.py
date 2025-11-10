# Ejercicio 1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

for i, a in precios_frutas.items(): #.items() para que nos deje iterar
    print(f"● {i} = {a}")
    
# Ejercicio 2

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

# Articulos agregados en ejercicio 1
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Actualización de precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800


for i, a in precios_frutas.items():
    print(f"● {i} = {a}")
    
# Ejercicio 3

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

# Articulos agregados en ejercicio 1
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Actualización de precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800


lista_frutas = list(precios_frutas.keys()) # list() para convertir a lista, .keys() para obtener las keys de el diccionario

print(lista_frutas)

# Ejercicio 4

contactos = {} # Inicialización del diccionario

print("Registremos 5 nuevos contactos")

for i in range(1,6):
    nombre = input(f"Ingrese el nombre del {i}º Contacto:")
    numero = input(f"Ingrese el numero del {i}º Contacto:")
    
    contactos[nombre] = numero

consul = input("Ingrese el nombre del contacto que quisiera consultar su número")

if consul in contactos:
    print(f"El número de {consul} es: {contactos[consul]}")

else:
    print(f"{consul} no se encuentra dentro de su lista de contactos.")
    
# Ejercicio 5

dic_frase = {}

frase = input("Ingrese una frase: ")

lista_frase = frase.split() # .split() separa las palabras y las convierte en una lista

set_frase = set(lista_frase) # Pasamos lista a set

print(f"Palabras únicas: {set_frase}")


for i in set_frase: # uso el set para que no haya repetidos
    cantidad = lista_frase.count(i) # obtenemos la cantidad de veces que aparece cada palabra dentro de la lista con .count() y el i de recorrido por el set

    dic_frase[i] = cantidad # asignamos la cantidad en el diccionario usando el mismo i

print(f"Diccionario: {dic_frase}")

# Ejercicio 6

alumnos = {}

for i in range (1,4):
    nombre = input(f"Ingrese el nombre del {i}º estudiante: ")
    n1 = int(input("Ingrese la primera nota: "))
    n2 = int(input("Ingrese la segunda nota: "))
    n3 = int(input("Ingrese la tercera nota: "))

    alumnos[nombre] = (n1, n2, n3)

for i in alumnos.keys():
    promedio = sum(alumnos[i]) / 3 # sum() permite sumar lo que este dentro de la tupla
    print(f"El promedio de {i} es: {promedio}")
    
# Ejercicio 7

set_1 = {1, 3, 4, 5, 8, 9}
set_2 = {2, 3, 5, 7, 8, 9}

ambos = set_1 & set_2
uno = set_1 ^ set_2
total = set_1 | set_2

print(f"los que aprobaron ambos parciales: {ambos}")
print(f"los que aprobaron solo uno de los dos: {uno}")
print(f"lista total de estudiantes que aprobaron al menos un parcial: {total}")

# Ejercicio 8

productos = {'celular': 10, 'notebook': 5, 'teclado': 8}

consulta = input("Ingrese el nombre del producto que desee consultar stock: ").lower()

if consulta in productos.keys():
    print(f"El stock de {consulta} es: {productos[consulta]}")
    n_stock = int(input("Ingrese la cantidad de unidades que quiera agregar: "))
    productos[consulta] += n_stock

else:
    print(f"{consulta} no estaba en la lista.")
    n_stock = int(input("Ingrese la cantidad de unidades que quiera agregar: "))
    productos[consulta] = n_stock


print("la lista actualizada Producto-Stock\n===================================")
for i, a in productos.items():
    print(f"● {i} = {a}")
    
# Ejercicio 9

agenda = {('martes', '10:00'): "Clase Arquitectura", ('martes', '18:00'): "Clase Organización", ('miercoles', '15:00'): "Clase Programación", ('viernes', '16:00'): "Clase Matemática"}

dia = input("Ingrese el día que quiera consultar actividad: ")
hora = input("Ingrese la hora del día que consultó (en el siguiente formato = 00:00): ")

if (dia, hora) in agenda.keys(): # verificamos que la clave exista
    print(f"El {dia} a las {hora} usted tiene la siguiente tarea: {agenda[(dia, hora)]}") # si existe la llamamos para ver su valor usando agenda[(dia, hora)]
else:
    print("No tiene nada programado para esa hora ese día.")
    
# Ejercicio 10

invertido = {}

original = {'Argentina': 'Buenos Aires', 'Chile': 'Santiago', 'Uruguay': 'Montevideo'}
print(f"Original: {original}")
cant = len(original) # cantidad que usaremos para iterar

keys = list(original.keys())
values = list(original.values()) # Convertimos claves y valores a listas independientes

for i in range(cant):
    invertido[values[i]] = keys[i] # con el iterador asignamos a el dic. invertido los datos de value a keys y viceversa, armando el nuevo diccionario

print(f"Invertido: {invertido}")