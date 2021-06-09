import sqlite3

conexion = sqlite3.connect("db/datos1.db")
cursor = conexion.cursor()

cursor.execute("INSERT INTO empleados VALUES (2, 'Pilar Herrera', 1400) ")


conexion.commit()