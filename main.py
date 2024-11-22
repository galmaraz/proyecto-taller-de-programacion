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
        print("2. Ver Campeones, Ítems y Partidas")
        print("3. Actualizar Campeón y su Ítem Relacionado y partida ")
        print("4. Eliminar")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Crear Campeón con Ítem y Partida
            create.nuevo_campeon()
        elif opcion == "2":
            # Leer Campeones, Ítems y Partidas
            read.listar_campeones()
        elif opcion == "3":
            # Actualizar Campeón y su Ítem Relacionado
            update.actualizar_campeon()

        elif opcion == "4":
                delete.eliminar_campeon()
                
        elif opcion == "5":
            # Salir del Programa
            print("¡Hasta luego!")
            Database.close_connection()
            break

        else:
            print("Opción no válida. Por favor, seleccione nuevamente.")

if __name__ == "__main__":
    main()
