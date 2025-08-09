from conexionBD import *
import funciones
print("se importo funciones")
import datetime

def crear (id_venta, id_medicamentos ):
    try:
        fecha=datetime.datetime.now()
        cursor.execute("INSERT INTO ventas (id_venta, fecha_venta, id_medicamentos, cantidad, precio_unitario, total) VALUES (%s, NOW(), %s, %s, %s, %s)",
                       )
        conexion.commit()
        return True
    except:
        return False    
    
def cargar_medicamentos():
    cursor.execute("SELECT id, nombre_marca, precio, cantidad FROM medicamentos;")
    medicamentos = cursor.fetchall()
    return medicamentos
meds = cargar_medicamentos()
print(f"Medicamentos cargados: {len(meds)}")
for med in meds:
    print(f"{med[0]}: {med[1]} - ${med[2]} (Stock: {med[3]})")


