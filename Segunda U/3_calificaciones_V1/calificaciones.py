#lista=[
#       ["Ruben",10.0,8.9,9.2],
#       ["Andres",10.0,10.0,10.0],
#       ["Maria",10.0,10.0,10.0]
#     ]
calificaciones = []

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\tOprima cualquier tecla para continuar...\n\t")

def menu_principal():
    print("\n\t\t\t..::: Sistema de Gestiion de Calificaciones :::....\n\n\t\t-1.--Agregar--\n\t\t-2.--Mostar--\n\t\t-3.--Calcular Promedios--\n\t\t-4.--SALIR--")
    opcion = input("\n\t\t Elige una opción (1-4): ").upper()
    return opcion

def agregar_clalificaciones(lista):
    borrarPantalla()
    print(".:: Agragar Calificaciones ::.")
    nombre=input("Nombre del Alumno: ").upper().strip()
    calificaciones=[]
    for i in range(1,4):
        bandera=True
        while bandera:
            try:
                #calificaciones.append(float(input(f"Calificaciones {i}: ")))
                cal=float(input(f"Calificación {i}:"))
                if cal >= 0 and cal<=10:
                    calificaciones.append(cal)
                    bandera=False
                else:
                    input("Ingrese en valor comprendido entre 0 y 10: ")
                    esperarTecla()
            except ValueError:
                input("Ingrese el valor numerico")
                esperarTecla()
    lista.append([nombre] + calificaciones)
    print("Accion realizada con exito ")

    

    '''nombre = input("Ingresa el nombre: ").upper().strip()
    try:
        cal1 = float(input("Ingresa la calificación 1: "))
        cal2 = float(input("Ingresa la calificación 2: "))
        cal3 = float(input("Ingresa la calificación 3: "))
    except ValueError:
        print("\n\t\t.:: ¡ERROR! Debes ingresar números válidos. ::.")
        esperarTecla()
        return
    if nombre:
        calificaciones.append([nombre, cal1, cal2, cal3])
        print("\n\t\t.:: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! ::.")
    esperarTecla()'''

def mostrar_calificaciones(lista):
    borrarPantalla()
    print(".::Mostrar Calificaciones::.")
    if len(lista)>0:
        print("{'Nombre':<15}{'Calif.1 ':<10}{'Calif.2':<10}{'Calif.3':<10}"   )
        print("-"*50)
        for fila in lista:
            print(f"{fila[0]:<15}   {fila[1]:<10}   {fila[2]:<10}   {fila[3]:<10}")
            print("-"*50)
            print(f"Son {len(lista)} alumnos")
    else:
        print("No hay calificaciones en la lista")

    ''' print(".:: Lista de Calificaciones ::.")
        if not calificaciones:
            print("\n\t\t.:: No hay registros para mostrar ::.")
        else:
            for alumno in calificaciones:
                print(f"Nombre: {alumno[0]}, Calificaciones: {alumno[1:]}")
        esperarTecla()'''

def calcular_promedios(lista):
    borrarPantalla()
    print(".::Promedios Alumnos::.")
    if len(lista) > 0:
        print(f"{'Nombre':<15}{'Promedio':<10}")
        print("-" * 30)
        suma_general = 0
        for fila in lista:
            promedio = (fila[1] + fila[2] + fila[3]) / 3
            suma_general += promedio
            print(f"{fila[0]:<15}{promedio:<10.2f}")
        promedio_general = suma_general / len(lista)
        print("-" * 30)
        print(f"El promedio general es: {promedio_general:.2f}")
    else:
        print("No hay calificaciones en la lista")



    '''borrarPantalla()
    print(".:: Promedios de los Alumnos ::.")
    if not calificaciones:
        print("\n\t\t.:: No hay registros para calcular promedios ::.")
    else:
        for alumno in calificaciones:
            promedio = sum(alumno[1:]) / 3
            print(f"Nombre: {alumno[0]} - Promedio: {promedio:.2f}")
    esperarTecla()'''

# Programa principal
'''while True:
    borrarPantalla()
    op = menu_principal()
    if op == "1":
        agregar_clalificaciones()
    elif op == "2":
        mostrar_calificaciones()
    elif op == "3":
        calcular_promedios()
    elif op == "4":
        print("\n\t\t.:: Saliendo del programa... ::.")
        break
    else:
        print("\n\t\t.:: Opción no válida ::.")
        esperarTecla()'''
