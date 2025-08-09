import mysql.connector
import csv
import funciones

try:
    conexion = mysql.connector.connect(
        host="::1", user="root", password="", database="db_farmacia", use_pure=True
    )
    confirm = True
    cursor = conexion.cursor(buffered=True)
except mysql.connector.errors.ProgrammingError:
    try:
        conexion = mysql.connector.connect(
            host="::1", user="root", password="", use_pure=True
        )
        cursor = conexion.cursor(buffered=True)
    except:
        print(
            f"En este momento no posible comunicarse con el sistema, intentelo mas tarde ..."
        )
    else:
        cursor.execute("CREATE DATABASE db_farmacia")
        cursor.execute("USE db_farmacia")
except:
    print(
        f"En este momento no posible comunicarse con el sistema, intentelo mas tarde ..."
    )
if confirm:
    cursor.execute("SHOW TABLES")
    a = cursor.fetchall()
    if ("medicamentos",) not in a:
        valores = "tabla_medicamentos.csv"
        with open(valores, mode="r", encoding="utf-8") as archivo:
            lector_csv = csv.reader(archivo)
            print(lector_csv)
            fila1 = next(lector_csv)
        cursor.execute(
            """
CREATE TABLE IF NOT EXISTS medicamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_marca VARCHAR(50),
    compuesto_activo VARCHAR(200),
    caducidad DATE,
    concentracion INT,
    presentacion VARCHAR(25),
    cantidad INT,
    precio DECIMAL(8,2),
    laboratorio VARCHAR(25)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
"""
        )


def tabla_med_upd():
    valores = "tabla_medicamentos.csv"
    with open(valores, mode="r", encoding="utf-8") as archivo:
        lector_csv = csv.reader(archivo)
        next(lector_csv)  # Saltar encabezados

        nuevos = 0
        for fila in lector_csv:
            sql = """
            INSERT INTO medicamentos 
            (nombre_marca, compuesto_activo, caducidad, concentracion, presentacion, cantidad, precio, laboratorio)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, fila)
            nuevos += 1

    conexion.commit()
    print(f"{nuevos} medicamentos insertados correctamente.")


tabla_med_upd()


def tabla_ventas():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ventas (
        id_venta INT AUTO_INCREMENT PRIMARY KEY,
        fecha_venta DATETIME DEFAULT NOW(),
        metodo_pago ENUM('efectivo', 'transferencia') NOT NULL,
        monto_pagado DECIMAL(10,2),
        cambio DECIMAL(10,2)
    );
    """) #este bloque crea la tabla de la venta global
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS detalle_venta (
        id_detalle INT AUTO_INCREMENT PRIMARY KEY,
        id_venta INT NOT NULL,
        id_medicamento INT NOT NULL,
        cantidad INT NOT NULL,
        precio_unitario DECIMAL(10,2) NOT NULL,
        total DECIMAL(10,2) NOT NULL,
        FOREIGN KEY (id_venta) REFERENCES ventas(id_venta),
        FOREIGN KEY (id_medicamento) REFERENCES medicamentos(id)
    );
    """) #este bloque crea la tabla del detalle de la venta


    conexion.commit()
    print("tabla creada")

tabla_ventas()

def tablas_usuarios():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id_usuario INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR (50),
        contrasena VARCHAR(25)
    );
    """)
    conexion.commit()
    print("tabla creada")

tablas_usuarios()