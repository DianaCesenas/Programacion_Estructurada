import calificaciones

def main():
    datos = []
    opcion = True

    while opcion:
        calificaciones.borrarPantalla()
        calificaciones.menu_principal()

        match opcion:
            case "1":
                calificaciones.agregar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "2":
                calificaciones.mostrar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "3":
                calificaciones.calcular_promedios(datos)
                calificaciones.esperarTecla()
            case "4":
                opcion = False



if __name__ == "__main__":
    main()











    