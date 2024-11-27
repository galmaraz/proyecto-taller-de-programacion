import bcrypt
from database import Database

class Crear:
    def __init__(self):
        self.connection = Database.get_connection()  # Ahora funciona correctamente
        
class IniciarSesion:
    def __init__(self):
        self.connection = Database.get_connection()  # Ahora funciona correctamente

    def cuenta_usuario(self, correo_electronico, contraseña, tipo_rol):
        """Crea una nueva cuenta de usuario."""
        cursor = self.connection.cursor()
        try:
            salt = bcrypt.gensalt()
            contraseña_hash = bcrypt.hashpw(contraseña.encode('utf-8'), salt)
            sql = "INSERT INTO usuarios (correo, contraseña, rol) VALUES (%s, %s, %s)"
            cursor.execute(sql, (correo_electronico, contraseña_hash, tipo_rol))
            self.connection.commit()
            print(f"Usuario '{correo_electronico}' creado como '{tipo_rol}'.")
        except Exception as e:
            self.connection.rollback()
            print("Error al crear usuario:", e)

    def iniciar_sesion(self, correo_electronico, contraseña):
        """Permite iniciar sesión."""
        cursor = self.connection.cursor()
        try:
            sql = "SELECT id_usuario, contraseña, rol FROM usuarios WHERE correo = %s"
            cursor.execute(sql, (correo_electronico,))
            resultado = cursor.fetchone()

            if resultado:
                id_usuario, contraseña_hash, tipo_usuario = resultado

                if bcrypt.checkpw(contraseña.encode('utf-8'), contraseña_hash.encode('utf-8')):
                    print("Inicio de sesión exitoso.")
                    return id_usuario, tipo_usuario
                else:
                    print("Contraseña incorrecta.")
            else:
                print("Correo no encontrado.")
        except Exception as e:
            print("Error al iniciar sesión:", e)
        return None, None
