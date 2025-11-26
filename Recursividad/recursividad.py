# Ejercicio 1

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


num = int(input("Ingrese un número para calcular su factorial.\n►"))
print(f"El factorial de {num} es: {factorial(num)}")

# Ejercicio 2
def fibonacci(pos):

    # 0 y 1 son los valores base de la serie de fibonacci
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)

print("Calcule el valor de la serie de Fibonacci en la posición")
pos = int(input("Ingrese la posición\n►"))

for i in range(pos):
    print(f"{i+1}º posición: {fibonacci(i+1)}")
    
# Ejercicio 3

def potencia(base, pot):
    if pot == 1:
        return base
    else:
        return base * potencia(base, pot - 1) # restamos de a 1 a la potencia en cada llamada y luego se multiplican las bases

base = int(input("Calculemos la Potencia de un numero base\nIngrese la base:"))
pot = int(input("Ingrese su potencia: "))

print(f"La potencia de {base} elevado a {pot} es: {potencia(base,pot)}")

# Ejercicio 4

def dec_bin(num):
    binario = ""
    if num == 0:
        return binario
    else:
        if num % 2 == 0: # sumamos por delante para que se vaya dando el numero invertido durante las llamadas
            binario = '0' + binario
        else:
            binario = '1' + binario

    return dec_bin(num//2) + binario


num = int(input("Ingrese un número decimal para calcular su equivalente en binario\n►"))

print(f"El binario de {num} es: {dec_bin(num)}")

# Ejercicio 5
# Aclaración: (No razone la coincidencia de las letras del principio y final, en este me apoye en el uso de IA)

def es_palindromo(palabra):
    # Si la palabra tiene 0 o 1 caracteres, es palíndromo
    if len(palabra) <= 1:
        return True
    
    # Si la primera y la última letra no coinciden, no es palíndromo
    if palabra[0] != palabra[-1]:
        return False
    
    # Evalua la palabra sin el primer y último carácter
    return es_palindromo(palabra[1:-1])

palabra = input("Ingrese un apalabra para ver si es Palíndromo\n").strip().lower()

if es_palindromo(palabra):
    print("Si es palíndromo")
else:
    print("No es palíndromo")
    
# Ejercicio 6

def  suma_digitos(n):
    if n == 0:
        return 0
    else:
        suma = n % 10 # vamos asignando a suma cada valor final y luego se sumaran cuando n llegue a 0
    
    return suma_digitos(n//10) + suma

n = int(input("Ingrese un valor entero para calcular la suma de sus dígitos: "))
print(f"La suma de los dígitos de {n} es: {suma_digitos(n)}")

# Ejercicio 7

def contar_bloques(n):
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n-1)

num = int(input("Ingrese la cantidad de bloques de base:"))
print(f"El total de bloques necesarios para armar la piramide es {contar_bloques(num)}")

# Ejercicio 8

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        contador = 0
        if digito == (numero % 10): # comprobamos cada ultimo digito
            contador += 1
    
    return contador + contar_digito(numero // 10, digito) # dejamos la parte entera


numero = int(input("Ingrese un número"))
digito = int(input("Ingrese el digito para contar cuantas veces este se repite en el número anterior\n►"))

print(f"El digito {digito}, se repite {contar_digito(numero, digito)} vez/ces en el número {numero}")