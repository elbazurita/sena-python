#  1. verifica si un numero es positivo, negativo o cero.
numero1 = float(input("ingrese un numero: "))
if numero1 > 0:
    print(f"positivo porque es {numero1}")
elif numero1 < 0 :
    print(f"positivo porque es {numero1}")
else:
    print(f"es cero {numero1} ")

# 2. calcula el mayor de dos numeros ingresados._
n1 = float(input("ingrese un numero: "))
n2 = float(input("ingrese otro numero: "))
if n1 > n2:
    print(f"el numero mayor es {n1}")
elif n2 > n1:
    print(f"elnumero mayor es {n2}")
else:
    print("ambos numeros son iguales")

# 3. determina si un numero es par o impar.
numero = int(input("ingresa un numero: "))
if numero % 2 == 0:
    print("el numero es par")
elif numero % 2 != 0:
    print("el numero es impar")
else:
    print("no se pudo determinar si el numero es par o impar")

# 4. dado un numero, verifica si esta entre 10 y 20.
num = int(input("ingresa un numero: "))
if 10 <= num <= 20:
    print("el numero esta entre 10 y 20")
elif num < 10:
    print("el numero es menor que 10")
else:
    print("el numero es mayo que 20")

# 5. dados tres numeros encuentra el mayor usando condicionales.
num1 = int(input("ingresa el primer numero: "))
num2 = int(input("ingresa el segundo numero: "))
num3 = int(input("ingresa el tercer numero: "))
if num1 >= num2 and num1 >= num3:
    print(f"el numero mayor es {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"el numero mayor es {num2}")
else:
    print(f"el numero mayor es {num3}")

# 6. calcula el precio final con un 10% de descuento si el total es mayor a $100.
total = float(input("ingresa el total de la compra: "))
if total > 100:
    descuento = total * 0.10
    precio_final  = total - descuento
    print("se le dio un 10% de descuento")
elif total == 100:
    print("no se le dio el descuento")
    print(f"el precio final es {total}")
else:
    print("no se aplica descuento")
    print(f"el precio final es {total}")

# 7. verifica si una persona puede votar. (mayo o igual a 18 años).
edad = int(input("ingresa tu edad: "))
if edad >= 18:
    print("puede votar")
else:
    print("no puede votar")

# 8 aplica un descuento del 20% solo a clientes vip
total2 = float(input("Ingresa el total de la compra: "))
es_vip = input("¿Eres cliente VIP? (sí/no): ").lower()
if es_vip == "sí" or es_vip == "si":
    descuento = total2 * 0.20
    precio_final = total2 - descuento
    print("Eres cliente VIP. Se le aplica 20% de descuento.")
    print("El precio final es: $", precio_final)
elif es_vip == "no":
    print("No eres cliente VIP. No se aplica descuento.")
    print("El precio final es: $", total2)
else:
    print("Respuesta no válida. No se aplicó ningún descuento.")
    print("El precio final es: $", total2)

# 9.determina si un número es múltiplo de 5 y de 3 al mismo tiempo.
numero4 = int(input("ingresa un número: "))
if numero4 % 5 == 0 and numero4 % 3 == 0:
    print(f"{numero4} es múltiplo de 5 y 3")
else:
    print(f"{numero4} no es múltiplo de 5 y 3")

# 10.verifica si un número es divisible entre dos números dados.
numero5 = int(input("Ingresa el número que quieres verificar: "))
divisor1 = int(input("Ingresa el primer divisor: "))
divisor2 = int(input("Ingresa el segundo divisor: "))
if numero5 % divisor1 == 0 and numero5 % divisor2 == 0:
    print(f"{numero5} es divisible entre {divisor1} y {divisor2}.")
elif numero5 % divisor1 == 0:
    print(f"{numero5} solo es divisible entre {divisor1}.")
elif numero5 % divisor2 == 0:
    print(f"{numero5} solo es divisible entre {divisor2}.")
else:
    print(f"{numero5} no es divisible entre {divisor1} ni entre {divisor2}.")

# 11. ingresa una palabra muestra si su primera letra es vocal consonante o un numero
palabra = input("ingresa una palabra: ")
letra = palabra[0].lower()
if letra in "aeiou":
    print("vocal")
elif letra in "0123456789":
    print("numero")
else:
    print("consonante")

# 12. pide una fruta si esta en la lista ["manzana", "pera", "piña"], muestra su precio. si no, indica que esta disponible.
fruta1 = input("ingresa una fruta: ")
if fruta1 == "manzana":
    print("precio: 2000")
elif fruta1 == "pera":
    print("precio: 5000")
elif fruta1 == "piña":
    print("precio: 9000")
else:
    print("no hay")

# 13. pide tu calificacion (0 a 5). si es menor que 3, reprobado.entre 3 y 4, aprobado. mayor a 4, excelente.
nota1 = float(input("ingresa tu calificacion: "))
if nota1 < 3:
    print("reprobado")
elif nota1 <= 4:
    print("aprobado")
else:
    print("excelente")

# 14. pide un numero y muestra si es divisible entre 4, entre 6, o no loes.
nnumero = float(input("ingresa un numero: "))
if nnumero % 4 == 0:
    print("divisible entre 4")
elif nnumero % 6 == 0:
    print("divisible entre 6")
else:
    print("no es divisible entre 4 ni 6")

# 15. crea un sistema de autenticacion basico. pide usuario y clave. usa un diccionario para validar.
usuario = input("ingrese su usuario: ")
clave = input("ingrese su clave: ")
if usuario == "admin" and clave == "1234":
    print("acceso permitido")
else:
    print("acceso denegado")

# 16. solicita una edad y muestra a que grupo pertenece: niño (0-12), adolescente (13-17), adulto (18-64), mayor (65+)
edad1 = int(input("ingrese su edad: "))
if edad1 <= 12:
    print("niño")
elif edad1 <= 17:
    print("adolescente")
elif edad1 <= 64:
    print("adulto")
else:
    print("mayor")

# 17. pide el nombre de una ciudad. si esta en una tupla, muestra que es capital; si no, muestra "ciudad secundaria"
ciudad = input("ingresa el nombre de una ciudad: ")
if ciudad == "medellin":
    print("es capital")
elif ciudad == "cali":
    print("es capital")
elif ciudad == "bogota":
    print("es capital")
else:
    print("ciudad secundaria")

# 18. ingresa el valor de una compra. si es mayor de $200.000 aplica un 15% de descuento. entre $100.000 y $200.000 aplica 10%. si es menor, no hay desceunto.
valor1 = float(input("ingresa el valor de la compra: "))
if valor1 > 200000:
    print("desceunto 15%")
    print("total:", valor1 * 0.85)
elif valor1 >= 100000:
    print("descuento 10%")
    print("total:", valor1 * 0.90)
else:
    print("sin descuento")
    print("total:", valor1)

# 19. pide el nombre y el numero de horas trabajadas. calcula el salario con tarifa de $10.000/hora. si trabajo mas de 40 horas. aplica un bono del 20%.
nombre3 = input("ingrese su nombre: ")
horas = int(input("ingrese el numero de horas trabajadas: "))
salario = horas * 10000
if horas > 40:
    salario = salario * 1.2
    print("salario:", salario)

# 20. ingresa tu puntuaje en una prueba (0 a 100). si es menor a 50, insuficiente. de 50 a 79, aceptable. 80 a 100, sobresaliente.
puntaje = int(input("ingrese su puntaje (0 a 100): "))
if puntaje < 50:
    print("insuficiente")
elif 50 <= puntaje <= 79:
    print("aceptable")
else:
    print("sobresaliente")