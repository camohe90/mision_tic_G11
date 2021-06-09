import sqlite3

datos = (4,"Hally", 1250)

conexion = sqlite3.connect("db/datos1.db")
print("Conectado exitosamente")

cursor = conexion.cursor()

cursor.execute("INSERT INTO  empleados (id, nombre, salario) VALUES(?, ?, ?)", datos)

conexion.commit()