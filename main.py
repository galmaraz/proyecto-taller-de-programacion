from gestor_crear import Crear, IniciarSesion
from jugador import Jugador
from database import Database

def menu_jugador(jugador):
    while True:
        print("\n=== Menú Jugador ===")
        print("1. Crear Partida")
        print("2. Ver Campeones")
        print("3. Ver Ítems")
        print("4. Ver Partidas")
        print("5. Actualizar Partida")
        print("6. Eliminar Partida")
        print("7. Salir")
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
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")



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
                print("Función de administrador no implementada.")
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
