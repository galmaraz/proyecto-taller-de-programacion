from database import Database

class Actualizar:
    def __init__(self):
        self.connection = Database.get_connection()

    

    def actualizar_partida(self):
        partida_id = int(input("Ingresa el ID de la partida que desea actualizar: "))
        cursor = self.connection.cursor()

        # Verificar si hay una partida asociada
        cursor.execute("SELECT id, modo, num_jugadores FROM partidas WHERE id=%s", (partida_id,))
        partida = cursor.fetchone()

        if partida:
            print(f"\n Partida actual: ID: {partida[0]}, Modo: {partida[1]}, Jugadores: {partida[2]}")
            actualizar_partida = input("¿Desea actualizar la partida asociada? (s/n): ").lower()

            if actualizar_partida == "s":
                nuevo_modo = input("Nuevo modo de la partida (dejar vacío para no cambiar): ")
                nuevo_num_jugadores = input("Nuevo número de jugadores (dejar vacío para no cambiar): ")

                if nuevo_modo:
                    cursor.execute("UPDATE partidas SET modo=%s WHERE id=%s", (nuevo_modo, partida[0]))
                if nuevo_num_jugadores:
                    cursor.execute("UPDATE partidas SET num_jugadores=%s WHERE id=%s", (nuevo_num_jugadores, partida[0]))
                self.connection.commit()
                print(f"¡Partida con ID {partida[0]} actualizada exitosamente!")
        else:
            print(f"No hay partidas con el ID {partida_id}.")
