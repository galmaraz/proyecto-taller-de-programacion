from database import Database

class Actualizar:
    def __init__(self):
        self.connection = Database.get_connection()

    def actualizar_campeon(self):
        campeon_id = int(input("\n Ingrese el ID del campeón que desea actualizar: "))
        cursor = self.connection.cursor()
        #Verificar si hay el campeon
        cursor.execute("SELECT id, nombre, rol, habilidades FROM campeones WHERE id=%s", (campeon_id,))
        campeon = cursor.fetchone()

        if campeon:
            print(f"Campeon actual: ID: {campeon[0]}, Nombre: {campeon[1]}, Rol: {campeon[2]}, Habilidades: {campeon[3]}")
            actualizar_campeon = input("¿Desea actualizar el campeon? (s/n): ").lower()

            if actualizar_campeon:
                nuevo_nombre = input("Nuevo nombre del campeon (dejar vacio, para no cambiar): ")
                nuevo_rol = input("Nuevo rol del campeon (dejar vacio, para no cambiar): ")
                nuevas_habilidades = input("Nuevas habilidades del campeón (dejar vacío, para no cambiar): ")
                
                if nuevo_nombre:
                    cursor.execute("UPDATE campeones SET nombre=%s WHERE id=%s", (nuevo_nombre, campeon_id))
                if nuevo_rol:
                    cursor.execute("UPDATE campeones SET rol=%s WHERE id=%s", (nuevo_rol, campeon_id))
                if nuevas_habilidades:
                    cursor.execute("UPDATE campeones SET habilidades=%s WHERE id=%s", (nuevas_habilidades, campeon_id))
                self.connection.commit()
                print(f"¡Campeón con ID {campeon_id} actualizado exitosamente!")
        else:
            print(f"No existe campeon con el ID {campeon_id}")
 

    def actualizar_item(self):
        item_id = int(input("Ingrese el ID del item que sea actualizar: "))
        cursor = self.connection.cursor()

        # Verificar si hay un ítem asociado
        cursor.execute("SELECT id, nombre, tipo, costo FROM items WHERE id=%s", (item_id,))
        item = cursor.fetchone()

        if item:
            print(f"Ítem actual: ID: {item[0]}, Nombre: {item[1]}, Tipo: {item[2]}, Costo: {item[3]}")
            actualizar_item = input("¿Desea actualizar el ítem asociado? (s/n): ").lower()

            if actualizar_item == "s":
                nuevo_nombre_item = str(input("Nuevo nombre del ítem (dejar vacío para no cambiar): "))
                nuevo_tipo_item = str(input("Nuevo tipo del ítem (dejar vacío para no cambiar): "))
                nuevo_costo_item = str(input("Nuevo costo del ítem (dejar vacío para no cambiar): "))

                if nuevo_nombre_item:
                    cursor.execute("UPDATE items SET nombre=%s WHERE id=%s", (nuevo_nombre_item, item[0]))
                if nuevo_tipo_item:
                    cursor.execute("UPDATE items SET tipo=%s WHERE id=%s", (nuevo_tipo_item, item[0]))
                if nuevo_costo_item:
                    cursor.execute("UPDATE items SET costo=%s WHERE id=%s", (nuevo_costo_item, item[0]))
                self.connection.commit()
                print(f"¡Ítem con ID {item[0]} actualizado exitosamente!")
        else:
            print(f"No hay ítems con el ID {item_id}.")

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
