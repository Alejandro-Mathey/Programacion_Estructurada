import peliculas

opcion = True
while opcion:
    peliculas.borrarPantalla()
    print("\n\t\t\t..::: CINEPOLIS CLON :::..\n\t\t..::: Sistema de Gestión de Películas :::..\n")
    print("\t1. Crear Película")
    print("\t2. Borrar Todas")
    print("\t3. Mostrar")
    print("\t4. Agregar Características")
    print("\t5. Modificar Características")
    print("\t6. Borrar Características")
    print("\t7. SALIR")

    opcion = input("\n\tSelecciona una opción: ").strip()

    match opcion:
        case "1":
            peliculas.crearPeliculas()
        case "2":
            peliculas.borrarPeliculas()
        case "3":
            peliculas.mostrarPeliculas()
        case "4":
            peliculas.agregarCaracteristicaPeliculas()
        case "5":
            peliculas.modificarCaracteristicaPeliculas()
        case "6":
            peliculas.borrarCaracteristicaPeliculas()
        case "7":
            opcion = False
            peliculas.borrarPantalla()
            print("\n\t👋 Terminaste la ejecución del programa.")
        case _:
            input("\n\t⚠️ Opción inválida. Inténtalo de nuevo.")

