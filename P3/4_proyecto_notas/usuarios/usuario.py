from conexionBD import *
import datetime

def registrar(nombre,apellidos,email,contrasena):
    try:
        fecha=datetime.datetime.now()
        sql="insert into usuarios (nombre,apellidos,email,password,fecha) values (%s,%s,%s,%s,%s)"
        val=(nombre,apellidos,email,contrasena,fecha)
        cursor.execute(sql,val)
        conexion.commit()
        return True
    except:
        return False
    
def iniciar_secion(email,contrasena):
    try:
        sql=""
        val=()
        cursor.execute(val,sql)
        registro=cursor.fetchone()
        if registro:
            return registro
        else:
            return None
    except:
        return False