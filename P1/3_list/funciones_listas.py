import os
''''
List (Array)
son colleciones o conjunto de datos/valores bajo un mismmo nombre, para acceder a los valores se hace con un indice numerico

nota: sus valores si son modificables 
la listas es una collecion ordenada y modificable. Permite miembros duplicados.
'''
os.system("cls")
#Funciones mas comunes en las listas

paises=["Mexico","Brasil","España","Canada"]
numeros=[23,45,8,24, 23,233]
varios=["Hola",3.1416,33,True]

#Imprimir el contenido de una lista
print(paises)
print(numeros)
print(varios)

#Recorrer un lista e imprimir el recorrido
#1er forma

for i in paises:
    print(i)

lista=''-
for i in paises:
    lista=lista+f"{i},"
print(lista)

lista=''
for i in paises:
    lista+=f"{i},"
print(lista)

#2da forma

for i in range(0,len(paises)):
    print(paises[i])

for i in range(0,len(paises)):
    lista+=f"{paises[i]},"
print(paises[i])

os.system("cls")
print(paises)
print(numeros)
print(varios)

paises.sort()
print(paises)
numeros.sort()
print(numeros)

#Dar vuelta a las listas
varios.reverse()
print(varios)
numeros.reverse()
print(numeros)
paises.reverse()
print(paises)

#Buscar un elemento dentro de una lista
print("España" in paises )

#Insertar, añadir, agragar un elemnto a la lista
os.system("cls")
print(paises)

#1er forma
paises.append("México")
print(paises)

#2da forma
paises.insert(1,"México")
print(paises)

#Borrar, eliminar, suprimir, quitar un lemento de la lista
os.system("cls")
print(paises)

#1er Forma
paises.pop(0)
print(paises)

#2da Forma
paises.remove("México")
print(paises)

paises.sort()

#Obtener la posicion donde se encuntra un elemento
os.system("cls")
print(paises)

posicion=paises.index("Canada")
print(posicion)
paises.pop(posicion)
print(posicion)

#Conter el numero que hay en una lista
os.system("cls")
print(numeros)

cuantas=numeros.count(45)
print(cuantas)

cuantas=numeros.count(23)
print(cuantas)

cuantas=numeros.count(233)
print(cuantas)

#Unir una lista con otra
os.system("cls")
print(numeros)
numeros2=[100,200]
print(numeros2)

#Crear un programa que una las listas numericas 1 y e imprima el contenido de  de las lista resultante en forma decendente
os.system("cls")
numeros.extend(numeros2)
print(numeros)

numeros.sort()
numeros.reverse()
print(numeros)



#Crear una lista multidimensional para almacenar los nombres y los telefonos de unos contactos "Agenda"
# Definir la lista multidimensional
agenda = [
    ["Alejandro", "123-456-7890"],
    ["Roberto", "987-654-3210"],
    ["Daniel", "567-890-1234"]
]

# Mostrar los contactos
print("\nAgenda Telefónica:")
for contacto in agenda:
    print(f"Nombre: {contacto[0]}, Teléfono: {contacto[1]}")