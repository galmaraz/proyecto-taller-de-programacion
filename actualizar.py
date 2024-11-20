from conexion import obtener_conexion

conn, cursor = obtener_conexion()

def actualizar_campeon():
    id_campeon = int(input("Ingrese el ID del campeón que desea actualizar: "))
    nuevo_nombre = input("Ingrese el nuevo nombre del campeón (deje vacío para no cambiar): ")
    nuevo_rol = input("Ingrese el nuevo rol del campeón (deje vacío para no cambiar): ")
    if nuevo_nombre:
        cursor.execute("UPDATE campeones SET nombre = %s WHERE id = %s", (nuevo_nombre, id_campeon))
    if nuevo_rol:
        cursor.execute("UPDATE campeones SET rol = %s WHERE id = %s", (nuevo_rol, id_campeon))
    conn.commit()
    print("Información del campeón actualizada exitosamente.")
