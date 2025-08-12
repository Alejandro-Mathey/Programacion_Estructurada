import funciones
from usuarios import usuario
from registros import registro
from consultas import consulta
from modificaciones import modificaciones
import getpass

def main():
    opcion = True
    while opcion:
        funciones.borrarPantalla()
        opcion = funciones.menu_usurios()

        if opcion == "1" or opcion.upper() == "REGISTRO":
            funciones.borrarPantalla()
            print("\n\t📝 ..:: Registro en el Sistema ::..\n")
            nombre = input("\t👤 ¿Cuál es tu nombre?: ").upper().strip()
            apellidos = input("\t👥 ¿Cuáles son tus apellidos?: ").upper().strip()
            email = input("\t📧 Ingresa tu email: ").lower().strip()
            contrasena = getpass.getpass("\t🔒 Ingresa tu contraseña: ").strip()
            # Mostrar lista de equipos antes de pedir ID
            try:
                from conexionBD import cursor
                cursor.execute("SELECT id_equipo, nombre_equipo, categoria FROM equipos")
                equipos = cursor.fetchall()
                if equipos:
                    print("\n📋 Lista de equipos registrados:")
                    for eq in equipos:
                        print(f"  ID: {eq[0]} | Nombre: {eq[1]} | Categoría: {eq[2]}")
                else:
                    print("\n⚠️ No hay equipos registrados en el sistema.")
            except Exception as e:
                print(f"❌ Error al obtener equipos: {e}")

            # Ahora pedir al usuario que elija ID o deje vacío
            id_equipo_input = input("\nCual equipo deseas ingresar (escribe ID o deja vacío): ").strip()
            if id_equipo_input == "":
                id_equipo = None
            else:
                try:
                    id_equipo = int(id_equipo_input)
                except ValueError:
                    id_equipo = id_equipo_input  # por si alguna vez quieres permitir nombres

            regresar = usuario.registrar(nombre, apellidos, email, contrasena, id_equipo)

            if regresar:
                print(f"\n✅ {nombre} {apellidos} se registró correctamente con el e-mail: {email}\n")
            else:
                print("\n❌ No fue posible realizar el registro. Intenta de nuevo.\n")
            funciones.esperarTecla()

        elif opcion == "2" or opcion.upper() == "INICIAR":
            funciones.borrarPantalla()
            print("\n\t🔐 ..:: Inicio de Sesión ::..\n")
            email = input("\t📧 Ingresa tu E-mail: ").lower().strip()
            contrasena = getpass.getpass("\t🔒 Ingresa tu contraseña: ").strip()

            lista_usuario = usuario.iniciar_sesion(email, contrasena)

            if lista_usuario:
                nombre, apellidos, email = lista_usuario[:3]
                print(f"\n✅ Bienvenido {apellidos} {email}\n")
                funciones.esperarTecla()
                menu_sistema()
            else:
                print("\n❌ El E-mail y/o contraseña son incorrectos.\n")
                funciones.esperarTecla()

        elif opcion == "3" or opcion.upper() == "PARTIDOS":
            funciones.borrarPantalla()
            consulta.mostrarPartidosConJugadores()

        elif opcion == "4" or opcion.upper() == "MOSTRAR":
            funciones.borrarPantalla()
            consulta.mostrarJugadores()

        elif opcion == "5" or opcion.upper() == "SALIR":
            print("\n🚪 Terminó la ejecución del sistema.\n")
            opcion = False
            funciones.esperarTecla()

        else:
            print("\n❌ Opción no válida.\n")
            funciones.esperarTecla()

def menu_sistema():
    while True:
        funciones.borrarPantalla()
        print("\n\t⚽️ ..::: SISTEMA PRINCIPAL DEPORTIVO :::.. ⚽️\n")
        print("\t..::: Academia de Futbol Tuzos Drilling :::..\n")
        print("\t1️⃣\t📋 Ir al menú de Registro")
        print("\t2️⃣\t🔍 Ir al menú de Consulta")
        print("\t3️⃣\t🔙 Volver al menú de usuario")
        print("\t4️⃣\t🚪 Salir del sistema\n")

        opcion = input("👉 Elige una opción: ").strip()

        if opcion == "1":
            menu_registro()
        elif opcion == "2":
            menu_consulta()
        elif opcion == "3":
            # Volver al menú principal de usuarios
            break
        elif opcion == "4":
            registro.borrarPantalla()
            print("\n🎉 Gracias por usar el sistema. ¡Hasta pronto!\n")
            exit()  # Salir del programa completamente
        else:
            input("❌ Opción inválida. Intenta de nuevo...")

def menu_registro():
    while True:
        registro.borrarPantalla()
        print("\n\t📋 ..::: MENÚ DE REGISTRO :::.. 📋\n")
        print("\t1️⃣\t Inscribir jugador")
        print("\t2️⃣\t Registrar día de entrenamiento")
        print("\t3️⃣\t Registrar partido")
        print("\t4️⃣\t Registrar torneo")
        print("\t5️⃣\t Vaciar registros")
        print("\t6️⃣\t Editar o borrar un registro específico")
        print("\t7️⃣\t🔙 Volver al menú principal\n")

        opcion = input("👉 Elige una opción: ").strip()

        match opcion:
            case "1":
                registro.registrarJugador()
                registro.esperarTecla()
            case "2":
                registro.agregarHorario()
                registro.esperarTecla()
            case "3":
                registro.registrarPartido()
                registro.esperarTecla()
            case "4":
                registro.registrarTorneo()
                registro.esperarTecla()
            case "5":
                registro.vaciarRegistros()
                registro.esperarTecla()
            case "6":
                modificaciones.menu_modificaciones()
                registro.esperarTecla()
            case "7":
                break
            case _:
                input("❌ Opción inválida. Intenta de nuevo...")

def menu_consulta():
    while True:
        registro.borrarPantalla()
        print("\n\t🔍 ..::: MENÚ DE CONSULTA :::.. 🔍\n")
        print("\t1️⃣\t Consultar jugador")
        print("\t2️⃣\t Consultar días de entrenamiento")
        print("\t3️⃣\t Consultar partidos por día")
        print("\t4️⃣\t Consultar torneos")
        print("\t5️⃣\t🔙 Volver al menú principal\n")

        opcion = input("👉 Elige una opción: ").strip()

        match opcion:
            case "1":
                consulta.consultarJugador()
                registro.esperarTecla()
            case "2":
                consulta.consultarDiasEntrenamiento()
                registro.esperarTecla()
            case "3":
                consulta.consultarPartidosPorDia()
                registro.esperarTecla()
            case "4":
                consulta.consultarTorneo()
                registro.esperarTecla()
            case "5":
                break
            case _:
                input("❌ Opción inválida. Intenta de nuevo...")

if __name__ == "__main__":
    main()
