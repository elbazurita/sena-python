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