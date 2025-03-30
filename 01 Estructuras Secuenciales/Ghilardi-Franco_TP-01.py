# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f...) para
# realizar la impresión por pantalla.
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f...) para realizar
# la impresión por pantalla.
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad= input("Ingrese su edad: ")
residencia= input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.
radio =int(input("Ingrese el radio de un circulo: "))
pi = 3.14
area = pi * radio **2
perimetro = 2 * pi * radio
print(f"El area del circulo es: {area}")
print(f"El perimetro del circulo es: {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 60
print(f"{segundos} segundos equivalen a {horas} horas!")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.
numero = int(input("Ingrese un numero: "))
print(f"{numero} x 1: {numero}")
print(f"{numero} x 2: {numero * 2}")
print(f"{numero} x 3: {numero * 3}")
print(f"{numero} x 4: {numero * 4}")
print(f"{numero} x 5: {numero * 5}")
print(f"{numero} x 6: {numero * 6}")
print(f"{numero} x 7: {numero * 7}")
print(f"{numero} x 8: {numero * 8}")
print(f"{numero} x 9: {numero * 9}")
print(f"{numero} x 10: {numero * 10}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
primer_numero=int(input("Ingrese el primer numero distinto de 0: "))
segundo_numero=int(input("Ingrese el segundo numero distinto de 0: "))
print(f"La suma de {primer_numero} y {segundo_numero} es: {primer_numero + segundo_numero}")
print(f"La division de {primer_numero} y {segundo_numero} es: {primer_numero / segundo_numero}")
print(f"La multiplicacion de {primer_numero} y {segundo_numero} es: {primer_numero * segundo_numero}")
print(f"La resta de {primer_numero} y {segundo_numero} es: {primer_numero - segundo_numero}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal.
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kg: "))
IMC = peso / altura**2
print(f"Su IMC es de: {IMC}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit.
temperaturaC = float(input("Ingrese una temperatura en grados Celcius: "))
temperaturaF= (9/5) * temperaturaC + 32
print(f"La temperatura en grados Fahrenheit es: {temperaturaF}")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.
primer_numero = int(input("Ingrese el primer numero: "))
segundo_numero = int(input("Ingrese el segundo numero: "))
tercer_numero = int(input("Ingrese el tercer numero: "))
promedio = (primer_numero + segundo_numero + tercer_numero) / 3
print(f"El promedio de {primer_numero}, {segundo_numero} y {tercer_numero} es: {promedio}")