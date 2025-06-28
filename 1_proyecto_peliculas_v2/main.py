#Crear un proyecto que permita gestionar, administrar peliculas  colocar un menu de opciones para agrgar, borrar, modificar mostrar, buscar, vaciar, limpiar una lista de peliculas 
#Notas: 
#Utilizar funciones y mandar llamar desde otro archivo
#Utilizar dict oara almacenar los atributos (nombre, categoria, clasificacion, genero, idioma) de peliculas
import peliculas

opcion=True

while opcion:
    peliculas.borrarPantalla()
    print("\n\t\t\t.::: Gestion de peliculas:::. \n\n\t 1.-Crear\n\n\t 2.-Borrar \n\n\t 3.-Mostrar\n\n\t 4.-Agregar\n\n\t 5.-Modificar caracteristica\n\n\t 6.-Borrar\n\n\t 7.-Salir")

    opcion=input("\n\n\t Elige una opcion: ").upper()

    match opcion:
        case "1":
            peliculas.crearPeliculas()
            peliculas.espereTecla()
            peliculas.borrarPantalla()
        case "2":
            peliculas.borrarPeliculas
            peliculas.espereTecla()
            peliculas.borrarPantalla()
        case "3":
            peliculas.mostrarPeliculas()
            peliculas.espereTecla()
            peliculas.borrarPantalla()
        case "4":
            peliculas.agregarPeliculas()
            peliculas.espereTecla()
            peliculas.borrarPantalla()
        case "5":
            peliculas.modificarCaracteristicaPeliculas()
            peliculas.espereTecla()
            peliculas.borrarPantalla()
        case "6":
            peliculas.borrarCaracteristicaPeliculas()
            peliculas.espereTecla()
            peliculas.borrarPantalla()
        case "7":
            peliculas.borrarPantalla()
            print("\n\tTerminaste la ejecución del sistema \n\t\t -\|Gracias|/-")
            opcion=False
            peliculas.espereTecla()
            peliculas.borrarPantalla()
        case _:
             peliculas.borrarPantalla()
             print("\n\tOpción inválida, vuelva a intentarlo")
             opcion=True

           




           