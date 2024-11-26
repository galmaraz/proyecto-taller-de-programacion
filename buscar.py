from database import Database

class Buscar:
    def __init__(self):
        # Establece conexión a la base de datos
        self.connection = Database.get_connection()

    def buscar_campeon(self):
        """
        Permite buscar campeones por nombre o rol.
        Muestra los resultados encontrados o indica si no hay coincidencias.
        """
        cursor = self.connection.cursor()
        print("\n--- Búsqueda de Campeones ---")
        criterio = input("¿Desea buscar por 'nombre' o por 'rol'? ").strip().lower()

        if criterio == "nombre":
            nombre = input("Ingrese el nombre del campeón a buscar: ").strip()
            query = "SELECT id, nombre, rol, habilidades FROM campeones WHERE nombre LIKE %s"
            cursor.execute(query, (f"%{nombre}%",))
        elif criterio == "rol":
            rol = input("Ingrese el rol del campeón a buscar: ").strip()
            query = "SELECT id, nombre, rol, habilidades FROM campeones WHERE rol LIKE %s"
            cursor.execute(query, (f"%{rol}%",))
        else:
            print("Criterio inválido. Por favor, intente nuevamente.")
            return

        resultados = cursor.fetchall()

        if resultados:
            print("\nResultados encontrados:")
            for id_campeon, nombre, rol, habilidades in resultados:
                print(f"ID: {id_campeon}, Nombre: {nombre}, Rol: {rol}, Habilidades: {habilidades}")
        else:
            print("No se encontraron campeones que coincidan con la búsqueda.")
