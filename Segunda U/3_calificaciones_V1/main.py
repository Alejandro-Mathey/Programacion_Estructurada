'''Crear un proyecto que permita gestionar (Administar) calificaciones, colocar un menu de opciones para agregar, mostrar, y calcular el promedio de calificaciones

Notas
1.- Utilizar funciones y mandar a llamar desde otro arcivo
2.- Utilizar listas para almacenar los siguinetes archivos: ( nombre y 3 calificacones de los alumnos).
'''

import calificaciones

def main():
    opcion = True
    lista=[]
    while opcion:
        calificaciones.borrarPantalla()
        opcion=calificaciones.menu_principal()

        match opcion:
            case "1":
                calificaciones.agregar_clalificaciones(lista)
                calificaciones.esperarTecla()
            case "2":
                calificaciones.mostrar_calificaciones(lista)
                calificaciones.esperarTecla()
            case "3":
                calificaciones.calcular_promedios(lista)
                calificaciones.esperarTecla()
            case "4":
                opcion = False
                calificaciones.borrarPantalla()
                print("\n\tTerminaste la ejecucion del SW")
            case _:
                opcion = True
                input("\n\tOpción inválida, vuelva a intentarlo.... por favor")

if __name__ == "__main__":#Ejecuta fuera de la terminal
    main()