#Crear un proyecto que permita gestionar, administrar peliculas  colocar un menu de opciones para agrgar, borrar, modificar mostrar, buscar, vaciar, limpiar una lista de peliculas 
#Notas: 
#Utilizar funciones y mandar llamar desde otro archivo
#Utilizar listas oara almacenar los nombres de peliculas

import peliculas

opcion=True

while opcion:
    peliculas.borrarPantalla()
    print("\n\t\t\t.::: Gestion de peliculas:::. \n\n\t 1.-Agregar\n\n\t 2.-Borrar \n\n\t 3.-Modificar\n\n\t 4.-Mostrar\n\n\t 5.-Buscar\n\n\t 6.-Limpiar\n\n\t 7.-Salir")

    opcion=input("\n\n\t Elige una opcion: ").upper()

    match opcion:
        case "1":
            peliculas.agregarPeliculas()
            peliculas.esperarTecla()
            peliculas.borrarPantalla()
        case "2":
            peliculas.borrarPeliculas
            peliculas.esperarTecla()
        case "3":
            peliculas.modificarPeliculas()
            peliculas.esperarTecla()
            peliculas.borrarPantalla()
        case "4":
            peliculas.mostrarPeliculas()
            peliculas.espereTecla()
            peliculas.borrarPantalla()
        case "5":
            peliculas.buscarPeliculas()
            peliculas.espereTecla()
            peliculas.borrarPantalla()
        case "6":
            peliculas.limpiarPeliculas()
            peliculas.espereTecla()
            peliculas.borrarPantalla()
        case "7":
            peliculas.borrarPantalla()
            print("\n\tTerminaste la ejecucion del Sistema... Gracias...")
            opcion=False
            peliculas.espereTecla()
            peliculas.borrarPantalla()
        case _:
            peliculas.BorrarPantalla()
            print("\n\tOpción inválida, vuelva a intentarlo")
            opcion=True