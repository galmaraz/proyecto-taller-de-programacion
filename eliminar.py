from database import Database

class Delete:
    def __init__(self):
        self.connection = Database.get_connection()

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

