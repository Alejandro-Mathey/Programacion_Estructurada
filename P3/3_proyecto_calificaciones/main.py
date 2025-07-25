import calificaciones

def main():
    opcion = True
    while opcion:
        calificaciones.borrarPantalla()
        opcion = calificaciones.menu_principal()

        match opcion:
            case "1":
                calificaciones.agregar_clalificaciones()
            case "2":
                calificaciones.mostrar_calificaciones()
            case "3":
                calificaciones.calcular_promedios()
            case "4":
                calificaciones.borrarPantalla()
                print("\n👋 Terminaste la ejecución del programa.")
                opcion = False
            case _:
                input("\n⚠️ Opción inválida, vuelve a intentarlo.")

if __name__ == "__main__":
    main()


