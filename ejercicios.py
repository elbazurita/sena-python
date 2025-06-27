# 1. registrar 3 frutas
frutas = []
print(frutas)
fruta = input("ingresa la primera fruta: ")
frutas.append(fruta)
fruta2 = input("ingresa la segunda fruta: ")
frutas.append(fruta2)
fruta3 = input("ingresa la tercera fruta: ")
frutas.append(fruta3)
print(frutas)

# 2. guardar 2 edades
edades = []
print(edades)
e1 = input("ingresa tu edad: ")
edades.append(e1)
e2 = input("ingresa tu edad: ")
edades.append(e2)
print(edades)

# 3. notas de 2 estudiantes
notas = []
print(notas)
nota1 = input("ingrese una nota: ")
notas.append(nota1)
nota2 = input("ingresa una nota: ")
notas.append(nota2)
print(notas)

# 4. productos en una bolsa
productos = []
print(productos)
pro1 = input("ingrese el nombre de un producto: ")
productos.append(pro1)
pro2 = input("ingrese el nombre de un producto: ")
productos.append(pro2)
pro3 = input("ingrese el nombre de un producto: ")
productos.append(pro3)
print(productos)

# 5. precios de 3 articulos
precios = []
print(precios)
precio1 = float(input("ingresa un precio: "))
precios.append(precio1)
precio2 = float(input("ingrese un precio: "))
precios.append(precio2)
precio3 = float(input("ingrese un precio: "))
precios.append(precio3)
print(precios)
total = precio1 + precio2 + precio3
print("la suma total es:", total)

# 6. numeros ingresados por el usuario
numeros = []
print(numeros)
no1 =input("ingrese un numero: ")
numeros.append(no1)
no2 = input("ingrese un numero: ")
numeros.append(no2)
no3 = input("ingrese un numero: ")
numeros.append(no3)
print(numeros)
mayor = max(numeros)
menor = min(numeros)
print("numero mayor:" , mayor)
print("numero menor:" , menor)

# 7. registrar 2 nombres completos
nombres = []
print(nombres)
nom1 = input("ingrese su nombre completo: ")
nombres.append(nom1)
nom2 = input("ingrese su nombre colpleto: ")
nombres.append(nom2)
print("hola" , nom1)
print("hola" , nom2)

# 8. registrar dos temperaturas
temperaturas = []
print(temperaturas)
temp1 = float(input("ingrese una temperatura en celsius: "))
temperaturas.append(temp1)
temp2 = float(input("ingrese una temperatura en celsius: "))
temperaturas.append(temp2)
fahrenheit1 = (temperaturas[0] * 9/5) + 32
print(fahrenheit1)
fahrenheit2 = (temperaturas[1] * 9/5) + 32
print(fahrenheit2)