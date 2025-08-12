# ejercicios con condicionales y operaciones matematicas

# 1. verifica si un numero es positivo, negativo o cero

numero = int(input("ingresa un numero: "))
if numero > 0:
    print("el numero es positivo")
elif numero < 0:
    print("el numero es negativo")
else:
    print("el numero es cero")

# 2. calcula el mayor de dos numeros ingresados

num = int(input("ingresa un numero: "))             
num1 = int(input("ingresa un numero: "))
if num >= num1:
    print(f"{num} es mayor que {num1}")
elif num1 >= num:
    print(f"{num1} es mayor que {num}")
else:
    print("no hay ningun numero ingresado")

# 3. determina si un numero es par o impar

num2 = int(input("ingresa un numero: "))
if num2 % 2 == 0:
    print("el numero es par")
else:("el numero es impar")

# 4. dado un numero verifica si esta entre 10 y 20

num3 = int(input("ingresa un numero: "))
if num3 >= 10 and num3 <= 20:
    print("el numero esta entre 10 y 20")
else:
    print("el numero no esta entre 10 y 20")

# 5. dados tres numeros encuentra el mayor usando condicionales

num4 = int(input("ingresa el primer numero: "))
num5 = int(input("ingresa el segundo numero: "))
num6 = int(input("ingresa el tercer numero: "))
if num4 >= num5 and num6:
    print("el primer numero es mayor")
elif num5 >= num4 and num6:
    print("el segundo numero es mayor")
elif num6 >= num4 and num5:
    print("el tercer numero es mayor")
else:
    print("no hay ningun numero ingresado")

# 6. calcula el precio final con un 10% de descuento si el total es mayor a $100

precio = float(input("ingresa un precio: "))
if precio > 100:
    descuento = precio * 0.10
    precio_total = precio - descuento
    print("se le dara un 10% de descuento")
else:
    precio_total = precio
    print("no se le da el descuento")
print(precio_total)

# 7. verifica si una persona puede votar (mayor o igual a 18 años)

edad = int(input("ingresa tu edad: "))
if edad >= 18:
    print("es mayor de edad, si puede votar")
else:
    print("no eres mayor de edad, asi que no puedes votar")

# 8. dado el precio y tipo de cliente (vip o normal), aplica un descuento del 20% solo a vip

cliente = input("ingresa el tipo de cliente (vip o normal): ")
precio1 = float(input("ingresa un precio: "))
if cliente == "normal":
    descuento = precio1
    precio1 = precio1
    print("no se le aplica descuento")
elif cliente == "vip":
    descuento = precio1 * 0.20
    print("se le aplica un 20% de descuento")
print(descuento)

# 9. determina si un numero es multiplo de 5 y de 3 al mismo tiempo

n = int(input("ingresa un numero: "))
if n % 3 == 0 and n % 5 == 0:
    print("es multiplo")
else:
    print("no es multiplo")

# 10. dado un numero verifica si es divisible entre dos numeros dados

n1 = int(input("ingresa un numero: "))
n2 = int(input("ingresa un numero: "))
n3 = int(input("ingresa un numero: "))
if n1 % n2 == 0 and n1 % n3 == 0:
    print("divisible")
else:
    print("no es divisible")

# Ejercicios con Listas (con condicionales)

# 11. Crea una lista con 5 números. Si el tercer número es mayor que 10, muestra “Mayor a 10”, si no, muestra “Menor o igual a 10”. 

num7 = [2, 3, 1, 8, 5]
if num7 [2] > 10:
    print("mayor a 10")
else:
    print("menor o igual a 10")

# 12. Verifica si el número 7 está en la lista [3, 5, 7, 9]. Si está, muestra “Está en la lista”, si no, muestra “No está en la lista”.

num8 = [3, 5, 7, 9]
if 7 in num8:
    print("esta en la lista")
else:
    print("no esta en la lista")

# 13. Suma los dos primeros elementos de la lista [4, 6, 2, 8]. Si la suma es mayor que 10, muestra “Suma alta”, de lo contrario, muestra “Suma baja”.

num9 = [4, 6, 2, 8]
suma1 = num9[0] + num9[1]
if suma1 > 10:
    print("suma alta")
else:
    print("suma baja")

# 14. Dada la lista ["Ana", "Luis", "Pedro", "Marta"], muestra el último nombre. Si ese nombre es “Marta”, muestra “Nombre correcto”, si no, “Nombre diferente”.

names1 = ["Ana", "Luis", "Pedro", "Marta"]
if "Marta" in names1:
    print("nombre correcto")
else:
    print("nombre diferente")

# 15. Crea una lista con tres colores. Cambia el segundo color solo si es igual a "azul", y muestra la lista actualizada.

colores = ["verde", "azul", "rosado"]
if colores[1] == "azul":
    colores[1] = "naranja"
print(colores)

# Ejercicios con Tuplas (con condicionales)

# 16. Crea una tupla con los valores (5, 8, 12, 20). Si el primer valor es menor que el último, muestra “Orden ascendente”, si no, “Orden descendente”.

num10 = (5, 8, 12, 20)
if num10[0] < num10[3]:
    print("orden ascendente")
else:
    print("orden descendente")

# 17. Dada la tupla (25, 32, 28), verifica si el segundo valor es mayor a 30. Si lo es, muestra “Edad mayor a 30”, si no, “Edad menor o igual a 30”.

num11 = (25, 32, 28)
if num11[1] > 30:
    print("edad mayor a 30")
else:
    print("edad menor o igual a 30")

# 18. Convierte la tupla (1, 2, 3) a lista, cambia el segundo valor a 10 solo si es igual a 2, luego vuelve a convertirla en tupla y muéstrala.

num12 = (1, 2, 3)
lista33 = list(num12)
if lista33[1] == 2:
    lista33[1] = 10
tupla22 = tuple(lista33)
print(tupla22)

# 19. Dada la tupla (4, 9), accede al segundo valor. Si es mayor que 5, muestra “Coordenada alta”, si no, “Coordenada baja”.

tupla11 = (4, 9)
if tupla11[1] > 5:
    print("coordenada alta")
else:
    print("coordenada baja")

# 20. Compara si las tuplas (3, 4) y (3, 5) son iguales. Si lo son, muestra “Tuplas iguales”, si no, “Tuplas diferentes”.

tupla33 = (3, 4)
tupla44 = (3, 5)
if tupla33 == tupla44:
    print("tuplas iguales")
else:
    print("tuplas diferentes")

# Ejercicios con Diccionarios (con condicionales)

# 21. Crea un diccionario con {"nombre": "Juan", "edad": 17}. Si la edad es mayor o igual a 18, muestra “Adulto”, si no, muestra “Menor de edad”.

persona1 =  {"nombre": "Juan", "edad": 17}
if persona1["edad"] >= 18:
    print("adulto")
else:
    print("menor de edad")

# 22. Crea un diccionario {"nombre": "Lucía", "edad": 20}. Si la edad es mayor a 18, cambia el valor de “edad” a 21. Luego muestra el diccionario.

persona2 = {"nombre": "Lucía", "edad": 20}
if persona2["edad"] > 18:
    persona2["edad"] = 21
print(persona2)

# 23. Crea un diccionario con {"nombre": "Carlos"}. Si la clave “ciudad” no existe, agrégala con el valor “Bogotá” y muestra el diccionario.

persona3 = {"nombre": "Carlos"}
if "ciudad" not in persona3:
    persona3["ciudad"] = "bogota"
print(persona3)

# 24. Dado el diccionario {"producto": "pan", "precio": 1200}, verifica si la clave “precio” existe. Si existe, muestra su valor, si no, muestra “No hay precio”.

alimentos = {"producto": "pan", "precio": 1200}
if "precio" in alimentos:
    print(alimentos["precio"])
else:
    print("no hay precio")

# 25. Crea un diccionario con {"pan": 1200, "leche": 2000}. Si “pan” está en el diccionario, muestra su precio; si no, muestra “Producto no disponible”

alimentos2 = {"pan": 1200, "leche": 2000}
if "pan" in alimentos2:
    print(alimentos2["pan"])
else:
    print("producto no disponible")

edad = int(input("ingresa tu edad: "))
if edad >= 18:
    print("es mayor de edad puede votar")
else:
    print("no es mayor de edad no puede votar")