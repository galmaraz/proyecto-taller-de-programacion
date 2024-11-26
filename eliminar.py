from database import Database

class Delete:
    def __init__(self):
        self.connection = Database.get_connection()

    def eliminar_campeon(self):
        id_campeon = int(input("ID del campeón a eliminar: "))
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
  

    def eliminar_partida(self):
        id_partida = int(input("ID de la partida a eliminar: "))
        cursor = self.connection.cursor()
        #Verificar si hay partida  
        cursor.execute("SELECT id FROM partidas WHERE id=%s", (id_partida,))
        partida = cursor.fetchone()
        if partida:
            try:
                cursor.execute("DELETE FROM partidas WHERE id=%s", (id_partida,))
                self.connection.commit()
                print("¡Partida eliminada exitosamente!")
            except Exception as e:
                self.connection.rollback()
                print(f"Error al eliminar la partida: {e}")
        else:
            print(f"No existe partida con ese ID {id_partida}")

