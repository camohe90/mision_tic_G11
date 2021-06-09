import sqlite3

conexion = sqlite3.connect("db/datos1.db")
print("Conectado exitosamente")

cursor = conexion.cursor()

cursor.execute("UPDATE empleados SET nombre= 'Bolt de pelicula', salario = 7500 where id =3")

conexion.commit()