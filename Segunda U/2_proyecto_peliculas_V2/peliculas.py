"""dict u objeto para almacenar los atributos (nombre, categoria, clasificacion, genero, idioma)
pelicula = {
    "nombre": "",
    "categoria": "",
    "clasificacion": "",
    "genero": "",
    "idioma": ""
}
"""

pelicula = {}

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\tOprima cualquier tecla para continuar...\n\t")
    
def crearPeliculas():
    borrarPantalla()
    print("\n\t.:: Alta de Películas ::.\n")
    pelicula.update({"nombre": input("Ingresa el nombre: ").upper().strip()})
    pelicula.update({"categoria": input("Ingresa la categoría: ").upper().strip()})
    pelicula.update({"clasificacion": input("Ingresa la clasificación: ").upper().strip()})
    pelicula.update({"genero": input("Ingresa el género: ").upper().strip()})
    pelicula.update({"idioma": input("Ingresa el idioma: ").upper().strip()})
    #pelicula["nombre"]=input("\n Ingresa el nombre: ").upper().strinp()
    input("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")

def mostrarPeliculas():
    borrarPantalla()
    print("\n\t.:: Consultar o Mostrar la Película ::.\n")
    if len(pelicula) > 0:
        for i in pelicula:
            print(f"\t{i}: {pelicula[i]}")
    else:
        print("\t..:: No hay películas en el sistema ::..\n")

def borrarPeliculas():
    borrarPantalla()
    print("\n\t.:: Borrar o Quitar TODAS las Películas ::.\n")
    resp = input("¿Deseas quitar o borrar todas las películas del sistema? (Si/No): ").lower().strip()
    if resp == "si":
        pelicula.clear()
        input("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")

def agregarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Agregar Característica a Películas ::.\n")
    atributo = input("Ingresa la nueva característica de la película: ").lower().strip()
    valor = input("Ingresa el valor de la característica de la película: ").upper().strip()
    pelicula[atributo] = valor
    print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")

def modificarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Modificar Característica de Película ::.\n")
    
    if len(pelicula) == 0:
        print("\t..:: No hay películas registradas para modificar ::..\n")
        return

    mostrarPeliculas()
    atributo = input("\nIngresa el nombre de la característica que deseas modificar: ").lower().strip()
    
    if atributo in pelicula:
        nuevo_valor = input(f"Ingrese el nuevo valor para '{atributo}': ").upper().strip()
        if nuevo_valor:
            pelicula[atributo] = nuevo_valor
            print("\n\t\t::: ¡CARACTERÍSTICA ACTUALIZADA CON ÉXITO! :::")
        else:
            print("\n\t\t::: No se proporcionó un nuevo valor :::")
    else:
        print("\n\t\t::: La característica no existe en la película :::")

    esperarTecla()
    # if len(pelicula)>0:
    #   fori in pelicula:
    #       print(f"{i}:{pelicula[i]}")
    #       resp=input(f"\n\t Deseas modificar el valor de las caracteristicas de: {i}? (Si/No)").lower().strip()
    #       if resp =="si":
    #           


def borrarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Borrar Característica de Películas ::.\n")
    res=input("Deseas borrar alguna caracteristica? (Si/No) ").lower().strip()
    if res=="si":
        if len(pelicula) > 0:
            for clave in pelicula:
                print(f"\t{clave}: {pelicula[clave]}")
            atributo = input("\nIngresa el nombre de la característica que deseas borrar: ").lower().strip()
            if atributo in pelicula:
                del pelicula[atributo]
                print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
            else:
                print("\n\t\t::: La característica no existe :::")
        else:
            print("\t..:: No hay películas en el sistema ::..")
    else:
        esperarTecla()


"""def agregarPeliculas():
    borrarPantalla()
    print("\n\t\t.::Agregar Películas::.\n\t")
    peliculas.append(input("\nIngresa el nombre: ").upper().strip())
    print("\n\t:::¡LA OPERACIÓN SE REALIZÓ CON ÉXITO!\n\t")"""
"""def consultarPeliculas():
    borrarPantalla()
    print("\n\t\t.::Consultar o Mostrar TODAS las Películas::.\n\t")
    if len(peliculas) > 0:
        for i in range(0, len(peliculas)):
            print(f"\n\t{i+1}: {peliculas[i]}")
    else:
        print("\n\t.::No hay películas en el sistema::.\n\t")
"""
"""def vaciarPeliculas():
    borrarPantalla()
    print("\n\t\t.::Limpiar o Borrar TODAS las Películas::.\n\t")
    resp = input("¿Deseas borrar todas las películas? (Si/No)\n\t").lower()
    if resp == "si":
        peliculas.clear()
        print("\n\t:::¡LA OPERACIÓN SE REALIZÓ CON ÉXITO!:::\n\t")"""
"""ef borrarPelicula():
    borrarPantalla()
    print("\n\t\t.::Borrar Una Película::.\n\t")
    peliculabuscar = input("\n\t\t.::Dame el nombre de la película a borrar::.\n\t").upper().strip()
    if peliculabuscar in peliculas:
        resp = input("\n\t\t.::Se encontró la película::.\n\t\t.::¿Está seguro de borrar el registro de la película? (Si/No)::.\n\t").upper().strip()
        if resp == "SI":
            peliculas.remove(peliculabuscar)
            print(f"\n\tLa película se borró con éxito")
    else:
        print("\n\t.::No se encontró alguna película con este nombre, lo siento::.\n\t")"""