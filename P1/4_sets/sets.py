import os
'''
Es un tipo de datos para tener una cooleccion de valores pero no tiene ni indice ni orden

Set en una coleccion desordenada, inmutable* y no indexada. No hay miembros duplicados
'''

os.system("cls")
paises=["México","Brasil","España","Canada"]#lista
print(paises)
paises={"México","Brasil","España","Canada"}  #conjunto
print(paises)   # borra datos duplicados       mueve los datos al azar
varios={True,"Cadena",23,3.1416}
print(varios)

paises.add("Mexico")
print(paises)

varios.pop()
print(varios)

varios.remove("Cadena")

#Tarea

#Ejemplo de Crear un progama que solicite los email de los alumnos de la UTD alamcenar en una lista y posteriormente mostrar en pantalla los emails sin duplicarlos

def main():
    print(".::Registro de Emails de Alumnos de la UTD::.")
    
    emails = []  # Lista para almacenar los correos
    while True:
        email = input("Ingresa el email del alumno (o escribe 'salir' para terminar): ").strip()
        
        if email.lower() == 'salir':
            break
        elif '@' not in email or '.' not in email:
            print("Email inválido. Intenta de nuevo.")
        else:
            emails.append(email)

    # Eliminar duplicados usando un conjunto (set) y convertir de nuevo a lista
    emails_sin_duplicados = list(set(emails))

    # Mostrar resultados
    print("\n=== Emails registrados sin duplicados ===")
    for i, email in enumerate(emails_sin_duplicados, start=1):
        print(f"{i}. {email}")

if __name__ == "__main__":
    main()

#version del profe
emails = []
resp="si"
while resp== "si":
    emails.append(input("Escribe un Email: "))
    resp=input("¿Deseas agregar otro email? ").lower

print(emails)
emails_set=set(emails)
print(emails_set)
emails=list(emails_set)
print(emails)


