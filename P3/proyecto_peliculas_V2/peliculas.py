import mysql.connector
from mysql.connector import Error
import os

def borrarPantalla():
    os.system("cls")

def esperarTecla():
    input("\n\tOprima cualquier tecla para continuar...\n\t")

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_peliculas"
        )
        return conexion
    except Error as e:
        print(f"\n\tError al conectar con la base de datos: {e}")
        return None

def crearPeliculas():
    borrarPantalla()
    print("\n\t.:: Alta de Películas ::.\n")
    nombre = input("Nombre: ").upper().strip()
    categoria = input("Categoría: ").upper().strip()
    clasificacion = input("Clasificación: ").upper().strip()
    genero = input("Género: ").upper().strip()
    idioma = input("Idioma: ").upper().strip()

    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        sql = "INSERT INTO peliculas (nombre, categoria, clasificacion, genero, idioma) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (nombre, categoria, clasificacion, genero, idioma))
        conexion.commit()
        conexion.close()
        print("\n✅ ¡Película registrada con éxito!")
    esperarTecla()

def mostrarPeliculas():
    borrarPantalla()
    print("\n\t.:: Lista de Películas ::.\n")
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM peliculas")
        resultados = cursor.fetchall()
        if resultados:
            print(f"{'ID':<5}{'Nombre':<25}{'Categoría':<15}{'Clasificación':<15}{'Género':<15}{'Idioma':<15}")
            print("-" * 90)
            for peli in resultados:
                print(f"{peli[0]:<5}{peli[1]:<25}{peli[2]:<15}{peli[3]:<15}{peli[4]:<15}{peli[5]:<15}")
        else:
            print("⚠️ No hay películas registradas.")
        conexion.close()
    esperarTecla()

def borrarPeliculas():
    borrarPantalla()
    print("\n\t.:: Borrar Todas las Películas ::.\n")
    resp = input("¿Estás seguro de borrar TODAS las películas? (Si/No): ").lower().strip()
    if resp == "si":
        conexion = conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM peliculas")
            conexion.commit()
            conexion.close()
            print("\n✅ Todas las películas han sido eliminadas.")
    esperarTecla()

def agregarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Agregar Característica no soportada aún ::.\n")
    print("⚠️ En esta versión solo puedes modificar campos existentes.")
    esperarTecla()

def modificarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Modificar Característica de Película ::.\n")
    mostrarPeliculas()
    try:
        peli_id = int(input("\nIngresa el ID de la película a modificar: "))
    except ValueError:
        print("⚠️ Debes ingresar un número válido.")
        esperarTecla()
        return

    print("\nCampos disponibles para modificar: nombre, categoria, clasificacion, genero, idioma")
    campo = input("¿Qué campo deseas modificar?: ").lower().strip()
    if campo not in ["nombre", "categoria", "clasificacion", "genero", "idioma"]:
        print("⚠️ Campo no válido.")
        esperarTecla()
        return

    nuevo_valor = input(f"Ingresa el nuevo valor para '{campo}': ").upper().strip()
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        sql = f"UPDATE peliculas SET {campo} = %s WHERE id = %s"
        cursor.execute(sql, (nuevo_valor, peli_id))
        conexion.commit()
        conexion.close()
        print("\n✅ Película actualizada con éxito.")
    esperarTecla()

def borrarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Borrar una Característica ::.\n")
    mostrarPeliculas()
    try:
        peli_id = int(input("\nIngresa el ID de la película: "))
    except ValueError:
        print("⚠️ Debes ingresar un número válido.")
        esperarTecla()
        return

    print("Campos que puedes borrar: nombre, categoria, clasificacion, genero, idioma")
    campo = input("¿Qué campo deseas vaciar?: ").lower().strip()
    if campo not in ["nombre", "categoria", "clasificacion", "genero", "idioma"]:
        print("⚠️ Campo no válido.")
        esperarTecla()
        return

    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        sql = f"UPDATE peliculas SET {campo} = '' WHERE id = %s"
        cursor.execute(sql, (peli_id,))
        conexion.commit()
        conexion.close()
        print(f"\n✅ El campo '{campo}' fue vaciado con éxito.")
    esperarTecla()


