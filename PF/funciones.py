#Importaciones
import os
import platform
import mysql.connector
#Funciones
def BorrarPantalla():
    s = platform.system()
    if s == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def EsperarTecla():
    input("\n\n\t\t \U0001F552 ...Presiona enter para continuar... \U0001F552")

def menu_principal():
    print("\n \U0001F4DD .::Sistema de Gestion de Inventario de Farmacia::. \U0001F4DD \n\t 1.-Agregar \n\t 2.-Borrar \n\t 3.-Mostrar \n\t 4.-Buscar \n\t 5.-Vendido \n\t 6.-Salir")
    opcion = input("Elige una opcion (1-6): ")
    return opcion

def conexion():
    conexion=mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="farmacia"
    )
    cursor=conexion.cursor(buffered=True)
