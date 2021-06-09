import sqlite3

conexion = sqlite3.connect("db/datos1.db")
print("Conectado exitosamente")

cursor = conexion.cursor()

cursor.execute("CREATE TABLE empleados(id integer PRIMARY KEY, nombre text, salario real)")

conexion.commit() # Guardo los cambios en la base datos