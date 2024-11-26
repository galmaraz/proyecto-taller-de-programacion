from database import Database

class Crear:
    def __init__(self):
        self.connection = Database.get_connection()
        # Funcion para Crear un campeon
    def nuevo_campeon(self):
        nombre = input("Nombre del campeón para iniciar la partida: ")
        rol = input("Rol del campeón:\n Carril superior 'Top lane' \n Jungle 'Jungla' \n Carril central 'Mid lane' \n Carril inferior 'Support' \n Carril inferior 'Bot lane' \n Ingrese su rol:  ")
        habilidades = input("Habilidades del campeón: \n Ejemplos de habilidades: \n Garen:\n Pasiva: genera un porcentaje de salud maxima\n Judgmen: Garen gira rápidamente con su espada, infligiendo daño a los enemigos cercanos.\n Ingrese su habilidad: ")

        cursor = self.connection.cursor()
        sql_campeon = "INSERT INTO campeones (nombre, rol, habilidades) VALUES (%s, %s, %s)"  
        cursor.execute(sql_campeon, (nombre, rol, habilidades))
        self.connection.commit()
        campeon_id = cursor.lastrowid
        print(f"¡Campeón creado con ID: {campeon_id}!")

        # Crear Ítem relacionado
        nombre_item = input("Nombre del item relacionado segun el rol: \n Ejemplo:\n 'Top lane -> Blade of the Ruined King' \n 'Mid lane -> Rabadon's Deathcap' \n 'Bot lane -> Infinity Edge' \n Ingrese el item: ")
        tipo_item = input("Tipo del item 'Daño fisico, Daño magico, Defensa, Penetracion de armadura': ")
        costo_item = int(input("Costo del item: "))
        sql_item = "INSERT INTO items (nombre, tipo, costo, campeon_id) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql_item, (nombre_item, tipo_item, costo_item, campeon_id))
        self.connection.commit()
        print(f"¡Item creado para el campeón {nombre}!")

        # Crear Partida y Relación
        modo = input("Modo de juego de la partida \n'Clasificatoria,\n Normal,\n Aram': ")
        num_jugadores = int(input("Numero de jugadores: "))
        sql_partida = "INSERT INTO partidas (modo, num_jugadores) VALUES (%s, %s)"
        cursor.execute(sql_partida, (modo, num_jugadores))
        self.connection.commit()
        partida_id = cursor.lastrowid
        print(f"¡Partida creada exitosamente con ID: {partida_id}!")

        # Relacionar Campeón y Partida
        sql_relacion = "INSERT INTO campeones_partidas (campeon_id, partida_id) VALUES (%s, %s)"
        cursor.execute(sql_relacion, (campeon_id, partida_id))
        self.connection.commit()
        print(f"¡Campeón {nombre} relacionado con la partida {modo}!")
