from database import Database
import questionary

class Administrador:
    def __init__(self):
        self.connection = Database.get_connection()
    
    def crear_campeon(self):
        print("\n=== Crear Campeon ===")
        nombre = input("Nombre del campeon para iniciar la partida: ")
        rol = questionary.select("¿Qué rol prefieres?", choices=["Top lane", "Jungla", "Mid lane", "Support", "Bot lane"]).ask()
        habilidades = input("Ingrese habilidad para el campeon: ")
        cursor = self.connection.cursor()
        sql_campeon = "INSERT INTO campeones (nombre, rol, habilidades) VALUES (%s, %s, %s)"
        cursor.execute(sql_campeon, (nombre, rol, habilidades))
        self.connection.commit()
        campeon_id = cursor.lastrowid
        print(f"¡Campeón creado con ID: {campeon_id}!")
    
    def crear_item(self, campeon_id):
        nombre = input("Ingrese el nombre del item: ")
        tipo = questionary.select("¿Qué tipo de item quiere?", choices=["Daño físico", "Daño mágico", "Penetración de armadura", "Armadura física", "Armadura mágica"]).ask()
        costo = int(input("Ingrese el costo del item: "))
        cursor = self.connection.cursor()
        sql_item = "INSERT INTO items (nombre, tipo, costo, campeon_id) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql_item, (nombre, tipo, costo, campeon_id))
        self.connection.commit()
        print(f"¡Item creado para el campeón con ID {nombre}!")
    
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
                nuevo_nombre = str(input("Nuevo nombre del ítem (dejar vacío para no cambiar): "))
                nuevo_tipo = str(input("Nuevo tipo del ítem (dejar vacío para no cambiar): "))
                nuevo_costo = str(input("Nuevo costo del ítem (dejar vacío para no cambiar): "))
                if nuevo_nombre:
                    cursor.execute("UPDATE items SET nombre=%s WHERE id=%s", (nuevo_nombre, item[0]))
                if nuevo_tipo:
                    cursor.execute("UPDATE items SET tipo=%s WHERE id=%s", (nuevo_tipo, item[0]))
                if nuevo_costo:
                    cursor.execute("UPDATE items SET costo=%s WHERE id=%s", (nuevo_costo, item[0]))
                self.connection.commit()
                print(f"¡Ítem con ID {item[0]} actualizado exitosamente!")
        else:
            print(f"No hay ítems con el ID {item_id}.")
        
    def eliminar_campeon(self):
        id_campeon = int(input("ID del campenn a eliminar: "))
        cursor = self.connection.cursor()
        #Verificar si hay campeon 
        cursor.execute("SELECT id FROM campeones WHERE id=%s", (id_campeon,))
        campeon = cursor.fetchone()
        if campeon:
            try:
                # Eliminar las relaciones en campeones_partidas
                cursor.execute("DELETE FROM campeones_partidas WHERE campeon_id=%s", (id_campeon,))
                # Eliminar las relaciones en items
                cursor.execute("DELETE FROM items WHERE campeon_id=%s", (id_campeon,))
                # Finalmente, eliminar el registro en campeones
                cursor.execute("DELETE FROM campeones WHERE id=%s", (id_campeon,))
                self.connection.commit()
                print("¡Campeón eliminado exitosamente!")
            except Exception as e:
                self.connection.rollback()
                print(f"Error al eliminar el campeon: {e}")
        else:
            print(f"No existe un campeon con ese ID {id_campeon}")


    def eliminar_item(self):
        id_item = int(input("ID del ítem a eliminar: "))
        cursor = self.connection.cursor()
        #Verificar si hay item 
        cursor.execute("SELECT id FROM items WHERE id=%s", (id_item,))
        item = cursor.fetchone()
        if item:
            try:
                cursor.execute("DELETE FROM items WHERE id=%s", (id_item,))
                self.connection.commit()
                print("¡Ítem eliminado exitosamente!")
            except Exception as e:
                self.connection.rollback()
                print(f"Error al eliminar el ítem: {e}")
        else:
            print(f"No existe un item con ese ID {id_item}")