from conexion import obtener_conexion

conn, cursor = obtener_conexion()

def crear_campeon():
    nombre = input("Ingrese el nombre del campeón: ")
    rol = input("Ingrese el rol del campeón (e.g., Mago, Guerrero, Soporte): ")
    habilidades = input("Ingrese una descripción de las habilidades del campeón: ")
    query = "INSERT INTO campeones (nombre, rol, habilidades) VALUES (%s, %s, %s)"
    cursor.execute(query, (nombre, rol, habilidades))
    conn.commit()
    print("Campeón creado exitosamente.")

def crear_item():
    nombre = input("Ingrese el nombre del ítem: ")
    tipo = input("Ingrese el tipo del ítem (e.g., arma, armadura): ")
    costo = int(input("Ingrese el costo del ítem en oro: "))
    query = "INSERT INTO items (nombre, tipo, costo) VALUES (%s, %s, %s)"
    cursor.execute(query, (nombre, tipo, costo))
    conn.commit()
    print("Ítem creado exitosamente.")

def crear_partida():
    modo = input("Ingrese el modo de juego (e.g., Normal, Clasificatoria): ")
    num_jugadores = int(input("Ingrese el número de jugadores: "))
    query = "INSERT INTO partidas (modo, num_jugadores) VALUES (%s, %s)"
    cursor.execute(query, (modo, num_jugadores))
    conn.commit()
    print("Partida creada exitosamente.")
