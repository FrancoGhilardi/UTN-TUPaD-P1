# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print("Diccionario actualizado de precios de frutas:")
for fruta, precio in precios_frutas.items():
    print(f"{fruta}: ${precio}")

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1500,
    'Pera': 2300
}
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print("Diccionario con precios actualizados:")
for fruta, precio in precios_frutas.items():
    print(f"{fruta}: ${precio}")

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.
precios_frutas = {
    'Banana': 1330,
    'Ananá': 2500,
    'Melón': 2800,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1700,
    'Pera': 2300
}
lista_frutas = list(precios_frutas.keys())
print(f"Lista de frutas: {lista_frutas}")

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.
# Ejemplo:
# contactos = {"Juan":"123456", "Ana":"987654"}
# Consultar: "Juan" -> muestra "123456"
contactos = {}
print("Cargá 5 contactos:")
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    numero = input(f"Ingresá el número de {nombre}: ")
    contactos[nombre] = numero
consulta = input("\n¿A qué contacto querés consultar? Ingresá el nombre: ")
if consulta in contactos:
    print(f"El número de {consulta} es: {contactos[consulta]}")
else:
    print(f"No se encontró el contacto '{consulta}'.")

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.
# Ejemplo:
# Entrada -> "hola mundo hola"
# Salida:
# Palabras_unicas: {'hola','mundo'}
# Recuento: {'hola': 2, 'mundo':1}
frase = input("Ingresá una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1
print("\nPalabras únicas:", palabras_unicas)
print("Recuento de palabras:", recuento)

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.
# Ejemplo:
# alumnos = {"Sofia": (10,9,8),"Luis":(6,7,7)}
alumnos = {}
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    print(f"Ingresá las 3 notas de {nombre} separadas por espacio:")
    notas = tuple(map(int, input().split()))
    while len(notas) != 3:
        print("Debe ingresar exactamente 3 notas. Intentalo de nuevo:")
        notas = tuple(map(int, input().split()))
    alumnos[nombre] = notas
print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / 3
    print(f"{nombre}: promedio = {promedio:.2f}")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
parcial1 = {"Ana", "Luis", "Sofía", "Marcos", "Pedro"}
parcial2 = {"Sofía", "Pedro", "Camila", "Luis", "Valentina"}
ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2
print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno de los dos:", solo_uno)
print("Aprobaron al menos un parcial:", al_menos_uno)

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.
productos = {
    "Manzana": 50,
    "Banana": 30,
    "Leche": 20
}
def mostrar_menu():
    print("\nOpciones:")
    print("1 - Consultar stock de un producto")
    print("2 - Agregar unidades a un producto existente")
    print("3 - Agregar un nuevo producto")
    print("4 - Salir")
while True:
    mostrar_menu()
    opcion = input("Elegí una opción: ")
    if opcion == "1":
        prod = input("Ingresá el nombre del producto para consultar: ")
        if prod in productos:
            print(f"Stock de {prod}: {productos[prod]} unidades")
        else:
            print(f"El producto '{prod}' no existe en el inventario.")
    elif opcion == "2":
        prod = input("Ingresá el nombre del producto para agregar unidades: ")
        if prod in productos:
            try:
                unidades = int(input("Cantidad a agregar: "))
                if unidades > 0:
                    productos[prod] += unidades
                    print(f"Nuevo stock de {prod}: {productos[prod]} unidades")
                else:
                    print("Ingresá un número positivo.")
            except ValueError:
                print("Por favor, ingresá un número válido.")
        else:
            print(f"El producto '{prod}' no existe en el inventario.")
    elif opcion == "3":
        prod = input("Ingresá el nombre del nuevo producto: ")
        if prod in productos:
            print(f"El producto '{prod}' ya existe con stock {productos[prod]}.")
        else:
            try:
                stock = int(input("Ingresá el stock inicial: "))
                if stock >= 0:
                    productos[prod] = stock
                    print(f"Producto '{prod}' agregado con stock {stock}.")
                else:
                    print("El stock debe ser un número cero o positivo.")
            except ValueError:
                print("Por favor, ingresá un número válido.")
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Probá de nuevo.")

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Ejemplo:
# agenda = {("lunes","10:00"): "Reunion", ("martes","15:00"):"Clase de ingles"}
# Permití consultar qué actividad hay en cierto día y hora.
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "09:00"): "Entrega de proyecto",
    ("viernes", "18:30"): "Cena con amigos"
}
dia = input("Ingresá el día (por ejemplo, lunes): ").lower()
hora = input("Ingresá la hora (formato HH:MM, por ejemplo 10:00): ")
evento = agenda.get((dia, hora))
if evento:
    print(f"El {dia.capitalize()} a las {hora} tenés: {evento}")
else:
    print(f"No hay ningún evento registrado el {dia} a las {hora}.")

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.
# Ejemplo:
# original = {"Argentina":"Buenos Aires", "Chile":"Santiago"}
# invertido = {"Buenos Aires":"Argentina", "Santiago": "Chile"}
original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia",
    "Uruguay": "Montevideo"
}
invertido = {capital: pais for pais, capital in original.items()}
print(f"Diccionario invertido: {invertido}")