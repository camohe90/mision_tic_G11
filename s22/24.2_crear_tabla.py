import sqlite3

conexion = sqlite3.connect("db/tkinter.db")
print("Conectado exitosamente")

cursor = conexion.cursor()

cursor.execute("CREATE TABLE clientes(id integer PRIMARY KEY, nombre text,  apellido text)")

conexion.commit() # Guardo los cambios en la base datos