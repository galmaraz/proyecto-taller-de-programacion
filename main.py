
from gestor_crear import IniciarSesion
from administrador import Administrador
from jugador import Jugador
from database import Database
from ordenar import Ordenar 

def menu_jugador(jugador):
    ordenador = Ordenar()   

    while True:
        print("\n=== Menú Jugador ===")
        print("1. Crear Partida")
        print("2. Ver Campeones")
        print("3. Ver Ítems")
        print("4. Ver Partidas")
        print("5. Actualizar Partida")
        print("6. Eliminar Partida")
        print("7. Ordenar Campeones")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            jugador.crear_partida()
        elif opcion == "2":
            jugador.ver_campeones()
        elif opcion == "3":
            jugador.ver_items()
        elif opcion == "4":
            jugador.ver_partidas()
        elif opcion == "5":
            jugador.actualizar_partida()
        elif opcion == "6":
            jugador.eliminar_partida()
        elif opcion == "7":
            ordenador.ordenar_campeones()
        elif opcion == "9":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")


def menu_administrador(administrador):
    while True:
        print("\n=== Menú Administrador ===")
        print("1. Crear Campeon")
        print("2. Crear item")
        print("3. Actualizar Campeon")
        print("4. Actualizar item")
        print("5. Eliminar campeon")
        print("6. Eliminar item")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Crear Campeón 
            administrador.crear_campeon()
        elif opcion == "2":
            # Crear Ítem
            campeon_id = int(input("Ingrese el ID del campeon al cual quieres asociar el item: "))
            administrador.crear_item(campeon_id)
        elif opcion == "3":
            # Actualizar Campeón 
            administrador.actualizar_campeon()
        elif opcion == "4":
            # Actualizar item
            administrador.actualizar_item()
        elif opcion == "5":
            #Elimina al un campeon 
            administrador.eliminar_campeon()
        elif opcion == "6":
            #Elimina un item 
            administrador.eliminar_item()
        elif opcion == "7":
            # Salir del Programa
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor seleccione nuevamente.")

def main():
    Database.connect()
    sesion = IniciarSesion()

    while True:
        print("\n--- Menú Principal ---")
        print("1: Crear cuenta de usuario")
        print("2: Iniciar sesión")
        print("3: Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            correo = input("Correo: ")
            contraseña = input("Contraseña: ")
            rol = input("Rol (administrador/jugador): ").lower()
            sesion.cuenta_usuario(correo, contraseña, rol)

        elif opcion == "2":
            correo = input("Correo: ")
            contraseña = input("Contraseña: ")
            id_usuario, tipo_usuario = sesion.iniciar_sesion(correo, contraseña)

            if tipo_usuario == "jugador":
                jugador = Jugador(id_usuario)
                menu_jugador(jugador)
            elif tipo_usuario == "administrador":
                administrador = Administrador()
                menu_administrador(administrador)
            else:
                print("Inicio de sesión fallido.")
        
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

    Database.close()

if __name__ == "__main__":
    main()
