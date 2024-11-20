import mysql.connector

config = {
    'user': 'root',          
    'password': '',  
    'host': 'localhost',          
    'database': 'lol'
}

def obtener_conexion():
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        print("Conexión exitosa a la base de datos.")
        return conn, cursor
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        exit()
