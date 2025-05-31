
'''
Crear una funcion que calcule e imprima cuelquier tabal de multiplicar

Rsttricciones:
1.- Sin usar estructuras de control
2.- Sin usar funciones
'''
num = int(input("Inserta el numro de la tabla de multiplicar: "))
mult = num*1
print(f"{num} x 1 = {mult}")
mult = num*2
print(f"{num} x 2 = {mult}")
mult = num*3
print(f"{num}  x 3 = {mult}")
mult = num*4
print(f"{num} x 4 = {mult}")
mult = num*5
print(f"{num} x 5 = {mult}")
mult = num*6
print(f"{num} x 6 = {mult}")
mult = num*7
print(f"{num} x 7 = {mult}")
mult = num*8
print(f"{num} x 8 = {mult}")
mult = num*9
print(f"{num} x 9 = {mult}")
mult = num*10
print(f"{num} x 10 = {mult}")

#Version 3
'''
crear un progama que calcule e imprima cualquier tabla de multipicar

Restricciones
1.-con estructuras de control
2.-Sin funciones
'''
num = int(input("Inserta el numro de la tabla de multiplicar: "))
for i in range(1,11):
    mult=num*i
    print(f"{num} x {i} = {mult}")

#Version 4
'''
crear un progama que calcule e imprima cualquier tabla de multipicar

Restricciones
1.-con estructuras de control
2.-con funciones
'''

def tabla(numero):
    num = numero
    respuesta = ""
    for i in range(1,11):
        mult=num*i
        respuesta += f"\t{num} x {i} = {mult}\n"
    return respuesta

num = int(input("Inserta el numro de la tabla de multiplicar: "))
resultado=tabla(num)
print(f"{resultado}")