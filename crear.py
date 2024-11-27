import bcrypt
import questionary
from database import Database
from read import Read
from actualizar import Actualizar
from eliminar import Delete
from database import Database
from ordenar import Ordenar
from buscar import Buscar


class Crear:
    def __init__(self):
        self.connection = Database.get_connection()

    # Añadir las funciones existentes de `nuevo_campeon`, etc.
    def nuevo_campeon(self):
        nombre = input("Nombre del campeón para iniciar la partida: ")
        rol = questionary.select("¿Qué rol prefieres?", choices=["Top lane", "Jungla", "Mid lane", "Support", "Bot lane"]).ask()
        habilidades = input("Habilidades del campeón: \nEjemplos de habilidades: \nGaren:\nPasiva: genera un porcentaje de salud máxima\nJudgmen: Garen gira rápidamente con su espada, infligiendo daño a los enemigos cercanos.\nIngrese su habilidad: ")

        cursor = self.connection.cursor()
        sql_campeon = "INSERT INTO campeones (nombre, rol, habilidades) VALUES (%s, %s, %s)"
        cursor.execute(sql_campeon, (nombre, rol, habilidades))
        self.connection.commit()
        campeon_id = cursor.lastrowid
        print(f"¡Campeón creado con ID: {campeon_id}!")

        nombre_item = input("Nombre del item relacionado según el rol: \nEjemplo:\n 'Top lane -> Blade of the Ruined King' \n 'Mid lane -> Rabadon's Deathcap' \n 'Bot lane -> Infinity Edge' \nIngrese el item: ")
        tipo_item = questionary.select("¿Qué tipo de item quiere?", choices=["Daño físico", "Daño mágico", "Penetración de armadura", "Armadura física", "Armadura mágica"]).ask()
        costo_item = int(input("Costo del item: "))
        sql_item = "INSERT INTO items (nombre, tipo, costo, campeon_id) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql_item, (nombre_item, tipo_item, costo_item, campeon_id))
        self.connection.commit()
        print(f"¡Item creado para el campeón {nombre}!")

        modo = questionary.select("¿Qué modo de juego prefieres?", choices=["Clasificatoria", "Normal", "Aram"]).ask()
        num_jugadores = questionary.select("¿Cuántos jugadores quieres escoger?", choices=["5", "3"]).ask()
        sql_partida = "INSERT INTO partidas (modo, num_jugadores) VALUES (%s, %s)"
        cursor.execute(sql_partida, (modo, num_jugadores))
        self.connection.commit()
        partida_id = cursor.lastrowid
        print(f"¡Partida creada exitosamente con ID: {partida_id}!")

        sql_relacion = "INSERT INTO campeones_partidas (campeon_id, partida_id) VALUES (%s, %s)"
        cursor.execute(sql_relacion, (campeon_id, partida_id))
        self.connection.commit()
        print(f"¡Campeón {nombre} relacionado con la partida {modo}!")


class iniciar_sesion:
    def __init__(self):
        self.connection = Database.get_connection()
    # Funcion para Crear un usuario
    def cuenta_usuario(self, correo_electronico, contraseña, tipo_rol):
        cursor = self.connection.cursor()
        try:
            salt = bcrypt.gensalt()
            contraseña_hash = bcrypt.hashpw(contraseña.encode('utf-8'), salt)
            sql = "INSERT INTO usuarios (correo, contraseña, rol) VALUES (%s, %s, %s)"
            cursor.execute(sql, (correo_electronico, contraseña_hash, tipo_rol))
            self.connection.commit()
            print("Usuario creado exitosamente.")
            print(f"Usuario: '{correo_electronico}' se creó como '{tipo_rol}'")
        except Exception as e:
            self.connection.rollback()
            print("Error al crear usuario:", e)

    # Funcion para acceder a los privilegios
    def iniciar_sesion(self, correo_electronico, contraseña):
        cursor = self.connection.cursor()
        try:
            sql = "SELECT contraseña, rol FROM usuarios WHERE correo = %s"
            cursor.execute(sql, (correo_electronico,))
            resultado = cursor.fetchone()

            if resultado:
                contraseña_hash = resultado[0]
                tipo_usuario = resultado[1]

                if bcrypt.checkpw(contraseña.encode('utf-8'), contraseña_hash.encode('utf-8')):
                    print("Inicio de sesión exitoso\n")
                    if tipo_usuario == "administrador":
                        print("Bienvenido administrador")
                        submain()
                    elif tipo_usuario == "jugador":
                        print("Bienvenido jugador")
                        submain()
                else:
                    print("Contraseña incorrecta")
            else:
                print("Usuario no encontrado o incorrecto")
        except Exception as e:
            self.connection.rollback()
            print("Error al iniciar sesión:", e)

def submain():
    # Instanciar las clases
    create = Crear()
    read = Read()
    update = Actualizar()
    delete = Delete()
    ordenar = Ordenar()
    buscar = Buscar()
    while True:
        print("\n--- Menú Principal ---")
        print("1. Crear Campeón, Ítem y Partida")
        print("2. Ver Campeones, Ítems y Partidas")
        print("3. Ver Partidas")
        print("4. Ver items")
        print("5. Actualizar Campeón")
        print("6. Actualizar item")
        print("7. Actualizar partida")
        print("8. Eliminar campeon")
        print("9. Eliminar partida")
        print("10. Eliminar item")
        print("11. Ordenar campeones por nombre")
        print("12. Buscar campeones por nombre o rol")
        print("13. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Crear Campeón con Ítem y Partida
            create.nuevo_campeon()
        elif opcion == "2":
            # Leer Campeones, Ítems y Partidas
            read.listar_campeones()
        elif opcion == "3":
            #Leer partidas 
            read.listar_partidas()
        elif opcion == "4":
            #Listar items 
            read.listar_itmes()
        elif opcion == "5":
            # Actualizar Campeón y su Ítem Relacionado
            update.actualizar_campeon()
        elif opcion == "6":
            # Actualizar item
            update.actualizar_item()
        elif opcion == "7":
            #Actualizar partida
            update.actualizar_partida()
        elif opcion == "8":
            #Elimina al un campeon 
            delete.eliminar_campeon()
        elif opcion == "9":
            #Elimina un partida
            delete.eliminar_partida()
        elif opcion == "10":
            #Elimina un item 
            delete.eliminar_item()
        elif opcion == "11":
            ordenar.ordenar_campeones()
        elif opcion == "12":
            buscar.buscar_campeon()
        elif opcion == "13":
            # Salir del Programa
            print("¡Hasta luego!")
            Database.close_connection()
            break
        else:
            print("Opción no válida. Por favor seleccione nuevamente.")
