import mysql.connector
from mysql.connector import Error
import os

def borrarPantalla():
    os.system("cls")

def esperarTecla():
    input("\n\t... Oprima cualquier tecla para continuar ...")

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_calificaciones"
        )
        return conexion
    except Error as e:
        print(f"\n\tError de conexión: {e}")
        return None

def menu_principal():
    print("\n\t\t..::: Sistema de Gestión de Calificaciones :::..\n")
    print("\t1. Agregar Calificaciones")
    print("\t2. Mostrar Calificaciones")
    print("\t3. Calcular Promedios")
    print("\t4. SALIR")
    return input("\n\tSelecciona una opción: ").strip()

def agregar_clalificaciones():
    borrarPantalla()
    print(".:: Agregar Calificaciones ::.")
    nombre = input("Nombre del Alumno: ").upper().strip()
    calificaciones = []

    for i in range(1, 4):
        while True:
            try:
                cal = float(input(f"Calificación {i}: "))
                if 0 <= cal <= 10:
                    calificaciones.append(cal)
                    break
                else:
                    print("⚠️ Ingrese un valor entre 0 y 10.")
            except ValueError:
                print("⚠️ Ingresa un número válido.")

    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        sql = "INSERT INTO calificaciones (nombre, cal1, cal2, cal3) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nombre, *calificaciones))
        conexion.commit()
        conexion.close()
        print("\n✅ Calificaciones agregadas con éxito.")
    esperarTecla()

def mostrar_calificaciones():
    borrarPantalla()
    print(".:: Mostrar Calificaciones ::.")
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM calificaciones")
        registros = cursor.fetchall()
        if registros:
            print(f"{'ID':<5}{'Nombre':<15}{'Calif.1':<10}{'Calif.2':<10}{'Calif.3':<10}")
            print("-" * 50)
            for fila in registros:
                print(f"{fila[0]:<5}{fila[1]:<15}{fila[2]:<10}{fila[3]:<10}{fila[4]:<10}")
            print("-" * 50)
            print(f"Total de alumnos: {len(registros)}")
        else:
            print("⚠️ No hay calificaciones registradas.")
        conexion.close()
    esperarTecla()

def calcular_promedios():
    borrarPantalla()
    print(".:: Promedios de Alumnos ::.")
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre, cal1, cal2, cal3 FROM calificaciones")
        registros = cursor.fetchall()
        if registros:
            print(f"{'Nombre':<15}{'Promedio':<10}")
            print("-" * 30)
            suma_general = 0
            for fila in registros:
                promedio = (fila[1] + fila[2] + fila[3]) / 3
                suma_general += promedio
                print(f"{fila[0]:<15}{promedio:<10.2f}")
            promedio_general = suma_general / len(registros)
            print("-" * 30)
            print(f"Promedio general del grupo: {promedio_general:.2f}")
        else:
            print("⚠️ No hay calificaciones registradas.")
        conexion.close()
    esperarTecla()

