import sqlite3

conexion = sqlite3.connect("db/datos1.db")
print("Conectado exitosamente")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM empleados")

data = cursor.fetchall()
#print(data)

''' for info in data:
    print(info[1]) '''

[print(linea) for linea in data]