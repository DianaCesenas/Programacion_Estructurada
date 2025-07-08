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
 if len(pelicula) > 0:
    for i in pelicula:
     print(f" {i} : Las peliculas disponibles en es sistema son: {pelicula[i]} ")
     print("\n\n\t ||| LA OPERACIÓN SE REALIZÓ CON ÉXITO |||")
    else:
        print("\n---La lista se encuentra vacía---\n")
       
def borrarPeliculas():
    borrarPantalla()
    print("\n\t\t-.::Borrar película::./-")
    if len(pelicula) > 0:
        resp="a"
        while resp!="si" and resp!="no":
            resp=input("\n\n\t\t¡¡CUIDADO!!\n\n¿Desea borrar la película registrada?\n(si/no): ").lower().strip()
            match resp:
                case "si":
                    pelicula.clear()
                    print("\n\t .::LA OPERACIÓN SE REALIZÓ CON ÉXITO::.")
                case "no":
                    print("\n\t--Operacion cancelada--")
                case _:
                    borrarPantalla()
                    print("Operación no válida, vuelva a intentarlo")
                    print("\n\t\t-.::Borrar película::.-")
                    resp="a"
    else:
        print("\n---No se puede borrar porque no hay película en el sistema---")      

def agregarCaracteristica():
    borrarPantalla()
    opc="si"
    print("\n\t\t .::Agregar características a la película::.\n")
    while opc=="si":
        cate=input("Ingrese la característica a agregar: ").lower().strip()
        pelicula.update({cate:input(f"Ingrese el valor de la característica {cate}: ").lower().strip()})
        opc="¿Desea agregar alguna otra característica?\n(si/no): " 
    print("\n\t --LA OPERACIÓN SE REALIZÓ CON ÉXITO--")        
       
def modificarCaracteristicaPelicula():
    borrarPantalla()
    print("\n\t\t-\|Modificar características a la película|/-\n")
    if len(pelicula) > 0:
        for i in pelicula:
            print(f"valor actual de {i}: {pelicula[i]}")
            opc=input(f"¿Desea modificar el valor del {i}?\n(si/no): ").lower().strip()
            if opc=="si":
                if i=="clasificacion":
                    pelicula[i]=input(f"Ingrese el nuevo valor del {i}: ").upper().strip()
                else:
                    pelicula[i]=input(f"Ingrese el nuevo valor del {i}: ").lower().strip()
        
        print("\n\t --LA OPERACIÓN SE REALIZÓ CON ÉXITO--")
    else:
        print("\n---No se puede modificar porque no hay película en el sistema---")   

def borrarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t\t .:Borrar una caracterísitica a la película::. \n")
    if len(pelicula) > 0:
        print("\tValores actuales:")
        for i in pelicula:
            print(f"{i} : {pelicula[i]}")
        opc=input("\n¿Desea borrar alguna característica? \n(si/no): ").lower().strip()
        match opc:
            case "si":
                cara=input("Ingresa la característica a borrar/quitar: ").lower().strip()
                if cara in pelicula:
                    pelicula.pop(cara)
                    print("\n\t ¡¡LA OPERACIÓN SE REALIZÓ CON ÉXITO!!")
                else:
                    print("--No se encuentra la característica anterior--")
            case "no":
                print("\n\t--Operacion Cancelada--")
            case _:
                print("\n\t--La opción no es correcta--")
    else:
        print("\n - No es posible borrar, sistema vacio -")
#strip es para eliminar espacios
#len funcion que te saca el tamano