from database import Database

class Jugador:
    def __init__(self, id_usuario):
        self.id_usuario = id_usuario

    def crear_partida(self):
        print("\n=== Crear Partida ===")
        modo = input("Ingrese el modo de juego (Normal/Clasificatoria): ").strip()
        num_jugadores = int(input("Ingrese el número de jugadores: "))
        query = "INSERT INTO partidas (modo, num_jugadores, usuario_id) VALUES (%s, %s, %s)"
        params = (modo, num_jugadores, self.id_usuario)

        if Database.execute_query(query, params):
            print(f"Partida '{modo}' creada con éxito.")
        else:
            print("Error al crear la partida.")

    def ver_campeones(self):
        print("\n=== Lista de Campeones ===")
        query = "SELECT * FROM campeones"
        resultados = Database.execute_query(query)

        if resultados:
            for campeon in resultados:
                print(f"ID: {campeon[0]}, Nombre: {campeon[1]}, Rol: {campeon[2]}, Habilidades: {campeon[3]}")
        else:
            print("No se encontraron campeones.")

    def ver_items(self):
        print("\n=== Lista de Ítems ===")
        query = "SELECT * FROM items"
        resultados = Database.execute_query(query)

        if resultados:
            for item in resultados:
                print(f"ID: {item[0]}, Nombre: {item[1]}, Tipo: {item[2]}, Costo: {item[3]}")
        else:
            print("No se encontraron ítems.")

    def ver_partidas(self):
        print("\n=== Lista de Partidas ===")
        query = "SELECT * FROM partidas WHERE usuario_id = %s"
        params = (self.id_usuario,)
        resultados = Database.execute_query(query, params)

        if resultados:
            for partida in resultados:
                print(f"ID: {partida[0]}, Modo: {partida[1]}, Jugadores: {partida[2]}")
        else:
            print("No se encontraron partidas.")
