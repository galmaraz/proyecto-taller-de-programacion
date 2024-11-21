from database import Database

class Create:
    def __init__(self):
        self.connection = Database.get_connection()

    def nuevo_campeon(self):
        nombre = input("Nombre del campeón: ")
        rol = input("Rol del campeón: ")
        habilidades = input("Habilidades del campeón: ")

        cursor = self.connection.cursor()
        query_campeon = "INSERT INTO campeones (nombre, rol, habilidades) VALUES (%s, %s, %s)"
        cursor.execute(query_campeon, (nombre, rol, habilidades))
        self.connection.commit()
        campeon_id = cursor.lastrowid
        print(f"¡Campeón creado con ID: {campeon_id}!")

        # Crear Ítem relacionado
        nombre_item = input("Nombre del ítem relacionado: ")
        tipo_item = input("Tipo del ítem: ")
        costo_item = int(input("Costo del ítem: "))
        query_item = "INSERT INTO items (nombre, tipo, costo, campeon_id) VALUES (%s, %s, %s, %s)"
        cursor.execute(query_item, (nombre_item, tipo_item, costo_item, campeon_id))
        self.connection.commit()
        print(f"¡Ítem creado para el campeón {nombre}!")

        # Crear Partida y Relación
        modo = input("Modo de juego de la partida: ")
        num_jugadores = int(input("Número de jugadores: "))
        query_partida = "INSERT INTO partidas (modo, num_jugadores) VALUES (%s, %s)"
        cursor.execute(query_partida, (modo, num_jugadores))
        self.connection.commit()
        partida_id = cursor.lastrowid
        print(f"¡Partida creada con ID: {partida_id}!")

        # Relacionar Campeón y Partida
        query_relacion = "INSERT INTO campeones_partidas (campeon_id, partida_id) VALUES (%s, %s)"
        cursor.execute(query_relacion, (campeon_id, partida_id))
        self.connection.commit()
        print(f"¡Campeón {nombre} relacionado con la partida {modo}!")
