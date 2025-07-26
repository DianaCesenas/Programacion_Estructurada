
def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input(".:::Oprime Enter para continuar:::.")   

def menu_principal():
    print("\n\t\t\t.::: Sistema de Gestión de Agenda de Contactos :::.\n\n\t\t\t\t\t\t1️⃣ Agregar contacto\n\t\t\t\t\t\t2️⃣ Mostrar todos los contactos\n\t\t\t\t\t\t3️⃣ Buscar contacto por nombre\n\t\t\t\t\t\t4️⃣ Borrar contacto\n\t\t\t\t\t\t5️⃣ Modificar contacto por nombre\n\t\t\t\t\t\t6️⃣. SALIR")
    opcion=input("\n\t\t\t 👉 Elige una opción (1-6): ").upper().strip()
    return opcion


def agregar_contacto(agenda):
    borrarPantalla()
    print("📝Agregar contactos📝")
    nombre=input("Nombre: ").upper().strip()
    if nombre in agenda:
        print("Este contacto ya existe😲")
    else:
        tel=input("☎️Telefono:☎️ ").strip()
        email=input("📧E-mail:📧 ").lower().strip()
        agenda[nombre]=[tel,email]
        print("✨Accion Realizada con éxito✨")

def mostrar_contactos(agenda):
    borrarPantalla()
    print("👤Mostrar Contactos👤")
    if not agenda:
        print("😲No hay contactos😲")
    else:
        print(f"{'Nombre':<15} {'Telefono':<15} {'Email':<10}")
        print(f"-"*60)
        for nombre,datos in agenda.items(): #trae todo lo de los diccionarios, propia de ellos
            print(f"{nombre:<15} {datos[0]:<15} {datos[1]:<10}")    
        print(f"-"*60)

def buscar_contacto(agenda):
    borrarPantalla()
    print("🔎Buscar contactos🔍")
    if not agenda:
        print("No hay contactos a mostrar😲")
    else:
        nombre=input("Ingresa el nombre a buscar:✏️ ").upper().strip()
        if nombre in agenda:
            for nombres,datos in agenda.items(): #trae todo lo de los diccionarios, propia de ellos
                print(f"{nombres:<15} {datos[0]:<15} {datos[1]:<10}")

def  borrar_contacto(agenda):
    borrarPantalla()
    print("🗑️Borrar atributos🗑️")
    if not agenda:
        print("No hay contactos a mostrar😲")

    else:
        nombre=input("Ingresa el nombre a borrar: ").upper().strip()
        if nombre in agenda:
            # for nombres,datos in agenda.items(): #trae todo lo de los diccionarios, propia de ellos
               agenda.pop(nombre)    
        print("✨Accion realizada con exito✨")

def modificar_contacto(agenda):
    borrarPantalla()
    print("✏️Modificar contacto✏️")
    if not agenda:
        print("No hay contactos a mostrar😲")
    else:
        nombre=input("Ingresa el nombre a modificar: ").upper().strip()
        print(f" ➤Nombre: {[nombre]}")
        if nombre in agenda:
            tel=input("➤Telefono: ").strip()
            email=input("➤E-mail: ").lower().strip()
            agenda[nombre]=[tel,email]
    

