# main.py
import agenda

def menu():
    while True:
        print("\n📒 AGENDA DE CONTACTOS")
        print("1. Agregar contacto")
        print("2. Mostrar todos los contactos")
        print("3. Buscar contacto")
        print("4. Eliminar contacto")
        print("5. Actualizar contacto")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            agenda.agregar_contacto(nombre, telefono, email)
        elif opcion == "2":
            agenda.mostrar_contactos()
        elif opcion == "3":
            nombre = input("Nombre del contacto a buscar: ")
            agenda.buscar_contacto(nombre)
        elif opcion == "4":
            nombre = input("Nombre del contacto a eliminar: ")
            agenda.eliminar_contacto(nombre)
        elif opcion == "5":
            nombre = input("Nombre del contacto a actualizar: ")
            nuevo_telefono = input("Nuevo teléfono: ")
            nuevo_email = input("Nuevo email: ")
            agenda.actualizar_contacto(nombre, nuevo_telefono, nuevo_email)
        elif opcion == "6":
            print("👋 Saliendo...")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
