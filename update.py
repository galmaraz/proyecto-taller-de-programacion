from database import Database

class Update:
    def __init__(self):
        self.connection = Database.get_connection()

    def actualizar_campeon(self):
        # Seleccionar Campeón
        campeon_id = int(input("Ingrese el ID del campeón que desea actualizar: "))

        # Pedir nuevos valores para los campos del campeón
        nuevo_nombre = input("Nuevo nombre del campeón (dejar vacío para no cambiar): ")
        nuevo_rol = input("Nuevo rol del campeón (dejar vacío para no cambiar): ")
        nuevas_habilidades = input("Nuevas habilidades del campeón (dejar vacío para no cambiar): ")

        # Actualizar campos del campeón
        cursor = self.connection.cursor()
        if nuevo_nombre:
            cursor.execute("UPDATE campeones SET nombre=%s WHERE id=%s", (nuevo_nombre, campeon_id))
        if nuevo_rol:
            cursor.execute("UPDATE campeones SET rol=%s WHERE id=%s", (nuevo_rol, campeon_id))
        if nuevas_habilidades:
            cursor.execute("UPDATE campeones SET habilidades=%s WHERE id=%s", (nuevas_habilidades, campeon_id))
        self.connection.commit()
        print(f"¡Campeón con ID {campeon_id} actualizado exitosamente!")

        # Actualizar ítem relacionado
        self.actualizar_item_asociado(campeon_id)

        # Actualizar partida relacionada
        self.actualizar_partida_asociada(campeon_id)

    def actualizar_item_asociado(self, campeon_id):
        cursor = self.connection.cursor()

        # Verificar si hay un ítem asociado
        cursor.execute("SELECT id, nombre, tipo, costo FROM items WHERE campeon_id=%s", (campeon_id,))
        item = cursor.fetchone()

        if item:
            print(f"Ítem actual relacionado: ID: {item[0]}, Nombre: {item[1]}, Tipo: {item[2]}, Costo: {item[3]}")
            actualizar_item = input("¿Desea actualizar el ítem asociado? (s/n): ").lower()

            if actualizar_item == "s":
                nuevo_nombre_item = input("Nuevo nombre del ítem (dejar vacío para no cambiar): ")
                nuevo_tipo_item = input("Nuevo tipo del ítem (dejar vacío para no cambiar): ")
                nuevo_costo_item = input("Nuevo costo del ítem (dejar vacío para no cambiar): ")

                if nuevo_nombre_item:
                    cursor.execute("UPDATE items SET nombre=%s WHERE id=%s", (nuevo_nombre_item, item[0]))
                if nuevo_tipo_item:
                    cursor.execute("UPDATE items SET tipo=%s WHERE id=%s", (nuevo_tipo_item, item[0]))
                if nuevo_costo_item:
                    cursor.execute("UPDATE items SET costo=%s WHERE id=%s", (nuevo_costo_item, item[0]))
                self.connection.commit()
                print(f"¡Ítem con ID {item[0]} actualizado exitosamente!")
        else:
            print(f"No hay ítems asociados al campeón con ID {campeon_id}.")

    def actualizar_partida_asociada(self, campeon_id):
        cursor = self.connection.cursor()

        # Verificar si hay una partida asociada
        cursor.execute("""
            SELECT p.id, p.modo, p.num_jugadores
            FROM partidas p
            JOIN campeones_partidas cp ON p.id = cp.partida_id
            WHERE cp.campeon_id=%s
        """, (campeon_id,))
        partida = cursor.fetchone()

        if partida:
            print(f"Partida actual relacionada: ID: {partida[0]}, Modo: {partida[1]}, Jugadores: {partida[2]}")
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
            print(f"No hay partidas asociadas al campeón con ID {campeon_id}.")
