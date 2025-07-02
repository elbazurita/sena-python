# 1. calculadora de promedio
calificacion = float(input("ingresa una calificacion: "))
calificacion2 = float(input("ingresa una calificacion: "))
calificacion3 = float(input("ingresa una calificacion: "))
lista = [calificacion, calificacion2, calificacion3]
print(lista)
promedio = sum(lista) / len(lista)
print(promedio)

# 2. actualiza precios
productos = {
    "leche": 2500,
    "repollo": 3000,
    "papa": 1000
}
print(productos)
porcentaje = float(input("ingresa un porcentage de aumento (%): "))
productos["leche"] += productos["leche"] * (porcentaje / 100)
productos["repollo"] += productos["repollo"] * (porcentaje / 100)
productos["papa"] += productos["papa"] * (porcentaje / 100)
print(productos)

# 3. conversor de temperaturas
tem1 = float(input("temperatura 1 en °C: "))
tem2 =float(input("temperatura 2 en °C: "))
tem3 = float(input("temperatura 3 en °C: "))
tem4 = float(input("temperatura 4 en °C: "))
tem5 = float(input("temperatura 5 en °C: "))
celsius = (tem1, tem2, tem3, tem4, tem5)
f1 = tem1 * 9/5 + 32
f2 = tem2 * 9/5 + 32
f3 = tem3 * 9/5 + 32
f4 = tem4 * 9/5 + 32
f5 = tem5 * 9/5 + 32
fahrenheit = (f1, f2, f3, f4, f5)
print("temperaturas en °C:", celsius)
print("temperaturas en °F:", fahrenheit)

# 4. edad promedio con listas
edades = [int(input("edad 1: ")), int(input("edad 2: ")), int(input("edad 3: ")), int(input("edad 4: ")), int(input("edad 5: "))]
promedio2 = sum(edades) / len(edades)
print(f"mayor: {max(edades)}, menor: {min(edades)}, promedio: {promedio2}")

# 5. diccionario de frutas
frutas = {
    "banano": 5000,
    "manzana": 1000,
    "pera": 2000
}
kilos_banano = float(input("ingrese la cantidad de kilos: "))
kilos_manzana = float(input("ingrese la cantidad de kilos: "))
kilos_pera = float(input("ingrese la cantidad de kilos: "))
total = (kilos_banano * frutas["banano"]) + (kilos_manzana * frutas["manzana"]) + (kilos_pera * frutas["pera"])
print("el total a pagar es: ", total)

# 6. suma de elentos en tupla
num1 = (1, 7, 9, 3, 4)
suma_total = sum(num1)
print(suma_total)

# 7. inventario con listas de diccionarios
nombre1 = input("ingrese el nombre del primer producto: ")
cantidad1 = int(input("ingrese la cantidad del producto: "))
precio1 = float(input("ingrese el precio del producto: "))
producto1 = {"nombre": nombre1, "cantidad": cantidad1, "precio": precio1}

nombre2 = input("ingrese el nombre del segundo producto: ")
cantidad2 = int(input("ingrese la cantidad del producto: "))
precio2 = float(input("ingrese el precio del producto: "))
producto2 = {"nombre": nombre2, "cantidad": cantidad2, "precio": precio2}

nombre3 = input("ingrese el nombre del tercer producto: ")
cantidad3 = int(input("ingrese la cantidad del producto: "))
precio3 = float(input("ingrese el precio del producto: "))
producto3 = {"nombre": nombre3, "cantidad": cantidad3, "precio": precio3}

inventario = [producto1, producto2, producto3]
print(inventario)

total1 = (producto1["cantidad"] * producto1["precio"] + producto2["cantidad"] * producto2["precio"] + producto3["cantidad"] * producto3["precio"])
print(total1)

# 8. modificar una lista de precios
precios1 = [2000, 5000, 1000, 3000, 9000]
descuento = float(input("ingrese el descuento en porcentaje: "))
prrecio1 = precios1[0] - (precios1[0] * descuento / 100)
prrecio2 = precios1[1] - (precios1[1] * descuento / 100)
prrecio3 = precios1[2] - (precios1[2] * descuento / 100)
prrecio4 = precios1[3] - (precios1[3] * descuento / 100)
prrecio5 = precios1[4] - (precios1[4] * descuento / 100)
print("precios con descuento:")
print(prrecio1, prrecio2, prrecio3, prrecio4, prrecio5)

# 9. notas con tuplas
notta1 = float(input("ingresa la primer nota: "))
notta2 = float(input("ingresa la segunda nota: "))
notta3 = float(input("ingresa la tercer nota: "))
notta4 = float(input("ingresa la cuarta nota: "))
nottas = (notta1, notta2, notta3, notta4)
mayor = max(nottas)
menor = min(nottas)
print("la nota mas alta es:", mayor)
print("la nota mas baja es:", menor)

# 10. diccionario de conversiones
conversiones = {
    "km": 2000,
    "m": 5000,
    "cm": 1000
}
unidad = input("Ingresa la unidad: ")
cantidad = float(input("Ingresa la cantidad: "))

resultado = cantidad * conversiones[unidad]
print("Equivalente en metros:", resultado)


# 11. lista de productos mas IVA
preccio1 = float(input("Ingresa el primer precio : "))
preccio2 = float(input("Ingresa el segundo precio 2: "))
preccio3 = float(input("Ingresa el tercer precio 3: "))

precios = [preccio1, preccio2, preccio3]
iva1 = preccio1 * 1.19
iva2 = preccio2 * 1.19
iva3 = preccio3 * 1.19
precios_IVA = [iva1, iva2, iva3]

print(precios_IVA)

# 12. tupla de operaciones matemáticas
numm1 = float(input("ingresa el primer numero: "))
numm2 = float(input("ingresa el segundo numero: "))
operaciones = (numm1 + numm2, numm1 - numm2, numm1 * numm2, numm1 / numm2)
print(operaciones)

# 13. diccionario de estudiantes
estudiantes = {
    "Alfredo": 2.4,
    "El pepe": 3.3,
    "Alberto": 1.8,
    "Jose": 4.8
}
summa = estudiantes["Alfredo"] + estudiantes["El pepe"] + estudiantes["Alberto"] + estudiantes["Jose"]
prommedio = summa / 4
print(prommedio)

# 14.  Lista de salarios
salari1 = float(input("primer salario: "))
salari2 = float(input("segundo salario: "))
salari3 = float(input("tercer salario: "))
salari4 = float(input("cuarto salario: "))
salari5 = float(input("quinto salario: "))
salarios = [salari1, salari2, salari3, salari4, salari5]
salari_nuevos = [
    salari1 * 1.10,
    salari2 * 1.10,
    salari3 * 1.10,
    salari4 * 1.10,
    salari5 * 1.10
]
print("los nuevos salarios de aumento del 10%:", salari_nuevos)

# 15. diccionario de impuestos
productos = {
    "pc gamer2": 9000,
    "phone": 5000,
    "nokia": 2000
}
immpuesto = float(input("Ingresa el porcentaje de impuesto: "))
precio_pc_gamer2 = productos["pc gamer2"] * (1 + immpuesto / 100)
precio_phone = productos["phone"] * (1 + immpuesto / 100)
precio_nokia = productos["nokia"] * (1 + immpuesto / 100)
print(precio_pc_gamer2)
print(precio_phone)
print( precio_nokia)

# 16. analisis de edades
eddad1 = int(input("Edad 1: "))
eddad2 = int(input("Edad 2: "))
eddad3 = int(input("Edad 3: "))
eddad4 = int(input("Edad 4: "))
eddad5 = int(input("Edad 5: "))

m1 = eddad1 >= 18
m2 = eddad2 >= 18
m3 = eddad3 >= 18
m4 = eddad4 >= 18
m5 = eddad5 >= 18

mayores = int(m1) + int(m2) + int(m3) + int(m4) + int(m5)
menores = 5 - mayores
print(mayores)
print(menores)

# 17. Tupla de conversiones de moneda
dolares = float(input("Cantidad en dólares: "))
euros = dolares * 0.85
pesos = dolares * 4000
yenes = dolares * 110
conversiones = (euros, pesos, yenes)
print(conversiones)

# 18. diccionario de ventas
produc1 = input("Nombre del primer producto: ")
canti1 = int(input("Cantidad vendida: "))

produc2 = input("Nombre del segundo producto: ")
canti2 = int(input("Cantidad vendida: "))

produc3 = input("Nombre del tercer producto: ")
canti3 = int(input("Cantidad vendida: "))

ventas = {produc1: canti1, produc2: canti2, produc3: canti3}
total = canti1 + canti2 + canti3
print(total)

# 19. lista de temperaturas extremas
temperaturas = [6, 39, 9, 8, 40, 33]
print("Temperaturas mayores a 30°:")
print(temperaturas[1], temperaturas[3], temperaturas[4])
print("Temperaturas menores a 10°:")
print(temperaturas[0], temperaturas[2], temperaturas[3])

# 20. actualizar precios con metodos de listas
preciosss = [5000, 1000, 7000, 6000, 9000]
eliminar = float(input("eliminar precio: "))
preciosss.remove(eliminar)
nuevo = float(input("agregar nuevo precio: "))
preciosss.append(nuevo)
preciosss.sort()
print(preciosss)