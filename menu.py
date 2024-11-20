from crear import crear_campeon, crear_item, crear_partida
from visualizar import visualizar_campeones, visualizar_items, visualizar_partidas
from actualizar import actualizar_campeon
from eliminar import eliminar_campeon

def sub_menu_crear():
    while True:
        print("\n--- Menú Crear ---")
        print("1. Crear un nuevo campeón")
        print("2. Crear un nuevo ítem")
        print("3. Crear una nueva partida")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_campeon()
        elif opcion == "2":
            crear_item()
        elif opcion == "3":
            crear_partida()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

def sub_menu_visualizar():
    while True:
        print("\n--- Menú Visualizar ---")
        print("1. Visualizar campeones")
        print("2. Visualizar ítems")
        print("3. Visualizar partidas")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            visualizar_campeones()
        elif opcion == "2":
            visualizar_items()
        elif opcion == "3":
            visualizar_partidas()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

def sub_menu_actualizar():
    while True:
        print("\n--- Menú Actualizar ---")
        print("1. Actualizar un campeón")
        print("2. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            actualizar_campeon()
        elif opcion == "2":
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

def sub_menu_eliminar():
    while True:
        print("\n--- Menú Eliminar ---")
        print("1. Eliminar un campeón")
        print("2. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            eliminar_campeon()
        elif opcion == "2":
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Crear")
        print("2. Visualizar")
        print("3. Actualizar")
        print("4. Eliminar")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            sub_menu_crear()
        elif opcion == "2":
            sub_menu_visualizar()
        elif opcion == "3":
            sub_menu_actualizar()
        elif opcion == "4":
            sub_menu_eliminar()
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

# Ejecutar el menú principal
if __name__ == "__main__":
    menu_principal()
