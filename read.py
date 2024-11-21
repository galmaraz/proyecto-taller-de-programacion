from database import Database

class Read:
    def __init__(self):
        self.connection = Database.get_connection()

    def listar_campeones(self):
        cursor = self.connection.cursor()
        query = """
            SELECT c.id, c.nombre, c.rol, c.habilidades, i.nombre AS item_nombre, p.id AS partida_id, p.modo AS partida_modo
            FROM campeones c
            LEFT JOIN items i ON c.id = i.campeon_id
            LEFT JOIN campeones_partidas cp ON c.id = cp.campeon_id
            LEFT JOIN partidas p ON cp.partida_id = p.id
        """
        cursor.execute(query)
        campeones = cursor.fetchall()
        print("Campeones, Ítems y Partidas Relacionadas:")
        for c in campeones:
            print(f"ID: {c[0]}, Nombre: {c[1]}, Rol: {c[2]}, Habilidades: {c[3]}, Ítem: {c[4] or 'Ninguno'}, Partida: {c[6] or 'Ninguna'}")

    def listar_partidas(self):
        cursor = self.connection.cursor()
        query = """
            SELECT p.id, p.modo, p.num_jugadores, c.id AS campeon_id, c.nombre AS campeon_nombre
            FROM partidas p
            LEFT JOIN campeones_partidas cp ON p.id = cp.partida_id
            LEFT JOIN campeones c ON cp.campeon_id = c.id
        """
        cursor.execute(query)
        partidas = cursor.fetchall()
        print("Partidas y Campeones Involucrados:")
        for p in partidas:
            print(f"ID Partida: {p[0]}, Modo: {p[1]}, Jugadores: {p[2]}, ID Campeón: {p[3] or 'Ninguno'}, Nombre Campeón: {p[4] or 'Ninguno'}")
