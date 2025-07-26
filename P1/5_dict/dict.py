"""

 dict.- 
  Es un tipo de datos que se utiliza para almacenar datos de diferente tipo de datos pero en 
  lugar de tener como las listas indices numericos tiene alfanumericos. 
  Es decir, es algo parecido como los Objetos 

  Tambien se conoce como un arreglo asosiativo u Objeto JSON

  El diccionario es una colección ordenada** y modificable. No hay miembros duplicados.
"""
import os
os.system("clear")

paises=["Mexico","Brasil","Canada"]

pais1={
      "nombre":"Mexico",
      "Capital":"CDMX",
      "poblacion":1222222222,
      "idioma":"español",
      "status":True
      } 

pais2={
      "nombre":"Brasil",
      "Capital":"Brasilia",
      "poblacion":1222222222,
      "idioma":"portugues",
      "status":True
      }

pais3={
      "nombre":"Canada",
      "Capital":"Otawa",
      "poblacion":1222222222,
      "idioma":["ingles","frances"],
      "status":True
}

for i in pais1:
    print(f"{i}={pais1[i]}")

#agregar un atributo. no existe el append
pais1["altitud"]=3000
for i in pais1:
    print(f"{i}={pais1[i]}")