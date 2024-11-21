from create import Create
from read import Read
from update import Update
from eliminar import Delete
from database import Database

def main():
    # Instanciar las clases
    create = Create()
    read = Read()
    update = Update()
    delete = Delete()

    while True:
        print("\n--- Menú Principal ---")
        print("1. Crear Campeón, Ítem y Partida")
        print("2. Leer Campeones, Ítems y Partidas")
        print("3. Actualizar Campeón y su Ítem Relacionado y partida ")
        print("4. Eliminar")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Crear Campeón con Ítem y Partida
            create.nuevo_campeon()

        elif opcion == "2":
            # Leer Campeones, Ítems y Partidas
            print("\n--- Submenú Leer ---")
            print("1. Ver Campeones y sus relaciones")
            print("2. Ver Ítems y sus campeones")
            print("3. Ver Partidas y sus campeones")
            sub_opcion = input("Seleccione una opción: ")
            if sub_opcion == "1":
                read.listar_campeones()
            elif sub_opcion == "2":
                read.listar_items()
            elif sub_opcion == "3":
                read.listar_partidas()
            else:
                print("Opción inválida. Por favor, intente nuevamente.")

        elif opcion == "3":
            # Actualizar Campeón y su Ítem Relacionado
            update.actualizar_campeon()

        elif opcion == "4":
            # Menú para Eliminar
            print("\n--- Submenú Eliminar ---")
            print("1. Eliminar Campeón")
            print("2. Eliminar Ítem")
            print("3. Eliminar Partida")
            sub_opcion = input("Seleccione una opción: ")
            if sub_opcion == "1":
                delete.eliminar_campeon()
            elif sub_opcion == "2":
                delete.eliminar_item()
            elif sub_opcion == "3":
                delete.eliminar_partida()
            else:
                print("Opción inválida. Por favor, intente nuevamente.")

        elif opcion == "5":
            # Salir del Programa
            print("¡Hasta luego!")
            Database.close_connection()
            break

        else:
            print("Opción no válida. Por favor, seleccione nuevamente.")

if __name__ == "__main__":
    main()
