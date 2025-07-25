# agenda.py
import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # coloca tu contraseña si tiene
        database="agenda_db"
    )

def agregar_contacto(nombre, telefono, email):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO contactos (nombre, telefono, email) VALUES (%s, %s, %s)", (nombre, telefono, email))
        conn.commit()
        print("✔ Contacto agregado correctamente.")
    except mysql.connector.IntegrityError:
        print("❌ Ya existe un contacto con ese nombre.")
    finally:
        cursor.close()
        conn.close()

def mostrar_contactos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contactos")
    contactos = cursor.fetchall()
    print("\n📇 Lista de contactos:")
    for c in contactos:
        print(f"ID: {c[0]}, Nombre: {c[1]}, Teléfono: {c[2]}, Email: {c[3]}")
    cursor.close()
    conn.close()

def buscar_contacto(nombre):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contactos WHERE nombre = %s", (nombre,))
    contacto = cursor.fetchone()
    if contacto:
        print(f"🔍 Contacto encontrado: ID: {contacto[0]}, Nombre: {contacto[1]}, Teléfono: {contacto[2]}, Email: {contacto[3]}")
    else:
        print("⚠ No se encontró el contacto.")
    cursor.close()
    conn.close()

def eliminar_contacto(nombre):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contactos WHERE nombre = %s", (nombre,))
    conn.commit()
    if cursor.rowcount > 0:
        print("🗑 Contacto eliminado.")
    else:
        print("⚠ Contacto no encontrado.")
    cursor.close()
    conn.close()

def actualizar_contacto(nombre, nuevo_telefono, nuevo_email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE contactos SET telefono = %s, email = %s WHERE nombre = %s",
                   (nuevo_telefono, nuevo_email, nombre))
    conn.commit()
    if cursor.rowcount > 0:
        print("✅ Contacto actualizado.")
    else:
        print("⚠ Contacto no encontrado.")
    cursor.close()
    conn.close()
