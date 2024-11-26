from database import Database

class Ordenar:
    def __init__(self):
        # Establece conexión a la base de datos
        self.connection = Database.get_connection()

    def quicksort(self, lista):
        """
        Algoritmo QuickSort para ordenar una lista.
        Ordena la lista basada en el segundo elemento (nombre) de cada tupla.
        """
        if len(lista) <= 1:
            return lista  # Una lista vacía o de un solo elemento ya está ordenada
        pivot = lista[0]  # Elige el primer elemento como pivote
        menores = [x for x in lista[1:] if x[1].lower() <= pivot[1].lower()]  # Elementos <= al pivote
        mayores = [x for x in lista[1:] if x[1].lower() > pivot[1].lower()]   # Elementos > al pivote
        # Ordena recursivamente los elementos menores y mayores
        return self.quicksort(menores) + [pivot] + self.quicksort(mayores)

    def ordenar_campeones(self):
        """
        Obtiene los campeones de la base de datos, los ordena por nombre usando QuickSort y los muestra.
        """
        cursor = self.connection.cursor()
        # Obtiene todos los campeones con sus IDs y nombres
        cursor.execute("SELECT id, nombre FROM campeones")
        campeones = cursor.fetchall()

        if not campeones:
            print("No hay campeones en la base de datos para ordenar.")
            return

        print("Campeones sin ordenar:")
        for id_campeon, nombre in campeones:
            print(f"ID: {id_campeon}, Nombre: {nombre}")

        # Ordena los campeones usando QuickSort
        campeones_ordenados = self.quicksort(campeones)

        print("\nCampeones ordenados por nombre:")
        for id_campeon, nombre in campeones_ordenados:
            print(f"ID: {id_campeon}, Nombre: {nombre}")
