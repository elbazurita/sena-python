# 1. append(x)
numero = []
numero.append(7)
print(numero)

# ejercicio 2
nombres = ["Ana", "Luis"]
nombres.append("carlos")
print(nombres)

# 2. insert(i, x)
numeros = [1, 2, 3]
numeros.insert(0, 99)
print(numeros)

# ejercicio 2
colores = ["azul", "verde"]
colores.insert(1, "rojo")
print(colores)

# 3. extend(iterable)
lista_numeros = [1, 2, 3]
lista_numeros.extend([4, 5, 6])
print(lista_numeros)

# ejercicio 2
letras = ["a", "b"]
letras.extend(["o", "k"])
print(letras)

# 4. remove(x)
frutas = ["manzana", "uva", "pera"]
frutas.remove("uva")
print(frutas)

# ejercicio 2
lista_numeros2 = [1, 2, 3, 2]
lista_numeros2.remove(2)
print(lista_numeros2)

# 5. pop([i])
numeros2 = [1, 2, 3, 4]
valor = numeros2.pop()
print(valor)
print(numeros2)

# ejercicio 2
number = ["uno", "dos", "tres"]
valor2 = number.pop(0)
print(valor2)
print(number)

# 6. clear()
lista_number = [1, 2, 3]
lista_number.clear()
print(lista_number)

# ejercicio 2
productos = ["alcatel", "pc gamer", "nokia", "frutiño", "ventilador"]
productos.clear()
print(productos)

# 7. index(x)
fruits = ["manzana", "pera", "uva"]
print(fruits.index("pera"))

# ejercicio 2
number2 = [4, 5, 6, 7]
print(number2.index(6))

# 8. count(x)
number3 = [3, 1, 3, 5, 3]
print(number3.count(3))

# ejercicio 2
letras2 = ["a", "b", "a", "c", "a"]
print(letras2.count("a"))

# 9. sort()
numeros3 = [5, 1, 4, 2, 3]
numeros3.sort()
print(numeros3)

#ejercicio 2
letras3 = ["z", "a", "m", "b"]
letras3.sort()
print(letras3)

# 10. reverse()
numeros4 = [1, 2, 3, 4]
numeros4.reverse()
print(numeros4)

# ejercicio 2
palabras = ["inicio", "medio", "fin"]
palabras.reverse()
print(palabras)

# 11. copy()
numeros5 = [1, 2, 3]
nueva = numeros5.copy()
nueva.append(4)
print(numeros5)
print(nueva)

# ejercicio 2
letras4 = ["a", "b", "c"]
nuevo = letras4.copy()
nuevo.append("d")
print(letras4)
print(nuevo)

# actividad de listas
lista1 = ["mondongo", "arroz", "pollo"]
lista2 = ["pc gamer", "nokia", "alcatel"]
lista1.append(100)
lista1.append("hola mundo")
lista2.append("hola y adios")
lista2.append(300)
lista3 = lista1.copy()
lista3.pop()
lista4 = lista2.copy()
lista4.remove("hola y adios")
lista4.pop()
lista5 = []
lista5.extend(lista4)
lista5.extend(lista3)

# tuplas

# 1 convertir una tupla a lista
tupla = (1, 2, 3)
lista = list(tupla)
print(lista)

# convertir una lista a tupla
listae = [4, 5, 6]
tupla1 = tuple(listae)
print(tupla1)

# ejercicio 1
tupla2 = ("manzana", "pera")
lista6 = list(tupla2)
fruta1 = input("ingresa una nueva fruta: ")
lista6.append(fruta1)
tupla3 = tuple(lista6)
print(tupla3)

# ejercicio 2
tupla4 = (4.2, 3.8)
lista7 = list(tupla4)
nota = input("ingresa una nueva nota: ")
lista7.append(nota)
tupla5 = (lista7)
pirnt(tupla5)