#Importamos las clases para instanciarlas, y la base de datos
from crear import iniciar_sesion

def main():
    Crear = iniciar_sesion()
    while True:
        print("\n----Menu principal----")
        print("1: Crear cuenta de usuario")
        print("2: Iniciar sesion")
        print("3: Salir")
        opcion = int(input("Escoge una opcion: "))

        if opcion == 1:
            correo_electronico = input("Ingresar correo electronico: ")
            contraseña = input("Ingresar contraseña: ")
            tipo_usuario = str(input("Ingrese tipo de usuario (administrador o jugador): "))
            Crear.cuenta_usuario(correo_electronico, contraseña, tipo_usuario)

        elif opcion == 2:
            correo_electronico = str(input("Ingresar nombre de correo electronico: "))
            contraseña = input("Ingresar contraseña: ")
            Crear.iniciar_sesion(correo_electronico, contraseña)
        
        elif opcion == 3:
            print("Saliendo de programa")
            break
        
        else:
            print("Opcion no valido, selecione nuevamente")

if __name__ == "__main__":
    main()
