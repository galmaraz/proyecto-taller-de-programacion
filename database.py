import mysql.connector

class Database:
    _connection = None

    @staticmethod
    def get_connection():
        if Database._connection is None:
            try:
                Database._connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="taller"
                )
                print("Conexión establecida con la base de datos.")
            except mysql.connector.Error as err:
                print(f"Error al conectar con la base de datos: {err}")
        return Database._connection

    @staticmethod
    def close_connection():
        if Database._connection is not None:
            Database._connection.close()
            print("Conexión cerrada con la base de datos.")
