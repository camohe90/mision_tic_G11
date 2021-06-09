import sqlite3

conexion = sqlite3.connect("db/datos1.db")
print("Conectado exitosamente")

cursor = conexion.cursor()

cursor.execute("INSERT INTO empleados VALUES (2, 'Pilar Herrera', 1400) ")
cursor.execute("INSERT INTO empleados VALUES (3, 'Bolt', 400) ")

conexion.commit()