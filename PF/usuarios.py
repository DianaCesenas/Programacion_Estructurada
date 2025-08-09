
import datetime
import hashlib
from conexionBD import *
def hash_password(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def registrar(email,contrasena):
    try:
        fecha=datetime.datetime.now()
        contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
        cursor.execute(
            "INSERT INTO usuarios (id,  email, password) VALUES (NULL,%s, %s)", (email, contrasena)
        )
        conexion.commit()
        return True
    except:
        print("Error") 
        return False
           

def iniciar_sesion(email,contrasena):
    try:
        contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
        cursor.execute(
            "select * from usuarios where email=%s and password=%s", (email, contrasena)
        )
        registros=cursor.fetchone()
        if registros:
            return registros
        else:
            return None
    except:
        print("Error")
        return None
         