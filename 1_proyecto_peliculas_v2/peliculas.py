#Dict u objeto que me permita almacenar los siguientes atributos:(nombre, categoria, clasificacion, genero, idioma) de peliculas
#pelicula={"nombre":"",
          #"categoria":"",
          #"clasificacion":"",
          #"genero":"",
          #"idioma":""}

pelicula = {}
def borrarPantalla():
    import os
    os.system("Clear")


def espereTecla():
    input("\n\t\t Presiona una tecla para continuar ...")


def crearPeliculas():
   borrarPantalla()
   print("\n\t\t .::: AGREGAR PELICULAS :::.\n")
   pelicula.update({"nombre":  input ("Ingresa el nombre: ").upper().strip()})
   pelicula.update({"categoria":  input ("Ingresa la categoria: ").upper().strip()})
   pelicula.update({"clasificacion":  input ("Ingresa la clasificacion: ").upper().strip()})
   pelicula.update({"genero":  input ("Ingresa el genero: ").upper().strip()})
   pelicula.update({"idioma":  input ("Ingresa el idioma: ").upper().strip()})
   print("\n\t\t ::: ¡LA OPERACION SE REALIZO CON EXITO! :::")


def agregarPeliculas():
    borrarPantalla()
    print("\n\t\t .::: AGREGAR PELICULAS :::.\n")
    pelicula.append(input("\t Ingresa el nombre de la pelicula: ").upper().strip())
    print("\n\t\t ::: ¡LA OPERACION SE REALIZO CON EXITO! :::")


def mostrarPeliculas():
 borrarPantalla()
 print("\n\t ...Mostrar las peliculas...")
 if len(pelicula)>0:
    for i in range (0, len(pelicula)):
        print(f" {i+1} : Las peliculas disponibles en es sistema son: {pelicula[i]} ")
    else:
        print("\n\t ...No hay peliculas en este momento en el sistema...")   


#def buscarPeliculas():
 #borrarPantalla()
 #print("\n\t\t .::: BUSCAR PELICULAS :::.\n")
 #pelicula_buscar=input("Ingrese el nombre de la pelicula a buscar: ").upper().strip()
 #if not (pelicula_buscar in peliculas):
   #print("\n\t....Esta pelicula no se encuentra en el sistema...")
 #else:
     #encontro=0
     #for i in range(0,len(peliculas)):
            #if pelicula_buscar==peliculas[i]:
                #print(f"\n\tla pelicula {pelicula_buscar} se encontro en el casillero: {i+1}")
                #encontro+=1
     #print(f"\n\t Tenemos {encontro} pelicula(s) con este titulo")
     #print("\n\t\t...LA OPERACION SE REALIZO CON EXITO...")


#def limpiarPeliculas():
    #borrarPantalla()
    #print("\n\t ...Limpair o borrar TODAS las peliculas...\n")
    #resp=input("Deseas borrar todas las peliculas del sistema? (Si/No)").lower().strip()
    #if resp=="si":
        #peliculas.clear()
        #print("\n\t\t ::: ¡LA OPERACION SE REALIZO CON EXITO! :::")

def modificarPeliculas():
 borrarPantalla()
 print("\n\t ...Modificar peliculas...")
 pelicula_buscar=input("Ingrese el nombre de la pelicula que desea buscar: ").upper().strip()
 encontro=0
 if not (pelicula_buscar in pelicula):
  print("\n\t....Esta pelicula no se encuentra en el sistema...")
 else:
     for i in range(0,len(pelicula)):
        if pelicula_buscar==peliculas[i]:
            resp=input("Deseas actualizar la pelicula? (Si/No)").lower()

def borrarPeliculas():
 borrarPantalla()
 print("\n\t ...Borrar peliculas...")
 borrarPantalla()
 print("\n\t ...Mostrar las peliculas...")
 if len(pelicula)>0:
    resp = input("Deseas borrar o quitar la pelicula? (Si/No)").lower().strip()
    if resp =="si":
     pelicula.clear()
    else:
        print("\n\t ...No hay peliculas en este momento en el sistema...")   


def agregarCaracteristicaPeliculas():
   borrarPantalla()
   print("\n\t .::Agregar una caracteristica de Pelicula::.\n")
   atributo = input("Ingresa el nombre de la nueva caracteristica que deseas agregar: ").lower().strip()
   valor_atributo = input("Ingresa el valor de la nueva caracteristica que deseas agregar: ").upper().strip()
   pelicula.update({atributo:valor_atributo}) 
   print("\n\t\t...LA OPERACION SE REALIZO CON EXITO...") 

def modificarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.::Modificar una característica de Película::.\n")
    if len(pelicula)>0:
        for i in pelicula:
            print(pelicula[i])
            op=input("¿Deseas modificar este atributo?: ").lower().strip()
            if op=="si":
                pelicula[i]=input(".::Introduce el nuevo nombre del atributo: ").lower().strip()
                print("\n\t\t :::¡LA OPERACION SE REALIZÓ CON ÉXITO!:::")
    else:
        borrarPantalla()
#strip es para eliminar espacios
#len funcion que te saca el tamano