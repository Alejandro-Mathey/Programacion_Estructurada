import os
"""
 dict.- 
  Es un tipo de datos que se utiliza para almacenar datos de diferente tipo de datos pero en lugar de tener como las listas indices numericos tiene alfanumericos. Es decir es algo parecido como los Objetos 

  Tambien se conoce como un arreglo asosiativo u Objeto JSON

  El diccionario es una colección ordenada** y modificable. No hay miembros duplicados.
"""
os.system("cls")


pais1={"nombre":"México",
      "capital":"CDMX",
      "poblacion":12000,
      "idioma":"español",
      "status":True
        }

pais2={"nombre":"Brasil",
      "capital":"Brasilia",
      "poblacion":12000,
      "idioma":"español",
      "status":True
        }

pais3={"nombre":"Canada",
      "capital":"Otawua",
      "poblacion":1000000,
      "idioma":["ingles","franses"],
      "status":True
        }

#funciones u operaciones con los diccionarios
print(pais1)
for i in pais1:
    print(f"{i}={pais1[i]}")

#agragar un atributo a dic
pais1["altitud"]=3000
for i in pais1:
    print(f"{i}={pais1[i]}")
#Quitar
pais1.pop("status")
for i in pais1:
    print(f"{i}={pais1[i]}")