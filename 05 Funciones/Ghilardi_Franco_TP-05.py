# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.
def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de-
# volver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")
name = input("Ingrese un nombre: ")
saludar_usuario(name)

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe-
# dir los datos al usuario y llamar a esta función con los valores in-
# gresados.
def informacion_personal(nombre,apellido,edad,residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
name=input("Ingrese el nombre: ")
lastname=input("Ingrese el apellido: ")
age=input("Ingrese la edad: ")
county=input("Ingrese la residencia: ")
informacion_personal(name,lastname,age,county)

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra-
# dio como parámetro y devuelva el área del círculo. calcular_peri-
# metro_circulo(radio) que reciba el radio como parámetro y devuel-
# va el perímetro del círculo. Solicitar el radio al usuario y llamar am-
# bas funciones para mostrar los resultados.
import math
def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    print(f"El area del circulo es {area}")
def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    print(f"El perimetro del circulo es {perimetro}")
radio = int(input("Ingrese el radio del circulo: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mos-
# trar el resultado usando esta función.
def segundos_a_horas(segundos):
    horas = segundos / 3600
    print(f"{segundos} segundos equivalen a {horas} horas.")
segundos = int(input("Ingrese los segundos: "))
segundos_a_horas(segundos)

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la fun-
# ción.
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
numero = int(input("Ingrese un numero para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resulta-
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re-
# sultados de forma clara.
def operaciones_basicas(a, b):
    print("\nResultados de las operaciones:")
    print(f"Suma: {a + b}")
    print(f"Resta: {a - b}")
    print(f"Multiplicación: {a * b}")
    if b != 0:
        print(f"Division: {a / b}")
    else:
        print("No se puede dividir por 0")
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
operaciones_basicas(a , b)

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun-
# ción para mostrar el resultado con dos decimales.
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    print(f"Tu IMC es: {imc}")
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
calcular_imc(peso,altura)

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius} °C equivalen a {fahrenheit} °F")
grados = float(input("Ingrese la temperatura en grados celsus: "))
celsius_a_fahrenheit(grados)

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f"El promedio es {promedio}")
a = float(input("Ingeese el primer numero: "))
b = float(input("Ingeese el segundo numero: "))
c = float(input("Ingeese el tercer numero: "))
calcular_promedio(a,b,c)