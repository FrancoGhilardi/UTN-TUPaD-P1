# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
limite = int(input("Ingrese un número entero mayor o igual a 1: "))
for i in range(1, limite + 1):
    print(f"Factorial de {i} es {factorial(i)}")

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
limite = int(input("Ingrese hasta qué posición desea ver la serie de Fibonacci: "))
print("Serie de Fibonacci:")
for i in range(limite + 1):
    print(fibonacci(i), end=" ")

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula n^m = n ∗ n(m−1). Prueba esta función en un algoritmo general.
def potencia(base, exponente):
    if exponente == 0:
        return 1 
    else:
        return base * potencia(base, exponente - 1)
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
resultado = potencia(base, exponente)
print(f"{base}^{exponente} = {resultado}")

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
numero = int(input("Ingrese un número entero positivo: "))
if numero == 0:
    print("0")
else:
    binario = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {binario}")
print(decimal_a_binario(int(input('Ingrese un numero entero: '))))

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# lo es.
# Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])
print(es_palindromo(input('Ingrese una palabra sin espacios ni tildes: ')))

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)
def suma_digitos(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)
print(suma_digitos(int(input('Ingrese un numero entero positivo: '))))

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.
# Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)
print(contar_bloques(int(input('Ingrese la cantidad de bloques del nivel mas bajo: '))))

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
# Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4
# contar_digito(123456, 7) → 0
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    resto = numero // 10
    if ultimo == digito:
        return 1 + contar_digito(resto, digito)
    else:
        return contar_digito(resto, digito)
num = int(input('Ingrese un numero entero positivo: '))
dig = int(input('Ingrese un digito entre 0 y 9: '))
print(contar_digito(num,dig))
