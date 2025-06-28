import peliculas

opcion = True
while opcion:
    peliculas.borrarPantalla()
    print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Peliculas :::...\n 1.- Agregar  \n 2.- Eliminar \n 3.- Actualizar \n 4.- Consultar \n 5.- Buscar \n 6.- Vaciar \n 7.- SALIR ")
    opcion = input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.agregarPeliculas()
            peliculas.esperarTecla()
        case "2":
            print(".:: Eliminar Peliculas ::.")
            input("Oprima cualquier tecla para continuar ...")
            peliculas.eliminarPeliculas()
            peliculas.esperarTecla()
        case "3":
            print(".:: Modificar Peliculas ::.")
            input("Oprima cualquier tecla para continuar ...")
            peliculas.modificarPeliculas()
            peliculas.esperarTecla()
        case "4":
            peliculas.consultarPeliculas()
            peliculas.esperarTecla()
        case "5":
            peliculas.buscarPeliculas()
            peliculas.esperarTecla()
        case "6":
            peliculas.vaciarPeliculas()
            peliculas.esperarTecla()
        case "7":
            opcion = False
            peliculas.borrarPantalla()
            print("\n\t\tTerminaste la ejecución del SW")
        case _:
            opcion = True
            input("Opción inválida. Vuelva a intentarlo ... por favor")
