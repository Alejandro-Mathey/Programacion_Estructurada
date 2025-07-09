contactos = []

def borrarPantalla():
    import os
    os.system('cls')

def esperarTecla():
    input("\n\tOprime cualquier tecla para continuar...")

def agregarContactos():
    print(".:: Agregar Contacto ::.")
    nombre = input("Nombre del contacto: ").upper().strip()
    telefono = input("Teléfono: ").strip()
    email = input("Email: ").strip()
    if nombre and telefono:
        contactos.append([nombre, telefono, email])
        print("✅ Contacto agregado exitosamente.")
    else:
        print("⚠️ Nombre y teléfono son obligatorios.")
    esperarTecla()

def mostrarContactos():
    print(".:: Lista de Contactos ::.")
    if contactos:
        print(f"{'ID':<5}{'Nombre':<20}{'Teléfono':<15}{'Email':<25}")
        print("-" * 70)
        for i, c in enumerate(contactos):
            print(f"{i:<5}{c[0]:<20}{c[1]:<15}{c[2]:<25}")
        print("-" * 70)
        print(f"Total: {len(contactos)} contacto(s)")
    else:
        print("📭 No hay contactos registrados.")
    esperarTecla()

def buscarContactos():
    print(".:: Buscar Contacto ::.")
    nombre = input("Ingresa el nombre a buscar: ").upper().strip()
    encontrados = [c for c in contactos if nombre in c[0]]
    if encontrados:
        print(f"\n{'Nombre':<20}{'Teléfono':<15}{'Email':<25}")
        print("-" * 60)
        for c in encontrados:
            print(f"{c[0]:<20}{c[1]:<15}{c[2]:<25}")
    else:
        print("🔍 No se encontraron coincidencias.")
    esperarTecla()

def modificarContactos():
    mostrarContactos()
    try:
        idx = int(input("Ingresa el ID del contacto que deseas modificar: "))
        if 0 <= idx < len(contactos):
            print("Deja vacío el campo para conservar el valor actual.")
            nombre = input("Nuevo nombre: ").upper().strip()
            telefono = input("Nuevo teléfono: ").strip()
            email = input("Nuevo email: ").strip()

            if nombre:
                contactos[idx][0] = nombre
            if telefono:
                contactos[idx][1] = telefono
            if email:
                contactos[idx][2] = email

            print("✅ Contacto modificado exitosamente.")
        else:
            print("❌ ID inválido.")
    except ValueError:
        print("⚠️ Ingresa un número válido.")
    esperarTecla()

def eliminarContactos():
    mostrarContactos()
    try:
        idx = int(input("Ingresa el ID del contacto que deseas eliminar: "))
        if 0 <= idx < len(contactos):
            confirm = input(f"¿Estás seguro de eliminar a {contactos[idx][0]}? (S/N): ").upper()
            if confirm == 'S':
                contactos.pop(idx)
                print("🗑️ Contacto eliminado exitosamente.")
            else:
                print("❎ Operación cancelada.")
        else:
            print("❌ ID no válido.")
    except ValueError:
        print("⚠️ Ingresa un número válido.")
    esperarTecla()

def menu():
    borrarPantalla()
    print("\n📋 Sistema de Gestión de Contactos 📋\n")
    print("1️⃣ Agregar Contacto")
    print("2️⃣ Mostrar Todos los Contactos")
    print("3️⃣ Buscar Contacto por Nombre")
    print("4️⃣ Modificar Contacto")
    print("5️⃣ Eliminar Contacto")
    print("6️⃣ Salir")
    return input("\n👉 Elige una opción (1-6): ").strip()

def main():
    while True:
        opcion = menu()
        match opcion:
            case '1':
                borrarPantalla()
                agregarContactos()
            case '2':
                borrarPantalla()
                mostrarContactos()
            case '3':
                borrarPantalla()
                buscarContactos()
            case '4':
                borrarPantalla()
                modificarContactos()
            case '5':
                borrarPantalla()
                eliminarContactos()
            case '6':
                print("👋 Saliste del programa.")
                break
            case _:
                print("❌ Opción no válida. Intenta de nuevo.")
                esperarTecla()

if __name__ == "__main__":
    main()
