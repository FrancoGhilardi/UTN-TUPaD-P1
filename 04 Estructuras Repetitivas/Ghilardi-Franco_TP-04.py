# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
num = int(input("Ingrese un numero: "))
contador = 0
if num == 0:
    contador = 1
else:
    while num > 0:
        num = num // 10
        contador += 1
print(f"El número tiene {contador} dígitos.")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))
suma = 0
if inicio > fin:
    inicio, fin = fin, inicio
for i in range(inicio + 1, fin):
    suma += i
print(f"La suma de los numeros entre {inicio} y {fin} es: {suma}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.
suma = 0
while True:
    numero = int(input("Ingrese un numero entero (0 para terminar): "))
    if numero == 0:
        break
    suma += numero
print(f"La suma total es: {suma}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
numero = random.randint(0,9)
intentos = 0
acertado = False
print("Adivina el numero entre 0 y 9")
while not acertado:
    intento = int(input("Ingresa tu numero: "))
    intentos += 1
    if intento == numero:
        acertado = True
        print(f"Correcto, el numero era {numero}")
    else:
        print("Incorrecto, intenta de nuevo")
print(f'El numero fue adivinado en {intentos} intento(s)')

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
for numero in range(100,-1,-1):
    if numero % 2 == 0:
        print(numero)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
numero = int(input("Ingrese un numero entero positivo: "))
suma = 0
if numero < 0:
    print("Ingrese un numero positivo")
else:
    for i in range(0,numero+1):
        suma += i
print(f"La suma entre 0 y {numero} es: {suma}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range(100):
    numero = int(input("Ingrese un numero entero: "))
    if numero % 2 == 0:
        pares +=1
    else:
        impares +=1
    if numero >= 0:
        positivos +=1
    else:
        negativos +=1
print(f'Cantidad de numeros pares {pares}')
print(f'Cantidad de numeros impares {impares}')
print(f'Cantidad de numeros positivos {positivos}')
print(f'Cantidad de numeros negativos {negativos}')

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
suma = 0
CANTIDAD = 5
for i in range (CANTIDAD):
    numero = int(input("Ingrese un numero entero: "))
    suma += numero
media = suma / CANTIDAD
print(f"La media de los {CANTIDAD} numeros ingresados es: {suma}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
numero = int(input("Ingrese un numero entero: "))
invertido = 0
while numero != 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero //= 10
if numero < 0:
    invertido *= -1
print(f"El numero invertido es: {invertido}")