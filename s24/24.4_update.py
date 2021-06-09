import sqlite3

conexion = sqlite3.connect("db/datos1.db")
print("Conectado exitosamente")

cursor = conexion.cursor()

cursor.execute("UPDATE empleados SET nombre= 'Camilo Molano Herrera' where id =1")

conexion.commit()