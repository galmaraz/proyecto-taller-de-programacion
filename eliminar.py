from database import Database

class Delete:
    def __init__(self):
        self.connection = Database.get_connection()

    def eliminar_campeon(self):
        id_campeon = int(input("ID del campeón a eliminar: "))
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM campeones WHERE id=%s", (id_campeon,))
        self.connection.commit()
        print("¡Campeón eliminado exitosamente!")

    def eliminar_item(self):
        id_item = int(input("ID del ítem a eliminar: "))
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM items WHERE id=%s", (id_item,))
        self.connection.commit()
        print("¡Ítem eliminado exitosamente!")

    def eliminar_partida(self):
        id_partida = int(input("ID de la partida a eliminar: "))
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM partidas WHERE id=%s", (id_partida,))
        self.connection.commit()
        print("¡Partida eliminada exitosamente!")
