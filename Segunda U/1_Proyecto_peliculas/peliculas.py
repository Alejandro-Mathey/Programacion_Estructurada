peliculas = []

def borrarPantalla():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("Oprime cualquier tecla para continuar....")

def agregarPeliculas():
    borrarPantalla()
    print("\n\t\t.:: AGREGAR PELICULAS ::.")
    nombre = input("Ingresa el nombre: ").upper().strip()
    if nombre:
        peliculas.append(nombre)
        print("\n\t\t.:: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! ::.")
    else:
        print("\n\t\t.:: Nombre no válido ::.")

def consultarPeliculas():
    borrarPantalla()
    print("\n\t\t.:: CONSULTAR PELICULAS ::.")
    if len(peliculas) > 0:
        for i in range(len(peliculas)):
            print(f"{i + 1} : {peliculas[i]}")
    else:
        print("\n\t .:: No hay Películas en el sistema ::.")

def vaciarPeliculas():
    borrarPantalla()
    print("\n\t\t.:: Limpiar o Borrar todas las Películas ::.")
    resp = input("¿Deseas borrar todas las películas? (Si/No): ").lower()
    if resp == "si":
        peliculas.clear()
        print("\n\t\t.:: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! ::.")
    else:
        print("\n\t\t.:: Operación cancelada ::.")

def eliminarPeliculas():
    consultarPeliculas()  # Muestra la lista de películas disponibles
    if len(peliculas) > 0:  # Verifica si hay películas en la lista
        try:
            idx = int(input("\nIngresa el número de la película a eliminar: "))  # Solicita un índice numérico
            if 1 <= idx <= len(peliculas):  # Asegura que el número ingresado esté dentro del rango válido
                eliminada = peliculas.pop(idx - 1)  # Elimina la película seleccionada y la guarda en 'eliminada'
                print(f"\n\t\t.:: Película '{eliminada}' eliminada con éxito ::.") 
            else:
                print("\n\t\t.:: Número fuera de rango ::.")  # Manejo de error si el número no está en el rango válido
        except ValueError:
            print("\n\t\t.:: Entrada inválida ::.")  # Manejo de error si la entrada no es un número entero
    else:
        print("\n\t\t.:: No hay películas para eliminar ::.")  # Caso en el que la lista de películas está vacía

def modificarPeliculas():
    consultarPeliculas()  
    if len(peliculas) > 0:  # Verifica si hay películas en la lista
        try:
            idx = int(input("\nIngresa el número de la película a modificar: "))  # Solicita un índice numérico
            if 1 <= idx <= len(peliculas):  # Asegura que el número ingresado esté dentro del rango válido
                nuevo = input("Ingresa el nuevo nombre: ").upper().strip()  # .upper convierte en mayúsculas y .strip elimina espacios innecesarios
                if nuevo:  # Verifica que el nuevo nombre no esté vacío
                    peliculas[idx - 1] = nuevo  # Actualiza la película en la lista
                    print("\n\t\t.:: ¡Película actualizada con éxito! ::.")  
                else:
                    print("\n\t\t.:: Nombre no válido ::.")  # Manejo de error si el nombre ingresado es vacío
            else:
                print("\n\t\t.:: Número fuera de rango ::.")  
        except ValueError:
            print("\n\t\t.:: Entrada inválida ::.")  # Manejo de error si la entrada no es un número entero
    else:
        print("\n\t\t.:: No hay películas para modificar ::.")  # Caso en el que la lista de películas está vacía

def buscarPeliculas():
    borrarPantalla()
    print("\n\t\t.:: BUSCAR PELÍCULA ::.")
    criterio = input("Ingresa el nombre o parte del nombre a buscar: ").upper().strip()  # Si criterio está dentro de peli, se agrega a la lista encontrados.
    encontrados = [peli for peli in peliculas if criterio in peli]# Recorre cada elemento peli en la lista peliculas
    if encontrados:
        print("\n\t\t.:: RESULTADOS ENCONTRADOS ::.")
        for i, peli in enumerate(encontrados, 1): # enumerate(peliculas, 1): Recorre la lista y asigna a i el índice (desde 1) y a peli el valor.
            print(f"{i} : {peli}")
    else:
        print("\n\t\t.:: No se encontraron coincidencias ::.")

