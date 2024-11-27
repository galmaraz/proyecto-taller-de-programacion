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

    def actualizar_partida(self):
        """Permite al jugador actualizar el número de jugadores en una partida existente."""
        print("\n=== Actualizar Partida ===")
        id_partida = input("Ingrese el ID de la partida que desea actualizar: ").strip()

        # Verificar si la partida existe y pertenece al jugador
        query_verificar = "SELECT * FROM partidas WHERE id_partida = %s AND usuario_id = %s"
        params_verificar = (id_partida, self.id_usuario)
        resultado = Database.execute_query(query_verificar, params_verificar)

        if not resultado:
            print("No se encontró una partida con el ID proporcionado o no pertenece a usted.")
            return

        # Solicitar nuevo número de jugadores
        nuevo_num_jugadores = input("Ingrese el nuevo número de jugadores (o presione Enter para cancelar): ").strip()
        if not nuevo_num_jugadores:
            print("No se realizó ningún cambio.")
            return

        try:
            nuevo_num_jugadores = int(nuevo_num_jugadores)
        except ValueError:
            print("El número de jugadores debe ser un valor numérico.")
            return

        # Actualizar la partida
        query_actualizar = "UPDATE partidas SET num_jugadores = %s WHERE id_partida = %s AND usuario_id = %s"
        params_actualizar = (nuevo_num_jugadores, id_partida, self.id_usuario)
        if Database.execute_query(query_actualizar, params_actualizar):
            print(f"Partida con ID {id_partida} actualizada con éxito. Nuevo número de jugadores: {nuevo_num_jugadores}.")
        else:
            print("Error al actualizar la partida.")


    def eliminar_partida(self):
        """Permite al jugador eliminar una partida existente."""
        print("\n=== Eliminar Partida ===")
        id_partida = input("Ingrese el ID de la partida que desea eliminar: ").strip()

        # Verificar si la partida existe y pertenece al jugador
        query_verificar = "SELECT * FROM partidas WHERE id_partida = %s AND usuario_id = %s"
        params_verificar = (id_partida, self.id_usuario)
        resultado = Database.execute_query(query_verificar, params_verificar)

        if not resultado:
            print("No se encontró una partida con el ID proporcionado o no pertenece a usted.")
            return

        # Confirmar la eliminación
        confirmacion = input(f"¿Está seguro de que desea eliminar la partida con ID {id_partida}? (s/n): ").strip().lower()
        if confirmacion != "s":
            print("Operación cancelada.")
            return

        # Eliminar la partida
        query_eliminar = "DELETE FROM partidas WHERE id_partida = %s AND usuario_id = %s"
        params_eliminar = (id_partida, self.id_usuario)
        if Database.execute_query(query_eliminar, params_eliminar):
            print(f"Partida con ID {id_partida} eliminada con éxito.")
        else:
            print("Error al eliminar la partida.")