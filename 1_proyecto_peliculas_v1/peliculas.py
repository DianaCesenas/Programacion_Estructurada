peliculas=() 

def borrarPantalla():
    import os
    os.system("Clear")

def espereTecla():
    input("\n\t\t Presiona una tecla para continuar ...")

def agregarPeliculas():
    borrarPantalla()
    print("\n\t\t .::: AGREGAR PELICULAS :::.\n")
    peliculas.append(input("\t Ingresa el nombre de la pelicula: ").upper().strip())
    print("\n\t\t ::: ¡LA OPERACION SE REALIZO CON EXITO! :::")

   
def mostrarPeliculas():
 borrarPantalla()
 print("\n\t ...Mostrar TODAS las peliculas...")
 if len(peliculas)>0:
    for i in range (0, len(peliculas)):
        print(f" {i+1} : {peliculas[i]} ")
    else:
        print("n\t\ ...No hay peliculas en este momento en el sistema...")   

def buscarPeliculas():
 borrarPantalla()
 print("\n\t\t .::: BUSCAR PELICULAS :::.\n")
 pelicula_buscar=input("Ingrese el nombre de la pelicula a buscar: ").upper().strip()
 if not (pelicula_buscar in peliculas):
   print("\n\t....Esta pelicula no se encuentra en el sistema...")
 else:
     encontro=0
     for i in range(0,len(peliculas)):
            if pelicula_buscar==peliculas[i]:
                print(f"\n\tla pelicula {pelicula_buscar} se encontro en el casillero: {i+1}")
                encontro+=1
     print(f"\n\t Tenemos {encontro} pelicula(s) con este titulo")
     print("\n\t\t...LA OPERACION SE REALIZO CON EXITO...")

       
def limpiarPeliculas():
    borrarPantalla()
    print("\n\t ...Limpair o borrar TODAS las peliculas...\n")
    resp=input("Deseas borrar todas las peliculas del sistema? (Si/No)").lower().strip()
    if resp=="si":
        peliculas.clear()
        print("\n\t\t ::: ¡LA OPERACION SE REALIZO CON EXITO! :::")

def modificarPeliculas():
 borrarPantalla()
 print("\n\t ...Modificar peliculas...")
 pelicula_buscar=input("Ingrese el nombre de la pelicula que desea buscar: ").upper().strip()
 encontro=0
 if not (pelicula_buscar in peliculas):
  print("\n\t....Esta pelicula no se encuentra en el sistema...")
 else:
     for i in range(0,len(peliculas)):
        if pelicula_buscar==peliculas[i]:
            resp=input("Deseas actualizar la pelicula? (Si/No)").lower()


def borrarPeliculas():
 borrarPantalla()
 print("\n\t ...Borrar peliculas...")
 pelicula_borrar=input("Ingrese el nombre de la pelicula que desea borrar: ").upper().strip()
 resp=input("Deseas quitar o borrar la peliculas del sistema? (Si/No)").lower().strip()
 if resp=="si":
    peliculas.remove
 if not (pelicula_borrar in peliculas):
   print("\n\t....Esta pelicula no se encuentra en el sistema...")
 else:
     encontro=0
     for i in range(0,len(peliculas)):
            if pelicula_borrar==peliculas[i]:
                print(f"\n\tla pelicula que se borro es: {pelicula_borrar} y estaba en la casilla {i+1}")
                encontro+=1
     print(f"\n\t Se borro {encontro} pelicula(s) con este titulo")
     print("\n\t\t...LA OPERACION SE REALIZO CON EXITO...")



#strip es para eliminar espacios
#len funcion que te saca el tamano