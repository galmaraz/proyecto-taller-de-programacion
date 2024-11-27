import mysql.connector

class Database:
    _connection = None
    _cursor = None

    @staticmethod
    def connect():
        """Establece la conexión a la base de datos si no está conectada."""
        if Database._connection is None:
            try:
                Database._connection = mysql.connector.connect(
                    host="localhost",
                    user="root",  # Cambiar según tu configuración
                    password="",  # Cambiar si usas contraseña
                    database="LOL"  # Nombre de la base de datos
                )
                Database._cursor = Database._connection.cursor(buffered=True)
                print("Conexión establecida con la base de datos.")
            except mysql.connector.Error as err:
                print(f"Error al conectar con la base de datos: {err}")

    @staticmethod
    def get_connection():
        """Devuelve la conexión activa a la base de datos."""
        if Database._connection is None:
            Database.connect()
        return Database._connection

    @staticmethod
    def execute_query(query, params=None):
        """Ejecuta consultas SQL."""
        try:
            if Database._cursor is None:
                raise Exception("No hay conexión activa con la base de datos.")
            if params:
                Database._cursor.execute(query, params)
            else:
                Database._cursor.execute(query)

            if query.strip().upper().startswith("SELECT"):
                return Database._cursor.fetchall()
            else:
                Database._connection.commit()
                return True
        except mysql.connector.Error as err:
            print(f"Error al ejecutar la consulta: {err}")
            return False

    @staticmethod
    def close():
        """Cierra la conexión y el cursor."""
        if Database._cursor is not None:
            Database._cursor.close()
        if Database._connection is not None:
            Database._connection.close()
            Database._connection = None
            Database._cursor = None
            print("Conexión cerrada con la base de datos.")
